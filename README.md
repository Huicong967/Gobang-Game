# 五子棋棋谱对战系统 (Gobang Pattern Battle)

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

一个玩家vs电脑的五子棋棋谱对战系统。玩家执黑子，电脑执白子，按照经典棋谱进行对战练习，帮助玩家学习五子棋战术和开局技巧。

![游戏截图](https://via.placeholder.com/600x400/f0f0f0/333333?text=Game+Screenshot)

## 功能特点

- **玩家vs电脑对战**：玩家执黑子，电脑执白子，真实对战体验
- **经典棋谱对战**：基于真实的经典五子棋棋谱进行对战练习
- **智能走法验证**：实时验证玩家走法，与标准棋谱对比
- **错误纠正机制**：三次错误后自动演示正确走法
- **电脑自动应战**：电脑严格按照棋谱进行回应
- **棋谱深度解析**：完成对战后显示详细的战术分析
- **直观图形界面**：清晰的棋盘显示和实时状态反馈

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

### 对战模式
- **玩家执黑子**：你始终执黑子，享有先手优势
- **电脑执白子**：电脑严格按照棋谱执白子进行应战
- **回合制对战**：玩家下棋后，电脑立即按棋谱回应
- **实时验证**：每步都会验证是否符合标准棋谱走法
- **智能提示**：走错时给出位置提示，最多3次机会
- **自动演示**：3次错误后系统自动演示正确走法并继续对战
- **胜负分析**：对战结束后显示详细的战术解析

### 操作方式
- 鼠标点击棋盘交叉点下黑子
- 观察电脑的白子回应
- 根据提示调整走法
- 完成对战后学习棋谱分析

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