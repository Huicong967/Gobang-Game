@echo off
echo ================================
echo 五子棋项目 - GitHub上传工具
echo 作者：Xu Huicong
echo ================================
echo.

echo 请确认以下信息：
echo 1. GitHub仓库已创建
echo 2. 你有推送权限
echo 3. 网络连接正常
echo.

echo 常见的仓库URL格式：
echo - https://github.com/XuHuicong/Gobang-Game.git
echo - https://github.com/你的用户名/Gobang-Game.git
echo - git@github.com:XuHuicong/Gobang-Game.git (SSH)
echo.

set /p repo_url="请输入完整的仓库URL: "
if "%repo_url%"=="" (
    echo 仓库URL不能为空！
    pause
    exit /b 1
)

echo.
echo 正在设置远程仓库...
git remote add origin %repo_url%

echo 正在推送到GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================
    echo 🎉 上传成功！
    echo ================================
    echo.
    echo 你的项目已成功上传到GitHub！
    echo 仓库地址：%repo_url%
    echo.
    echo 接下来你可以：
    echo 1. 访问GitHub查看项目
    echo 2. 添加项目截图
    echo 3. 设置仓库主题标签
    echo 4. 创建Release版本
    echo.
) else (
    echo.
    echo ❌ 上传失败！
    echo.
    echo 可能的问题和解决方案：
    echo 1. 仓库不存在 - 检查仓库名称是否正确
    echo 2. 权限问题 - 确保你是仓库的所有者
    echo 3. 网络问题 - 检查网络连接
    echo 4. 认证问题 - 可能需要配置Git凭据
    echo.
    echo 如果是首次使用Git，可能需要：
    echo git config --global user.name "你的名字"
    echo git config --global user.email "你的邮箱"
    echo.
)

echo 当前远程仓库配置：
git remote -v

pause