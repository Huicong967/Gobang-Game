@echo off
echo ================================
echo 五子棋棋谱练习系统 - GitHub发布工具
echo 作者：Xu Huicong
echo ================================
echo.

echo 请确保已在GitHub创建了仓库：gobang-pattern-practice
echo.

set /p username="请输入你的GitHub用户名: "
if "%username%"=="" (
    echo 用户名不能为空！
    pause
    exit /b 1
)

echo.
echo 正在设置远程仓库...
git remote add origin https://github.com/%username%/gobang-pattern-practice.git

echo 正在重命名分支为main...
git branch -M main

echo 正在推送到GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================
    echo 🎉 发布成功！
    echo ================================
    echo.
    echo 仓库地址：https://github.com/%username%/gobang-pattern-practice
    echo.
    echo 接下来你可以：
    echo 1. 访问GitHub仓库完善项目信息
    echo 2. 添加项目截图
    echo 3. 创建Release版本
    echo 4. 添加项目标签（Topics）
    echo.
) else (
    echo.
    echo ❌ 推送失败！
    echo 可能的原因：
    echo 1. GitHub仓库不存在或名称错误
    echo 2. 网络连接问题  
    echo 3. 权限问题
    echo.
    echo 请检查上述问题后重试
)

pause