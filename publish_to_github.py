#!/usr/bin/env python3
"""
GitHub发布工具
GitHub Publishing Tool
作者：Xu Huicong / Author: Xu Huicong
"""

import os
import sys
import subprocess
from pathlib import Path

class GitHubPublisher:
    def __init__(self):
        self.username = "Huicong967"
        self.repo_name = "Gobang-Game"
        self.repo_url = f"https://github.com/{self.username}/{self.repo_name}.git"
        
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
    
    def check_git_status(self):
        """检查Git状态"""
        print("📋 Checking git status... / 检查Git状态...")
        success, stdout, stderr = self.run_git_command("git status --porcelain")
        
        if not success:
            print("❌ Not a git repository / 不是Git仓库")
            return False
            
        if stdout.strip():
            print("📝 Found uncommitted changes / 发现未提交的更改:")
            print(stdout)
            
            commit = input("Commit changes now? (y/n) / 现在提交更改吗？(y/n): ").lower()
            if commit == 'y':
                message = input("Enter commit message / 输入提交信息: ")
                if not message:
                    message = "Update project files"
                
                print("📦 Adding all changes... / 添加所有更改...")
                self.run_git_command("git add .")
                
                print("💾 Committing changes... / 提交更改...")
                success, _, _ = self.run_git_command(f'git commit -m "{message}"')
                if not success:
                    print("❌ Failed to commit changes / 提交更改失败")
                    return False
        
        return True
    
    def setup_remote(self):
        """设置远程仓库"""
        print("🔗 Setting up remote repository... / 设置远程仓库...")
        
        # 检查是否已有remote
        success, stdout, _ = self.run_git_command("git remote get-url origin", check=False)
        
        if success:
            print(f"✅ Remote already exists: {stdout.strip()}")
            print(f"✅ 远程仓库已存在: {stdout.strip()}")
        else:
            # 添加remote
            success, _, stderr = self.run_git_command(f"git remote add origin {self.repo_url}")
            if success:
                print(f"✅ Remote added: {self.repo_url}")
                print(f"✅ 已添加远程仓库: {self.repo_url}")
            else:
                print(f"❌ Failed to add remote: {stderr}")
                print(f"❌ 添加远程仓库失败: {stderr}")
                return False
        
        return True
    
    def push_to_github(self):
        """推送到GitHub"""
        print("🚀 Pushing to GitHub... / 推送到GitHub...")
        
        # 设置main分支
        print("🔄 Setting main branch... / 设置main分支...")
        self.run_git_command("git branch -M main", check=False)
        
        # 推送
        success, stdout, stderr = self.run_git_command("git push -u origin main")
        
        if success:
            print("\n" + "=" * 50)
            print("🎉 Publishing successful! / 发布成功！")
            print("=" * 50)
            print(f"📍 Repository URL / 仓库地址: https://github.com/{self.username}/{self.repo_name}")
            print("\n📋 Next steps / 接下来可以做:")
            print("1. Visit GitHub repository / 访问GitHub仓库")
            print("2. Add project screenshots / 添加项目截图") 
            print("3. Create release version / 创建发布版本")
            print("4. Add project topics / 添加项目标签")
            return True
        else:
            print("\n❌ Publishing failed! / 发布失败！")
            print("可能的原因 / Possible reasons:")
            print("1. Repository doesn't exist / 仓库不存在")
            print("2. Network connection issues / 网络连接问题")
            print("3. Permission issues / 权限问题")
            print("4. Authentication required / 需要身份验证")
            print(f"\nError details / 错误详情: {stderr}")
            return False
    
    def publish(self):
        """执行完整的发布流程"""
        print("=" * 50)
        print("五子棋残局训练系统 - GitHub发布工具")
        print("Gobang Endgame Training System - GitHub Publisher")
        print("作者：Xu Huicong / Author: Xu Huicong")
        print("=" * 50)
        print()
        
        print(f"🎯 Target repository / 目标仓库: {self.repo_url}")
        print()
        
        # 检查Git状态
        if not self.check_git_status():
            return False
        
        # 设置远程仓库
        if not self.setup_remote():
            return False
        
        # 推送到GitHub
        return self.push_to_github()

def main():
    publisher = GitHubPublisher()
    
    try:
        success = publisher.publish()
        if not success:
            print("\n💡 Troubleshooting tips / 故障排除提示:")
            print("- Ensure repository exists on GitHub / 确保GitHub上仓库存在")
            print("- Check your internet connection / 检查网络连接")
            print("- Verify Git credentials / 验证Git凭据")
            
    except KeyboardInterrupt:
        print("\n🛑 Publishing interrupted / 发布被中断")
    except Exception as e:
        print(f"\n❌ Unexpected error / 意外错误: {e}")
    
    input("\nPress Enter to exit... / 按回车键退出...")

if __name__ == "__main__":
    main()