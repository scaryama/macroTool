@echo off
chcp 65001 >nul
echo ========================================
echo Macro Tool 환경 설정 시작
echo ========================================
echo.

REM Python이 설치되어 있는지 확인
py --version >nul 2>&1
if errorlevel 1 (
    echo [오류] Python이 설치되어 있지 않습니다.
    echo Python을 먼저 설치해주세요.
    pause
    exit /b 1
)

echo [1/3] Python 버전 확인...
py --version
echo.

REM venv가 이미 존재하는지 확인
if exist "venv\" (
    echo [2/3] 기존 venv 폴더를 삭제합니다...
    rmdir /s /q venv
)

echo [2/3] 가상 환경(venv) 생성 중...
py -m venv venv
if errorlevel 1 (
    echo [오류] venv 생성에 실패했습니다.
    pause
    exit /b 1
)
echo 가상 환경 생성 완료!
echo.

echo [3/3] 패키지 설치 중...
call venv\Scripts\activate.bat
py -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo [오류] 패키지 설치에 실패했습니다.
    pause
    exit /b 1
)
echo.

echo ========================================
echo 설정 완료!
echo ========================================
echo.
echo 실행 방법:
echo   1. venv\Scripts\activate.bat 실행
echo   2. py macro_tool.py 실행
echo.
pause

