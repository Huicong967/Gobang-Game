#!/usr/bin/env python3
"""
测试走法验证器的双语功能
Test MoveValidator bilingual functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from game.board import Board
from game.pattern import PatternManager
from game.validator import MoveValidator

class MockLanguageManager:
    """模拟语言管理器"""
    def __init__(self, language='english'):
        self.current_language = language
        self.translations = {
            'english': {
                'computer_turn_wait': "Computer's turn, please wait...",
                'pattern_completed': 'Pattern completed!',
                'correct_move': 'Correct move!',
                'correct_move_computer_thinking': 'Correct move! Computer thinking...',
                'wrong_max_times': 'Wrong {} times, correct move is:',
                'wrong_move_chances_left': 'Wrong move! {} chances left. Hint:',
                'area_upper': 'upper',
                'area_middle': 'middle',
                'area_lower': 'lower',
                'area_left': 'left',
                'area_center': 'center',
                'area_right': 'right',
                'area_hint': '{} {} area',
                'its_player_turn': "It's player's turn!",
                'computer_moved_your_turn': 'Computer moved, your turn!',
                'computer_move_failed': 'Computer move failed!'
            },
            'chinese': {
                'computer_turn_wait': '现在轮到电脑下棋，请等待...',
                'pattern_completed': '棋谱已完成！',
                'correct_move': '走法正确！',
                'correct_move_computer_thinking': '走法正确！电脑思考中...',
                'wrong_max_times': '已错误{}次，正确走法是：',
                'wrong_move_chances_left': '走法错误！还有{}次机会。提示：',
                'area_upper': '上方',
                'area_middle': '中间',
                'area_lower': '下方',
                'area_left': '左侧',
                'area_center': '中间',
                'area_right': '右侧',
                'area_hint': '棋盘{}{}区域',
                'its_player_turn': '现在轮到玩家下棋！',
                'computer_moved_your_turn': '电脑已下棋，轮到你了！',
                'computer_move_failed': '电脑下棋失败！'
            }
        }
    
    def get_text(self, key, *args):
        """获取翻译文本"""
        text = self.translations[self.current_language].get(key, key)
        if args:
            return text.format(*args)
        return text
    
    def set_language(self, language):
        """设置语言"""
        self.current_language = language

def test_validator_bilingual():
    """测试验证器双语功能"""
    print("=" * 60)
    print("🎯 验证器双语功能测试 / Validator Bilingual Test")
    print("=" * 60)
    
    # 创建组件
    board = Board()
    pattern_manager = PatternManager()
    language_manager = MockLanguageManager()
    
    # 测试英文模式
    print("\n📝 English Mode:")
    print("-" * 40)
    language_manager.set_language('english')
    validator = MoveValidator(pattern_manager, board, language_manager)
    
    # 加载一个棋谱进行测试
    if pattern_manager.load_pattern('one_move_1'):
        validator.initialize_player_colors()
        
        # 测试错误走法提示
        result = validator.validate_player_move(0, 0)  # 随便一个错误位置
        print(f"Error message: {result['message']}")
        
        # 再次错误
        result = validator.validate_player_move(0, 1)
        print(f"Second error: {result['message']}")
        
        # 第三次错误
        result = validator.validate_player_move(0, 2)
        print(f"Max errors: {result['message']}")
    
    # 测试中文模式
    print("\n📝 Chinese Mode:")
    print("-" * 40)
    language_manager.set_language('chinese')
    validator = MoveValidator(pattern_manager, board, language_manager)
    
    # 重新加载棋谱
    if pattern_manager.load_pattern('one_move_1'):
        validator.initialize_player_colors()
        
        # 测试错误走法提示
        result = validator.validate_player_move(0, 0)  # 随便一个错误位置
        print(f"错误消息: {result['message']}")
        
        # 再次错误
        result = validator.validate_player_move(0, 1)
        print(f"第二次错误: {result['message']}")
        
        # 第三次错误
        result = validator.validate_player_move(0, 2)
        print(f"达到最大错误次数: {result['message']}")
    
    print("\n" + "=" * 60)
    print("✅ 验证器双语测试完成！Validator bilingual test completed!")
    print("=" * 60)

def test_hint_messages():
    """测试提示消息的双语功能"""
    print("\n🔍 测试区域提示双语功能 / Testing area hint bilingual functionality")
    print("-" * 60)
    
    board = Board(size=15)
    pattern_manager = PatternManager()
    language_manager = MockLanguageManager()
    
    # 英文提示
    print("English hints:")
    language_manager.set_language('english')
    validator = MoveValidator(pattern_manager, board, language_manager)
    
    test_positions = [
        (2, 2),   # upper left
        (7, 7),   # middle center  
        (12, 12), # lower right
        (2, 12),  # upper right
        (12, 2)   # lower left
    ]
    
    for row, col in test_positions:
        hint = validator._get_hint(row, col)
        print(f"  Position ({row}, {col}): {hint}")
    
    # 中文提示
    print("\nChinese hints:")
    language_manager.set_language('chinese')
    validator = MoveValidator(pattern_manager, board, language_manager)
    
    for row, col in test_positions:
        hint = validator._get_hint(row, col)
        print(f"  位置 ({row}, {col}): {hint}")

if __name__ == "__main__":
    test_validator_bilingual()
    test_hint_messages()