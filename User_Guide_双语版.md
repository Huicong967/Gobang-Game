# Gobang Endgame Training System User Guide / 五子棋残局训练系统使用说明

## Download and Installation / 下载和安装

### Step 1: Download the Game / 第一步：下载游戏

**Method A: GitHub Download / 方法A：GitHub下载**
1. Visit the project page / 访问项目页面: https://github.com/Huicong967/Gobang-Game
2. Click "Code" → "Download ZIP" / 点击"Code"→"Download ZIP"  
3. Extract the ZIP file to your desired location / 将ZIP文件解压到指定位置

**Method B: Git Clone / 方法B：Git克隆**
```bash
git clone https://github.com/Huicong967/Gobang-Game.git
cd Gobang-Game
```

### Step 2: Install Dependencies / 第二步：安装依赖

**Automatic Installation (Recommended) / 自动安装（推荐）**
```bash
pip install -r requirements.txt
```

**Manual Installation / 手动安装**
```bash
pip install pygame numpy
```

### Step 3: Launch the Game / 第三步：启动游戏

**Method A: Windows Batch File / 方法A：Windows批处理文件**
- Double-click `启动游戏.bat` / 双击 `启动游戏.bat`
- The script will automatically check dependencies and launch the game / 脚本会自动检查依赖并启动游戏

**Method B: Command Line / 方法B：命令行**
```bash
python main.py
```

**Method C: Direct Python / 方法C：直接Python运行**
```bash
cd "path/to/Gobang-Game"
python main.py
```

## Game Introduction / 游戏简介

This is an endgame training system where players practice solving classic Gobang endgame positions. Players use white stones to find winning moves while the computer sets up black stone patterns according to classic endgames.

这是一个残局训练系统，玩家练习解决经典五子棋残局。玩家执白子寻找制胜走法，电脑按照经典残局执黑子进行布局。

## 🌍 New Feature: Language Selection / 新功能：语言选择

### Complete Single-Language Experience / 完整的单语体验
- **At Startup / 启动时**: Choose your preferred language (English/Chinese) / 选择您的首选语言（英文/中文）
- **Unified Interface / 统一界面**: All game elements display in your chosen language / 所有游戏元素使用您选择的语言显示
- **No Mixed Text / 无混合文本**: Clean, professional single-language experience / 清洁、专业的单语体验
- **Pattern Localization / 棋谱本地化**: Pattern names, descriptions, and analysis in your language / 棋谱名称、描述和分析使用您的语言
- **Smart Hints / 智能提示**: Error messages and area hints in your preferred language / 错误消息和区域提示使用您的首选语言

## Main Features / 主要特点

- **🌍 Language Selection / 语言选择**: Choose English or Chinese at startup for complete localization / 启动时选择英文或中文，享受完整本地化
- **🎯 Endgame Training / 残局训练**: Player uses white stones to solve classic endgame positions / 玩家执白子解决经典残局局面  
- **📚 Localized Patterns / 本地化棋谱**: Pattern content dynamically translated to your chosen language / 棋谱内容动态翻译为您选择的语言
- **🤖 Computer Setup / 电脑布局**: Computer uses black stones to set up endgame positions according to patterns / 电脑执黑子按棋谱布局残局
- **🎯 Intelligent Move Validation / 智能走法验证**: Real-time validation of whether player moves solve the endgame / 实时验证玩家走法是否解决残局
- **💡 Smart Error Handling / 智能错误处理**: Localized hints and area guidance when moves are incorrect / 走错时提供本地化提示和区域指导
- **📖 Error Tolerance Mechanism / 容错机制**: Allows 3 errors, auto-demonstrates correct moves when exceeded / 允许3次错误，超出后自动演示正确走法
- **🔍 Deep Tactical Analysis / 深度战术解析**: Detailed pattern analysis in your language after completion / 完成后用您的语言显示详细的棋谱分析

## How to Use / 如何使用

### 1. First Launch and Language Selection / 首次启动和语言选择
- Launch the game using any of the methods above / 使用上述任一方法启动游戏
- **Language Selection Dialog / 语言选择对话框** will appear first / 首先出现语言选择对话框
- Choose "English" for complete English interface / 选择"English"获得完整英文界面
- Choose "中文" for complete Chinese interface / 选择"中文"获得完整中文界面
- Your choice will be saved for future launches / 您的选择将被保存供将来启动使用

### 2. Select Pattern / 选择棋谱
- Click "Select Pattern" button (or "选择棋谱" in Chinese) / 点击"Select Pattern"按钮（中文界面为"选择棋谱"）
- Choose from the list the endgame pattern you want to practice / 从列表中选择想要练习的残局棋谱
- Patterns are divided into Beginner, Intermediate, Advanced difficulty levels / 棋谱分为初级、中级、高级三个难度
- All pattern names and descriptions will be in your chosen language / 所有棋谱名称和描述将使用您选择的语言

### 3. Start Training / 开始训练
- You use white stones to find the winning move / 你执白子寻找制胜走法
- Computer has already set up the black stone endgame position / 电脑已经布置好黑子残局局面
- Click board intersections to place white stones / 鼠标点击棋盘交叉点下白子
- Find the correct winning sequence according to the pattern / 根据棋谱找出正确的制胜序列

