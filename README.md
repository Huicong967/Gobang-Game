# Gobang Pattern Battle System / 五子棋棋谱对战系统

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![AI-Assisted](https://img.shields.io/badge/Development-AI--Assisted-purple.svg)

**🤖 AI-Assisted Development / AI辅助开发**
This project was developed with the assistance of AI coding agents. / 本项目由AI代理辅助编码完成。

A player vs computer Gobang pattern battle system. Players use black stones, computer uses white stones, battle according to classic patterns to help players learn Gobang tactics and opening strategies.

一个玩家vs电脑的五子棋棋谱对战系统。玩家执黑子，电脑执白子，按照经典棋谱进行对战练习，帮助玩家学习五子棋战术和开局技巧。

![游戏截图](https://via.placeholder.com/600x400/f0f0f0/333333?text=Game+Screenshot)

## Features / 功能特点

- **🌍 Language Selection / 语言选择**: Choose English or Chinese at startup for complete single-language experience / 启动时选择英文或中文，享受完整的单语体验
- **🎯 Single Language Display / 单语显示**: All interface elements in your chosen language - no more mixed bilingual text / 所有界面元素使用您选择的语言 - 不再有混合双语文本
- **📚 Localized Patterns / 本地化棋谱**: Pattern names, descriptions, and analysis dynamically translated to your language / 棋谱名称、描述和分析动态翻译为您的语言
- **🤖 Player vs Computer Battle / 玩家vs电脑对战**: Player uses white stones, computer uses black stones for endgame training / 玩家执白子，电脑执黑子，进行残局训练
- **📖 Classic Pattern Training / 经典棋谱训练**: Practice based on real classic Gobang endgame patterns / 基于真实的经典五子棋残局棋谱进行练习
- **🎯 Intelligent Move Validation / 智能走法验证**: Real-time validation of player moves against standard patterns / 实时验证玩家走法，与标准棋谱对比
- **💡 Smart Error Correction / 智能错误纠正**: Localized hints with up to 3 chances, auto-demonstration after errors / 本地化提示最多3次机会，错误后自动演示
- **🔍 Pattern Deep Analysis / 棋谱深度解析**: Detailed tactical analysis in your preferred language / 使用您的首选语言显示详细的战术分析
- **🎮 Intuitive GUI / 直观图形界面**: Clean, localized interface with real-time status feedback / 清晰的本地化界面和实时状态反馈

## Requirements / 安装要求

- Python 3.7+
- Dependencies listed in `requirements.txt` / 依赖库请参见 `requirements.txt`

## Quick Start / 快速开始

### Method 1: Download from GitHub / 方法一：从GitHub下载

1. **Download the project / 下载项目**:
   - Visit GitHub repository / 访问GitHub仓库: https://github.com/Huicong967/Gobang-Game
   - Click "Code" → "Download ZIP" / 点击"Code"→"Download ZIP"
   - Extract to your desired location / 解压到指定位置

2. **Or clone the project / 或者克隆项目**:
```bash
git clone https://github.com/Huicong967/Gobang-Game.git
cd Gobang-Game
```

### Method 2: Install dependencies / 方法二：安装依赖

3. **Install Python dependencies / 安装Python依赖**:
```bash
pip install -r requirements.txt
```

Or install manually / 或手动安装:
```bash
pip install pygame numpy
```

### Method 3: Launch the game / 方法三：启动游戏

4. **Run the game / 运行游戏**:

**Option A / 选项A**: Command line / 命令行:
```bash
python main.py
```

**Option B / 选项B**: Windows batch file / Windows批处理文件:
```bash
# Double-click / 双击运行
启动游戏.bat
```

**Option C / 选项C**: Direct Python execution / 直接Python执行:
```bash
# Navigate to game directory first / 首先进入游戏目录
cd "d:\Polyu program\Gobang game"
python main.py
```

### First Time Setup / 首次设置

5. **Language Selection / 语言选择**:
   - When first launched, choose your preferred language / 首次启动时，选择您的首选语言
   - English: Complete English interface / 英文：完整英文界面
   - Chinese: Complete Chinese interface / 中文：完整中文界面
   - Language setting is saved automatically / 语言设置自动保存

6. **Game Features / 游戏特色**:
   - ✅ **Single Language Display / 单语显示**: No more mixed bilingual text / 不再有混合双语文本
   - ✅ **Pattern Localization / 棋谱本地化**: Pattern names, descriptions, and analysis in your chosen language / 棋谱名称、描述和分析使用您选择的语言
   - ✅ **Intelligent Hints / 智能提示**: Error messages and area hints in your preferred language / 错误消息和区域提示使用您的首选语言
   - ✅ **Complete User Experience / 完整用户体验**: Unified language throughout the entire game / 整个游戏使用统一语言

## Game Instructions / 游戏说明

### 🌍 Language Selection / 语言选择
- **First Launch / 首次启动**: Choose your preferred language (English/Chinese) / 选择您的首选语言（英文/中文）
- **Single Language Experience / 单语体验**: All game content displays in your chosen language / 所有游戏内容使用您选择的语言显示
- **No Mixed Text / 无混合文本**: Clean, professional single-language interface / 清洁、专业的单语界面

### 🎮 Endgame Training Mode / 残局训练模式
- **Player Uses White Stones / 玩家执白子**: You use white stones to find winning moves / 你执白子寻找制胜走法
- **Computer Uses Black Stones / 电脑执黑子**: Computer follows patterns for black stone setup / 电脑按棋谱执黑子进行布局
- **Pattern-Based Training / 基于棋谱的训练**: Practice solving classic endgame positions / 练习解决经典残局局面
- **Real-Time Validation / 实时验证**: Each move is validated against correct solutions / 每步都会验证是否符合正确解法
- **Smart Hints / 智能提示**: Localized area hints when moves are incorrect / 走错时给出本地化的区域提示
- **Auto Demonstration / 自动演示**: System demonstrates correct moves after 3 errors / 3次错误后系统演示正确走法
- **Victory Analysis / 胜利分析**: Detailed tactical analysis in your language after completion / 完成后用您的语言显示详细的战术解析

### 🎯 Operation / 操作方式
- Click board intersections to place white stones / 鼠标点击棋盘交叉点下白子
- Follow pattern requirements to find winning moves / 按照棋谱要求寻找制胜走法
- Use hints and analysis to improve understanding / 利用提示和分析提高理解
- Study localized pattern analysis after solving / 解决后学习本地化的棋谱分析

## Project Structure / 项目结构

```
gobang-game/
│
├── main.py              # Main program entry / 主程序入口
├── game/                # Game core modules / 游戏核心模块
│   ├── __init__.py
│   ├── board.py         # Board logic / 棋盘逻辑
│   ├── pattern.py       # Pattern management / 棋谱管理
│   └── validator.py     # Move validator / 走法验证器
├── gui/                 # GUI modules / 图形界面模块
│   ├── __init__.py
│   └── game_window.py   # Game window / 游戏窗口
├── patterns/            # Pattern data files / 棋谱数据文件
│   └── classic/         # Classic patterns / 经典棋谱
├── assets/              # Resource files / 资源文件
│   └── images/          # Image resources / 图片资源
├── tests/               # Test files / 测试文件
├── requirements.txt     # Dependencies list / 依赖列表
└── README.md           # Project description / 项目说明
```

## Development Plan / 开发计划

- [x] Basic game logic implementation / 基础游戏逻辑实现
- [x] Pattern management system / 棋谱管理系统
- [x] Move validation mechanism / 走法验证机制
- [x] GUI development / 图形界面开发
- [x] Error hint system / 错误提示系统
- [x] Pattern analysis function / 棋谱解析功能
- [ ] More classic patterns collection / 更多经典棋谱收录
- [ ] Learning progress statistics / 学习进度统计

## Contributing / 贡献指南

Welcome to submit Issues and Pull Requests to improve this project! / 欢迎提交 Issue 和 Pull Request 来改进这个项目！

## License / 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. / 本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## Author / 作者

- **Xu Huicong** - Project creator and primary developer / 项目创建者和主要开发者
- **AI Coding Agents** - Technical implementation assistance / 技术实现辅助
- GitHub: [@Huicong967](https://github.com/Huicong967)

## AI Development Details / AI开发详情

This project demonstrates effective human-AI collaboration in software development:
- **Human Direction**: Project vision, game rules, and user experience design / 人类指导：项目愿景、游戏规则和用户体验设计
- **AI Implementation**: Code architecture, technical implementation, and optimization / AI实现：代码架构、技术实现和优化

For detailed information about the AI-assisted development process, see [`AI_DEVELOPMENT_ACKNOWLEDGMENT.md`](AI_DEVELOPMENT_ACKNOWLEDGMENT.md).

有关AI辅助开发过程的详细信息，请参阅 [`AI_DEVELOPMENT_ACKNOWLEDGMENT.md`](AI_DEVELOPMENT_ACKNOWLEDGMENT.md)。

## Acknowledgments / 致谢

Thanks to all developers and AI systems that have contributed to this project. / 感谢所有为这个项目做出贡献的开发者和AI系统。

Special thanks to:
- **AI Coding Agents**: For technical implementation and code optimization / AI编码代理：技术实现和代码优化
- **Open Source Community**: For the foundational libraries and tools / 开源社区：基础库和工具支持