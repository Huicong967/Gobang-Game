"""
五子棋棋谱练习系统主程序

作者：Xu Huicong
运行此文件启动游戏
"""

import sys
import os

# 添加当前目录到路径，确保可以导入自定义模块
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    from gui.game_window import GameWindow
except ImportError as e:
    print(f"导入错误：{e}")
    print("请确保所有必需的模块都已正确安装。")
    print("运行 'pip install -r requirements.txt' 安装依赖。")
    sys.exit(1)


def main():
    """游戏主函数"""
    print("正在启动五子棋棋谱练习系统...")
    print("作者：Xu Huicong")
    print("=" * 50)
    
    try:
        # 创建并运行游戏窗口
        game = GameWindow()
        game.run()
    except Exception as e:
        print(f"游戏运行时发生错误：{e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()