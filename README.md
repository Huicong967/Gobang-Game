# 五子棋棋谱练习系统 (Gobang Pattern Practice)

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

一个基于经典棋谱的五子棋学习练习系统，帮助玩家通过实战练习提高五子棋水平。

![游戏截图](https://via.placeholder.com/600x400/f0f0f0/333333?text=Game+Screenshot)

## 功能特点

- 经典五子棋棋谱库练习
- 实时走法验证与提示
- 错误纠正机制（三次错误自动显示正解）
- 棋谱解析与胜利原理说明
- 图形化用户界面
- 进度跟踪和学习记录

## 安装要求

- Python 3.7+
- 依赖库请参见 `requirements.txt`

## 快速开始

1. 克隆项目到本地：
```bash
git clone https://github.com/Huicong967/Gobang-Game.git
cd Gobang-Game
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行游戏：
```bash
python main.py
```

或者双击 `启动游戏.bat`（Windows用户）

## 游戏说明

### 游戏模式
- 棋谱练习模式：按照经典棋谱进行练习
- 实时验证：每步走法都会与棋谱对比
- 错误提示：走错时给出提示，最多允许3次错误
- 自动演示：3次错误后自动显示正确走法
- 棋谱解析：完成后显示该棋谱的战术分析

### 操作方式
- 鼠标点击棋盘位置下棋
- 按照棋谱提示进行练习
- 查看错误提示和正确走法
- 学习棋谱背后的战术原理

## 项目结构

```
gobang-game/
│
├── main.py              # 主程序入口
├── game/                # 游戏核心模块
│   ├── __init__.py
│   ├── board.py         # 棋盘逻辑
│   ├── pattern.py       # 棋谱管理
│   └── validator.py     # 走法验证器
├── gui/                 # 图形界面模块
│   ├── __init__.py
│   └── game_window.py   # 游戏窗口
├── patterns/            # 棋谱数据文件
│   └── classic/         # 经典棋谱
├── assets/              # 资源文件
│   └── images/          # 图片资源
├── tests/               # 测试文件
├── requirements.txt     # 依赖列表
└── README.md           # 项目说明
```

## 开发计划

- [x] 基础游戏逻辑实现
- [x] 棋谱管理系统
- [x] 走法验证机制
- [x] 图形界面开发
- [x] 错误提示系统
- [x] 棋谱解析功能
- [ ] 更多经典棋谱收录
- [ ] 学习进度统计

## 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 作者

- **Xu Huicong** - 项目创建者和唯一开发者
- GitHub: [@Huicong967](https://github.com/Huicong967)

## 致谢

感谢所有为这个项目做出贡献的开发者。