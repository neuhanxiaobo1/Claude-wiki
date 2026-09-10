# -*- coding: utf-8 -*-
"""Merge master item list with Unpaywall results into final download-link CSV + MD (one-off helper)."""
import json
from pathlib import Path

base = str(Path(__file__).resolve().parent)
rows = json.load(open(base + "/items_master.json", encoding="utf-8"))
uw = json.load(open(base + "/unpaywall_results.json", encoding="utf-8"))

# DOIs supplemented via Crossref title search for items missing DOI in Zotero
crossref_supplement = {
    "S020": {"doi": "10.2514/6.2015-4193", "note": "Crossref 反查匹配（AIAA 2015），Zotero 原记录无 DOI，待核对"},
    "S147": {"doi": "10.1021/bk-1986-0301.ch017", "note": "Crossref 反查候选（ACS 书章 1986，原记录 1984），待核对"},
    "S177": {"doi": "10.4050/f-0071-2015-10240", "note": "Crossref 反查匹配（VFS 2015），Zotero 原记录无 DOI，待核对"},
}
# items left unresolved after Crossref
unresolved = {"S037": "无精确匹配，需手动检索（2011 年同名条目）",
              "S065": "无精确匹配，需手动检索（2017 年硬度/杨氏模量演化条目）"}

out_rows = []
for r in rows:
    sid, doi = r["sid"], r["doi"]
    rec = {"sid": sid, "key": r["key"], "title": r["title"], "collections": r["collections"],
           "itemType": r["itemType"], "doi": doi, "doi_source": "zotero",
           "is_oa": "", "download_url": "", "fallback_url": "", "note": ""}
    if doi:
        rec["fallback_url"] = "https://doi.org/" + doi
        u = uw.get(doi)
        if u and not u.get("error"):
            rec["is_oa"] = bool(u.get("is_oa"))
            rec["download_url"] = u.get("best_url_for_pdf") or u.get("best_url") or ""
            if rec["download_url"] and u.get("best_url_for_pdf"):
                rec["note"] = "OA pdf:" + (u.get("host") or "?")
            elif rec["download_url"]:
                rec["note"] = "OA page:" + (u.get("host") or "?")
            elif rec["is_oa"]:
                rec["note"] = "OA 但无直链"
            else:
                rec["note"] = "closed"
        elif u and u.get("error"):
            rec["note"] = "unpaywall error: " + u["error"][:60]
        else:
            rec["note"] = "no unpaywall record"
    else:
        sup = crossref_supplement.get(sid)
        if sup:
            rec["doi"] = sup["doi"]
            rec["doi_source"] = "crossref"
            rec["fallback_url"] = "https://doi.org/" + sup["doi"]
            u = uw.get(sup["doi"])
            if u and not u.get("error"):
                rec["is_oa"] = bool(u.get("is_oa"))
                rec["download_url"] = u.get("best_url_for_pdf") or u.get("best_url") or ""
                if rec["download_url"] and u.get("best_url_for_pdf"):
                    rec["note"] = sup["note"] + " | OA pdf:" + (u.get("host") or "?")
                elif rec["download_url"]:
                    rec["note"] = sup["note"] + " | OA page:" + (u.get("host") or "?")
                else:
                    rec["note"] = sup["note"] + " | closed"
            else:
                rec["note"] = sup["note"] + " | unpaywall 无记录"
        else:
            rec["note"] = unresolved.get(sid, "无 DOI")
            rec["fallback_url"] = "https://scholar.google.com/scholar?q=" + r["title"].replace(" ", "+")
    out_rows.append(rec)

json.dump(out_rows, open(base + "/pdf_links.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

n_oa = sum(1 for r in out_rows if r["download_url"])
n_closed = sum(1 for r in out_rows if r["doi"] and not r["download_url"])
n_nodoi = sum(1 for r in out_rows if not r["doi"])
print("total:", len(out_rows), "| OA with link:", n_oa, "| no OA link:", n_closed, "| still no DOI:", n_nodoi)

# CSV
import csv
with open(base + "/pdf_download_links.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["sid", "title", "doi", "is_oa", "download_url", "fallback_url", "note", "collections"])
    for r in out_rows:
        w.writerow([r["sid"], r["title"], r["doi"], r["is_oa"], r["download_url"], r["fallback_url"], r["note"], r["collections"]])
print("CSV written")

# MD table
lines = ["# scopus_1/2 PDF 下载链接清单（2026-09-09）", "",
         "共 %d 条。OA 可下载 %d 条；无 OA 链接 %d 条（用出版社 DOI 链接，需机构权限）；仍无 DOI %d 条。" % (
             len(out_rows), n_oa, n_closed, n_nodoi), "",
         "## 一、OA 可下载", "",
         "| S | 题名 | DOI | 下载链接 |", "|---|---|---|---|"]
for r in out_rows:
    if r["download_url"]:
        lines.append("| %s | %s | %s | [pdf](%s) |" % (r["sid"], r["title"][:60].replace("|", "/"), r["doi"], r["download_url"]))
lines += ["", "## 二、无 OA 直链（出版社/DOI 链接）", "",
          "| S | 题名 | DOI | 链接 |", "|---|---|---|---|"]
for r in out_rows:
    if r["doi"] and not r["download_url"]:
        lines.append("| %s | %s | %s | [doi](%s) |" % (r["sid"], r["title"][:60].replace("|", "/"), r["doi"], r["fallback_url"]))
lines += ["", "## 三、仍无 DOI（待手动检索）", "", "| S | 题名 | 备注 |", "|---|---|---|"]
for r in out_rows:
    if not r["doi"]:
        lines.append("| %s | %s | %s |" % (r["sid"], r["title"][:60].replace("|", "/"), r["note"]))
open(base + "/pdf_download_links.md", "w", encoding="utf-8").write("\n".join(lines))
print("MD written")
