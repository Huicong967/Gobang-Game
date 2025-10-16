#!/usr/bin/env python3
"""
GitHub上传工具
GitHub Upload Tool
作者：Xu Huicong / Author: Xu Huicong
"""

import os
import sys
import subprocess
import urllib.parse
from pathlib import Path

class GitHubUploader:
    def __init__(self):
        self.common_repos = {
            "1": "https://github.com/Huicong967/Gobang-Game.git",
            "2": "https://github.com/XuHuicong/Gobang-Game.git",
        }
        
    def run_git_command(self, command, check=True):
        """执行Git命令"""
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True,
                check=check
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.CalledProcessError as e:
            return False, "", str(e)
    
    def validate_repo_url(self, url):
        """验证仓库URL格式"""
        url = url.strip()
        
        # 常见的GitHub URL格式
        github_patterns = [
            "https://github.com/",
            "git@github.com:",
            "ssh://git@github.com/"
        ]
        
        if any(pattern in url for pattern in github_patterns):
            return True, url
        
        # 尝试补全URL
        if "/" in url and not url.startswith("http"):
            full_url = f"https://github.com/{url}"
            if not full_url.endswith(".git"):
                full_url += ".git"
            return True, full_url
            
        return False, url
    
    def get_repository_url(self):
        """获取仓库URL"""
        print("📋 Common repository formats / 常见仓库格式:")
        for key, repo in self.common_repos.items():
            print(f"  {key}. {repo}")
        print("  3. Custom URL / 自定义URL")
        print()
        
        choice = input("Select option (1-3) or enter URL directly / 选择选项(1-3)或直接输入URL: ").strip()
        
        if choice in self.common_repos:
            return self.common_repos[choice]
        elif choice == "3":
            url = input("Enter repository URL / 输入仓库URL: ").strip()
        else:
            # 直接输入的URL
            url = choice
            
        if not url:
            print("❌ Repository URL cannot be empty! / 仓库URL不能为空！")
            return None
            
        is_valid, validated_url = self.validate_repo_url(url)
        if not is_valid:
            print(f"❌ Invalid repository URL format! / 无效的仓库URL格式！")
            return None
            
        return validated_url
    
    def check_git_config(self):
        """检查Git配置"""
        print("🔧 Checking Git configuration... / 检查Git配置...")
        
        # 检查用户名和邮箱
        success, username, _ = self.run_git_command("git config user.name", check=False)
        success2, email, _ = self.run_git_command("git config user.email", check=False)
        
        if not success or not username.strip():
            name = input("Enter your name for Git / 输入Git用户名: ").strip()
            if name:
                self.run_git_command(f'git config user.name "{name}"')
        else:
            print(f"✅ Git user: {username.strip()}")
            
        if not success2 or not email.strip():
            user_email = input("Enter your email for Git / 输入Git邮箱: ").strip()
            if user_email:
                self.run_git_command(f'git config user.email "{user_email}"')
        else:
            print(f"✅ Git email: {email.strip()}")
    
    def setup_and_upload(self, repo_url):
        """设置并上传到GitHub"""
        # 检查是否已有未提交的更改
        success, stdout, _ = self.run_git_command("git status --porcelain", check=False)
        if success and stdout.strip():
            print("📝 Found uncommitted changes / 发现未提交的更改")
            
            commit = input("Commit changes? (y/n) / 提交更改？(y/n): ").lower()
            if commit == 'y':
                message = input("Enter commit message (press Enter for default) / 输入提交信息（回车使用默认）: ").strip()
                if not message:
                    message = "Update project files"
                
                print("📦 Adding changes... / 添加更改...")
                self.run_git_command("git add .")
                
                print("💾 Committing... / 提交中...")
                success, _, stderr = self.run_git_command(f'git commit -m "{message}"')
                if not success:
                    print(f"❌ Commit failed: {stderr}")
                    return False
        
        # 设置远程仓库
        print("🔗 Setting up remote repository... / 设置远程仓库...")
        
        # 移除现有的origin（如果存在）
        self.run_git_command("git remote remove origin", check=False)
        
        # 添加新的origin
        success, _, stderr = self.run_git_command(f"git remote add origin {repo_url}")
        if not success:
            print(f"❌ Failed to add remote: {stderr}")
            return False
        
        # 推送到GitHub
        print("🚀 Uploading to GitHub... / 上传到GitHub...")
        success, stdout, stderr = self.run_git_command("git push -u origin main")
        
        if success:
            print("\n" + "=" * 50)
            print("🎉 Upload successful! / 上传成功！")
            print("=" * 50)
            print(f"📍 Repository: {repo_url}")
            print("\n📋 Next steps / 接下来可以做:")
            print("1. Visit GitHub to view your project / 访问GitHub查看项目")
            print("2. Add project description / 添加项目描述")
            print("3. Set repository topics / 设置仓库主题")
            print("4. Create release version / 创建发布版本")
            return True
        else:
            print("\n❌ Upload failed! / 上传失败！")
            print("\n🔍 Possible solutions / 可能的解决方案:")
            print("1. Repository doesn't exist - check repository name / 仓库不存在 - 检查仓库名")
            print("2. Permission denied - ensure you own the repository / 权限不足 - 确保你拥有仓库")
            print("3. Network issues - check internet connection / 网络问题 - 检查网络连接")
            print("4. Authentication required - may need to configure credentials / 需要身份验证 - 可能需要配置凭据")
            print(f"\nError details / 错误详情:\n{stderr}")
            
            # 显示当前远程配置
            print("\n📋 Current remote configuration / 当前远程配置:")
            success, remotes, _ = self.run_git_command("git remote -v", check=False)
            if success:
                print(remotes)
            
            return False
    
    def upload(self):
        """执行完整的上传流程"""
        print("=" * 50)
        print("五子棋项目 - GitHub上传工具")
        print("Gobang Project - GitHub Upload Tool")
        print("作者：Xu Huicong / Author: Xu Huicong")
        print("=" * 50)
        print()
        
        # 检查Git配置
        self.check_git_config()
        print()
        
        # 获取仓库URL
        repo_url = self.get_repository_url()
        if not repo_url:
            return False
        
        print(f"\n🎯 Target repository: {repo_url}")
        confirm = input("Proceed with upload? (y/n) / 继续上传？(y/n): ").lower()
        
        if confirm != 'y':
            print("Upload cancelled / 上传已取消")
            return False
        
        return self.setup_and_upload(repo_url)

def main():
    uploader = GitHubUploader()
    
    try:
        success = uploader.upload()
        
        if not success:
            print("\n💡 Need help? / 需要帮助？")
            print("- Make sure the repository exists on GitHub / 确保GitHub上仓库存在")
            print("- Check your network connection / 检查网络连接")
            print("- Verify your GitHub credentials / 验证GitHub凭据")
            
    except KeyboardInterrupt:
        print("\n🛑 Upload interrupted / 上传被中断")
    except Exception as e:
        print(f"\n❌ Unexpected error / 意外错误: {e}")
    
    input("\nPress Enter to exit... / 按回车键退出...")

if __name__ == "__main__":
    main()