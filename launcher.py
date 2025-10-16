#!/usr/bin/env python3
"""
五子棋残局训练系统 - 统一启动器
Gobang Endgame Training System - Universal Launcher
作者：Xu Huicong / Author: Xu Huicong
"""

import os
import sys
import subprocess
from pathlib import Path

def show_menu():
    """显示主菜单"""
    print("=" * 60)
    print("🏮 五子棋残局训练系统 | Gobang Endgame Training System")
    print("👨‍💻 作者：Xu Huicong | Author: Xu Huicong")
    print("=" * 60)
    print()
    print("📋 Select an option / 选择一个选项:")
    print()
    print("1. 🎮 Start Game / 开始游戏")
    print("2. 📤 Publish to GitHub / 发布到GitHub")
    print("3. 🔄 Upload to GitHub / 上传到GitHub") 
    print("4. 📖 Show Project Info / 显示项目信息")
    print("5. ❌ Exit / 退出")
    print()

def start_game():
    """启动游戏"""
    script_dir = Path(__file__).parent.absolute()
    
    # 优先使用gui启动
    gui_main = script_dir / "gui" / "game_window.py"
    main_py = script_dir / "main.py"
    
    if gui_main.exists():
        target_file = gui_main
        print("🎮 Starting GUI version... / 启动图形界面版本...")
    elif main_py.exists():
        target_file = main_py
        print("🎮 Starting main version... / 启动主版本...")
    else:
        print("❌ Game files not found! / 找不到游戏文件！")
        return False
    
    try:
        subprocess.run([sys.executable, str(target_file)], cwd=script_dir)
        return True
    except Exception as e:
        print(f"❌ Failed to start game: {e}")
        print(f"❌ 启动游戏失败: {e}")
        return False

def publish_to_github():
    """发布到GitHub"""
    script_dir = Path(__file__).parent.absolute()
    publisher = script_dir / "publish_to_github.py"
    
    if not publisher.exists():
        print("❌ Publisher script not found! / 找不到发布脚本！")
        return False
    
    try:
        subprocess.run([sys.executable, str(publisher)], cwd=script_dir)
        return True
    except Exception as e:
        print(f"❌ Failed to run publisher: {e}")
        return False

def upload_to_github():
    """上传到GitHub"""
    script_dir = Path(__file__).parent.absolute()
    uploader = script_dir / "upload_to_github.py"
    
    if not uploader.exists():
        print("❌ Uploader script not found! / 找不到上传脚本！")
        return False
    
    try:
        subprocess.run([sys.executable, str(uploader)], cwd=script_dir)
        return True
    except Exception as e:
        print(f"❌ Failed to run uploader: {e}")
        return False

def show_project_info():
    """显示项目信息"""
    script_dir = Path(__file__).parent.absolute()
    
    print("\n" + "=" * 60)
    print("📋 Project Information / 项目信息")
    print("=" * 60)
    print(f"📁 Project Directory / 项目目录: {script_dir}")
    print(f"🐍 Python Version / Python版本: {sys.version}")
    
    # 检查主要文件
    important_files = {
        "main.py": "主程序文件",
        "gui/game_window.py": "图形界面文件", 
        "game/pattern.py": "棋谱管理器",
        "game/validator.py": "走法验证器",
        "README.md": "项目说明文档",
        "requirements.txt": "依赖清单"
    }
    
    print("\n📂 File Status / 文件状态:")
    for filename, description in important_files.items():
        filepath = script_dir / filename
        status = "✅ 存在" if filepath.exists() else "❌ 不存在"
        print(f"  {filename:<20} | {description:<15} | {status}")
    
    # Git信息
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"], 
            cwd=script_dir,
            capture_output=True, 
            text=True
        )
        if result.returncode == 0:
            changes = result.stdout.strip()
            git_status = "🔄 有未提交更改" if changes else "✅ 工作目录干净"
        else:
            git_status = "❓ 不是Git仓库"
    except:
        git_status = "❓ Git未安装或不可用"
    
    print(f"\n📊 Git Status / Git状态: {git_status}")
    
    # GitHub仓库信息
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"], 
            cwd=script_dir,
            capture_output=True, 
            text=True
        )
        if result.returncode == 0:
            remote_url = result.stdout.strip()
            print(f"🌐 Remote Repository / 远程仓库: {remote_url}")
        else:
            print("🌐 Remote Repository / 远程仓库: 未配置")
    except:
        print("🌐 Remote Repository / 远程仓库: 无法检查")
    
    print("=" * 60)

def main():
    """主函数"""
    while True:
        show_menu()
        
        try:
            choice = input("Enter your choice (1-5) / 输入你的选择 (1-5): ").strip()
            
            if choice == "1":
                print("\n🎮 Launching game... / 启动游戏中...")
                start_game()
                
            elif choice == "2":
                print("\n📤 Publishing to GitHub... / 发布到GitHub中...")
                publish_to_github()
                
            elif choice == "3":
                print("\n🔄 Uploading to GitHub... / 上传到GitHub中...")
                upload_to_github()
                
            elif choice == "4":
                show_project_info()
                
            elif choice == "5":
                print("\n👋 Goodbye! / 再见！")
                break
                
            else:
                print("\n❌ Invalid choice! Please enter 1-5.")
                print("❌ 无效选择！请输入1-5。")
                
        except KeyboardInterrupt:
            print("\n\n👋 Exiting... / 退出中...")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
        
        if choice in ["1", "2", "3", "4"]:
            input("\nPress Enter to continue... / 按回车键继续...")

if __name__ == "__main__":
    main()