@echo off
setlocal
title Git GitHub Proxy Repair

rem Match this port to the HTTP/mixed port in your running proxy app.
set "PROXY=http://127.0.0.1:7890"
set "RESULT=0"

if /i "%~1"=="off" goto disable

echo Testing GitHub through %PROXY% ...
git -c "http.https://github.com.proxy=%PROXY%" -c http.lowSpeedLimit=1 -c http.lowSpeedTime=15 ls-remote https://github.com/neuhanxiaobo1/Claude-wiki.git HEAD
if errorlevel 1 (
    echo [FAIL] Connection failed. Check the proxy app and port. Git configuration was not changed.
    set "RESULT=1"
    goto end
)

git config --global http.https://github.com.proxy "%PROXY%"
if errorlevel 1 (
    echo [FAIL] Could not save Git proxy configuration.
    set "RESULT=1"
    goto end
)
echo [OK] Global GitHub proxy configured: %PROXY%
goto end

:disable
git config --global --unset-all http.https://github.com.proxy
set "RESULT=%errorlevel%"
if "%RESULT%"=="5" set "RESULT=0"
if not "%RESULT%"=="0" (
    echo [FAIL] Could not remove the global GitHub proxy setting.
    goto end
)
echo [OK] Removed the global GitHub proxy setting. Other proxy settings may still apply.

:end
echo.
rem Pause for double-click use; pass "on" or "off" for terminal use.
if "%~1"=="" pause
exit /b %RESULT%
