@echo off
echo ====================================================
echo    Gobang Endgame Training System / 五子棋残局训练系统
echo    Starting game... / 正在启动游戏...
echo ====================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo 错误：未安装Python或未添加到系统路径！
    echo.
    echo Please install Python 3.7+ from https://python.org
    echo 请从 https://python.org 安装Python 3.7+
    pause
    exit /b 1
)

REM Check if required modules are available
echo Checking dependencies... / 检查依赖项...
python -c "import pygame, numpy" >nul 2>&1
if errorlevel 1 (
    echo Installing missing dependencies... / 安装缺失的依赖项...
    pip install pygame numpy
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies!
        echo 错误：安装依赖项失败！
        echo Please run: pip install pygame numpy
        echo 请运行：pip install pygame numpy
        pause
        exit /b 1
    )
)

REM Launch the game
echo.
echo Launching Gobang Endgame Training System...
echo 正在启动五子棋残局训练系统...
echo.
python main.py

if errorlevel 1 (
    echo.
    echo Game exited with error / 游戏异常退出
    pause
) else (
    echo.
    echo Game closed normally / 游戏正常关闭
)