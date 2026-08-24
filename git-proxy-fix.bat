@echo off
title Git 代理修复启动器

rem 本地代理地址（如端口变了改这里）
set "PROXY=http://127.0.0.1:7897"

if /i "%~1"=="off" goto disable

git config --global http.https://github.com.proxy %PROXY%
echo.
echo  [OK] 已设置 git 走本地代理: %PROXY%
echo  正在测试连接 github.com ...
git ls-remote https://github.com/neuhanxiaobo1/Claude-wiki.git HEAD >nul 2>&1
if %errorlevel%==0 (
    echo  [OK] 连接正常，现在可以推送了。
) else (
    echo  [FAIL] 仍无法连接 github.com。请确认代理软件已开启（端口 7897）。
)
goto end

:disable
git config --global --unset http.https://github.com.proxy >nul 2>&1
echo.
echo  [OK] 已关闭 github.com 代理，恢复直连。
goto end

:end
echo.
pause
