# 测试目录

这个目录包含项目的所有测试文件。

## 测试结构

```
tests/
├── __init__.py          # 使此目录成为Python包
├── test_game.py         # 游戏核心逻辑测试
├── test_board.py        # 棋盘功能测试
├── test_player.py       # 玩家类测试
└── test_ai.py           # AI算法测试（如果有）
```

## 运行测试

在项目根目录运行：

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_game.py

# 运行测试并显示覆盖率
pytest --cov=game --cov=gui

# 详细输出
pytest -v
```

## 编写测试

请确保为新功能编写相应的测试用例，并保持测试覆盖率。