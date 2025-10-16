#!/usr/bin/env python3
"""
五子棋残局训练系统启动器
Gobang Endgame Training System Launcher
作者：Xu Huicong / Author: Xu Huicong
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """启动五子棋残局训练系统"""
    print("=" * 50)
    print("Starting Gobang Endgame Training System...")
    print("启动五子棋残局训练系统...")
    print("Author / 作者：Xu Huicong")
    print("=" * 50)
    print()
    
    # 获取脚本所在目录
    script_dir = Path(__file__).parent.absolute()
    main_py = script_dir / "main.py"
    
    # 检查main.py是否存在
    if not main_py.exists():
        print("❌ Error: main.py not found!")
        print("❌ 错误：找不到main.py文件！")
        input("Press Enter to exit... / 按回车键退出...")
        return
    
    try:
        # 启动主程序
        print("🚀 Launching game... / 正在启动游戏...")
        subprocess.run([sys.executable, str(main_py)], cwd=script_dir, check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching game: {e}")
        print(f"❌ 启动游戏时出错：{e}")
        
    except FileNotFoundError:
        print("❌ Python interpreter not found!")
        print("❌ 未找到Python解释器！")
        
    except KeyboardInterrupt:
        print("\n🛑 Game interrupted by user")
        print("🛑 用户中断了游戏")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print(f"❌ 意外错误：{e}")
    
    finally:
        print("\nGame session ended / 游戏会话结束")
        input("Press Enter to exit... / 按回车键退出...")

if __name__ == "__main__":
    main()