### 4. Error Handling / 错误处理
- System prompts errors in your language when wrong moves are made / 走错时系统用您的语言提示错误
- Provides localized area hints (e.g., "upper left area" or "棋盘上方左侧区域") / 提供本地化的区域提示
- Maximum 3 error attempts per move / 每步最多允许3次错误尝试
- System auto-demonstrates correct moves after 3 errors / 3次错误后系统自动演示正确走法

### 5. View Analysis / 查看分析
- Right side displays detailed tactical analysis in your language after pattern completion / 棋谱完成后，右侧用您的语言显示详细的战术分析
- Includes strategy, key points, victory principles etc. / 包括策略、关键点、胜利原理等
- All analysis content is fully localized / 所有分析内容完全本地化

## Interface Description / 界面说明

### Left Board Area / 左侧棋盘区
- **Board / 棋盘**: 15x15 standard Gobang board / 15x15标准五子棋棋盘
- **Control Buttons / 控制按钮**:
  - Select Pattern / 选择棋谱: Choose pattern to practice / 选择要练习的棋谱
  - Restart / 重新开始: Reset current pattern / 重置当前棋谱
  - Undo / 悔棋: Withdraw previous move / 撤销上一步
  - Show Answer / 显示答案: Show current correct move / 显示当前正确走法

### Right Information Area / 右侧信息区
- **Pattern Info / 棋谱信息**: Display current pattern name and difficulty / 显示当前棋谱名称和难度
- **Game Status / 游戏状态**: Show whose turn and error count / 显示当前轮到谁下棋和错误次数
- **Step Progress / 步骤进度**: Show current step and total steps / 显示当前步骤和总步骤
- **Hint Info / 提示信息**: Show move validation results and hints / 显示走法验证结果和提示
- **Pattern Analysis / 棋谱分析**: Show tactical analysis after completion / 显示完成后的战术解析

## Built-in Patterns / 内置棋谱

### 1. Classic Opening - Tian Yuan (Beginner) / 经典开局-天元开局 (初级)
- Most basic Gobang opening / 最基础的五子棋开局
- Learn center control and basic offense-defense / 学习中心控制和基本攻防
- Suitable for beginners to practice / 适合初学者练习

### 2. Classic Opening - Hua Yue (Intermediate) / 经典开局-花月局 (中级)  
- Relatively complex offense-defense transitions / 较为复杂的攻防转换
- Learn creation of multiple threats / 学习多重威胁的创造
- Suitable for players with some foundation / 适合有一定基础的玩家

### 3. Classic Opening - Pu Yue (Advanced) / 经典开局-浦月局 (高级)
- Advanced tactics and precise calculations / 高级战术和精密计算
- Breakthrough techniques in complex situations / 复杂局面下的突破技巧
- Suitable for advanced players to challenge / 适合进阶玩家挑战

## Learning Suggestions / 学习建议

1. **Step by Step / 循序渐进**: Start from beginner patterns, gradually increase difficulty / 从初级棋谱开始，逐步提高难度
2. **Repeated Practice / 反复练习**: Same pattern can be practiced multiple times to deepen understanding / 同一个棋谱可以多次练习，加深理解
3. **Carefully Read Analysis / 仔细阅读分析**: Carefully read tactical analysis after completion to understand each move's intention / 完成后认真阅读战术分析，理解每步的意图
4. **Summarize Patterns / 总结规律**: After practicing multiple patterns, summarize common offense-defense patterns / 练习多个棋谱后，总结常见的攻防模式

## Technical Implementation / 技术实现

- **Programming Language / 编程语言**: Python 3.7+
- **GUI Framework / GUI框架**: tkinter (Python built-in / Python内置)
- **Core Algorithm / 核心算法**: numpy array processing / numpy数组处理
- **Design Pattern / 设计模式**: Modular design, easy to extend / 模块化设计，便于扩展

## System Requirements / 系统要求

- Python 3.7 or higher / Python 3.7 或更高版本
- numpy library / numpy 库
- tkinter (Python standard library / Python标准库)

## Troubleshooting / 故障排除

### 1. Game Won't Start / 游戏无法启动
- Check if Python version meets requirements / 检查Python版本是否符合要求
- Confirm numpy is installed: `pip install numpy` / 确认已安装numpy：`pip install numpy`
- Check if file path is correct / 检查文件路径是否正确

### 2. Pattern Display Abnormal / 棋谱显示异常
- Restart the game / 重新启动游戏
- Check if pattern files are complete / 检查棋谱文件是否完整

### 3. Interface Display Issues / 界面显示问题
- Confirm tkinter library works normally / 确认tkinter库正常工作
- Try adjusting system display scaling ratio / 尝试调整系统显示缩放比例

## Contact Author / 联系作者

- Author / 作者：Xu Huicong
- Project / 项目：Gobang Pattern Battle System / 五子棋棋谱对战系统
- Version / 版本：1.0.0

Thank you for using this system! Hope it helps improve your Gobang skills! / 感谢使用本系统！希望能帮助你提高五子棋水平！