# Gobang Pattern Battle System User Guide / 五子棋棋谱对战系统使用说明

## Game Introduction / 游戏简介

This is a player vs computer Gobang battle system. Players use black stones, computer uses white stones, strictly following classic patterns for battles. Through real battle experience, help players master classic Gobang tactics and opening strategies.

这是一个玩家vs电脑的五子棋对战系统。玩家执黑子，电脑执白子，严格按照经典棋谱进行对战。通过真实的对战体验，帮助玩家掌握五子棋的经典战术和开局技巧。

## Main Features / 主要特点

- **Real Battle Experience / 真实对战体验**: Player uses black stones vs computer uses white stones for turn-based battle / 玩家执黑子vs电脑执白子，真实的回合制对战
- **Classic Pattern Battle / 经典棋谱对战**: Based on classic Gobang patterns of multiple difficulty levels / 基于多个难度级别的经典五子棋棋谱
- **Intelligent Move Validation / 智能走法验证**: Real-time validation of whether player moves comply with patterns / 实时验证玩家走法是否符合棋谱
- **Computer Auto Response / 电脑自动应战**: Computer strictly follows patterns for responses, never makes mistakes / 电脑严格按照棋谱进行回应，不会出错
- **Error Tolerance Mechanism / 容错机制**: Allows 3 errors, auto-demonstrates correct moves when exceeded / 允许3次错误，超出后自动演示正确走法
- **Deep Tactical Analysis / 深度战术解析**: Detailed pattern analysis displayed after battle completion / 对战完成后显示详细的棋谱分析

## How to Use / 如何使用

### 1. Start Game / 启动游戏
Run `python main.py` to start the game window / 运行 `python main.py` 启动游戏窗口

### 2. Select Pattern / 选择棋谱
- Click "Select Pattern" button / 点击"选择棋谱"按钮
- Choose from the list the pattern you want to practice / 从列表中选择想要练习的棋谱
- Patterns are divided into Beginner, Intermediate, Advanced difficulty levels / 棋谱分为初级、中级、高级三个难度

### 3. Start Battle / 开始对战
- You use black stones, computer uses white stones / 你执黑子，电脑执白子
- Click board intersections to place black stones / 鼠标点击棋盘交叉点下黑子
- Computer will immediately respond with white stones according to pattern / 电脑会立即按照棋谱进行白子回应
- Continue turn-based battle until pattern ends / 继续轮流对战直到棋谱结束

### 4. Error Handling / 错误处理
- System prompts errors and gives position hints when wrong moves are made / 走错时系统提示错误并给出位置提示
- Maximum 3 error attempts per move / 每步最多允许3次错误尝试
- System auto-demonstrates correct moves after 3 errors and continues battle / 3次错误后系统自动演示正确走法并继续对战

### 5. View Analysis / 查看分析
- Right side displays detailed tactical analysis after pattern completion / 棋谱完成后，右侧会显示详细的战术分析
- Includes opening ideas, key steps, victory principles etc. / 包括开局思路、关键步骤、胜利原理等

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