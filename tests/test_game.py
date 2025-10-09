"""
游戏核心功能测试
"""

import sys
import os

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game import Board, PatternManager, MoveValidator


class TestGameBasics:
    """游戏基础功能测试"""

    def test_board_initialization(self):
        """测试棋盘初始化"""
        board = Board()
        assert board.size == 15
        assert board.board.shape == (15, 15)
        assert len(board.move_history) == 0

    def test_valid_move(self):
        """测试有效走法"""
        board = Board()
        assert board.is_valid_move(7, 7) == True
        assert board.is_valid_move(-1, 0) == False
        assert board.is_valid_move(15, 15) == False

    def test_make_move(self):
        """测试落子"""
        board = Board()
        assert board.make_move(7, 7, 1) == True
        assert board.board[7, 7] == 1
        assert len(board.move_history) == 1
        assert board.make_move(7, 7, 2) == False  # 位置已占用

    def test_undo_move(self):
        """测试悔棋"""
        board = Board()
        board.make_move(7, 7, 1)
        last_move = board.undo_move()
        assert last_move == (7, 7, 1)
        assert board.board[7, 7] == 0
        assert len(board.move_history) == 0

    def test_pattern_manager(self):
        """测试棋谱管理器"""
        pm = PatternManager()
        patterns = pm.get_patterns_list()
        assert len(patterns) > 0
        
        # 测试加载棋谱
        assert pm.load_pattern("classic_1") == True
        assert pm.current_pattern is not None
        
        # 测试获取当前走法
        move = pm.get_current_move()
        assert move == (7, 7, 1)  # 第一步应该是天元

    def test_move_validator(self):
        """测试走法验证器"""
        board = Board()
        pm = PatternManager()
        pm.load_pattern("classic_1")
        validator = MoveValidator(pm, board)
        
        # 测试正确走法
        result = validator.validate_move(7, 7, 1)
        assert result['valid'] == True
        
        # 测试错误走法
        result = validator.validate_move(0, 0, 1)
        assert result['valid'] == False

    def test_win_condition(self):
        """测试胜利条件检查"""
        board = Board()
        # 创建一个五连的情况
        for i in range(5):
            board.make_move(i, i, 1)
        
        # 检查最后一步是否导致胜利
        assert board.check_winner(4, 4, 1) == True


if __name__ == "__main__":
    # 简单的测试运行器
    import traceback
    
    test_instance = TestGameBasics()
    tests = [
        test_instance.test_board_initialization,
        test_instance.test_valid_move,
        test_instance.test_make_move,
        test_instance.test_undo_move,
        test_instance.test_pattern_manager,
        test_instance.test_move_validator,
        test_instance.test_win_condition,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            print(f"✓ {test.__name__}")
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: {e}")
            traceback.print_exc()
            failed += 1
    
    print(f"\n测试结果：通过 {passed} 个，失败 {failed} 个")