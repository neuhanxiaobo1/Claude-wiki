# -*- coding: utf-8 -*-
"""Query Unpaywall API for OA status of all master-list DOIs (one-off helper)."""
import json
from pathlib import Path
import time
import urllib.request

base = str(Path(__file__).resolve().parent)
rows = json.load(open(base + "/items_master.json", encoding="utf-8"))
out = {}
for i, r in enumerate(rows):
    doi = r["doi"]
    if not doi:
        continue
    url = "https://api.unpaywall.org/v2/" + doi + "?email=youthcookie@gmail.com"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research helper)"})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                d = json.loads(resp.read().decode())
            best = d.get("best_oa_location") or {}
            out[doi] = {
                "is_oa": d.get("is_oa"),
                "title": d.get("title"),
                "best_url_for_pdf": best.get("url_for_pdf"),
                "best_url": best.get("url"),
                "host": (best.get("host_type") or ""),
                "version": (best.get("version") or ""),
                "locations": [
                    {
                        "url_for_pdf": loc.get("url_for_pdf"),
                        "url": loc.get("url"),
                        "host": (loc.get("host_type") or ""),
                        "version": (loc.get("version") or ""),
                    }
                    for loc in (d.get("oa_locations") or [])[:5]
                ],
                "error": None,
            }
            break
        except Exception as e:  # noqa: BLE001
            if attempt == 0:
                time.sleep(3)
            else:
                out[doi] = {"is_oa": None, "error": str(e)[:200], "locations": []}
    time.sleep(1)
    if i % 20 == 0:
        print(i, "done", flush=True)
json.dump(out, open(base + "/unpaywall_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("DONE", len(out))
