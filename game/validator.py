"""
Move Validator
走法验证器
Validate if player moves comply with pattern requirements, support player vs computer battle mode
验证玩家的走法是否符合棋谱要求，支持玩家vs电脑对战模式
"""

from typing import Tuple, Optional


class MoveValidator:
    """走法验证器 - 残局训练模式（玩家固定执行一种颜色）"""
    
    def __init__(self, pattern_manager, board, language_manager=None):
        """
        初始化验证器
        
        Args:
            pattern_manager: 棋谱管理器
            board: 棋盘对象
            language_manager: 语言管理器
        """
        self.pattern_manager = pattern_manager
        self.board = board
        self.language_manager = language_manager
        self.error_count = 0
        self.max_errors = 3
        self.last_error_move = None
        self.player_color = None  # 玩家固定执行的颜色 (1=黑子, 2=白子)
        self.computer_color = None  # 电脑固定执行的颜色
        self.is_player_turn = True  # 当前是否轮到玩家
    
    def _get_text(self, key, *args):
        """获取翻译文本"""
        if self.language_manager and hasattr(self.language_manager, 'get_text'):
            return self.language_manager.get_text(key, *args)
        else:
            # 如果没有语言管理器，返回默认英文
            default_texts = {
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
            }
            text = default_texts.get(key, key)
            if args:
                return text.format(*args)
            return text
    
    def validate_player_move(self, row, col):
        """
        验证玩家走法（玩家在整个残局中固定执行同一种颜色）
        
        Args:
            row (int): 行位置
            col (int): 列位置
            
        Returns:
            dict: 验证结果 {
                'valid': bool,           # 是否正确
                'message': str,          # 提示信息
                'correct_move': tuple,   # 正确走法 (row, col, player)
                'show_answer': bool,     # 是否显示答案
                'pattern_complete': bool,# 棋谱是否完成
                'computer_move': bool    # 是否需要电脑走棋
            }
        """
        # 检查当前是否轮到玩家
        if not self.is_player_turn:
            return {
                'valid': False,
                'message': self._get_text('computer_turn_wait'),
                'correct_move': None,
                'show_answer': False,
                'pattern_complete': False,
                'computer_move': False
            }
        
        # 获取当前应该下的步骤
        expected_move = self.pattern_manager.get_current_move()
        if not expected_move:
            return {
                'valid': False,
                'message': self._get_text('pattern_completed'),
                'correct_move': None,
                'show_answer': False,
                'pattern_complete': True,
                'computer_move': False
            }
        
        expected_row, expected_col, expected_color = expected_move
        
        # 确保这一步应该是玩家的颜色
        if expected_color != self.player_color:
            return {
                'valid': False,
                'message': self._get_text('computer_turn_wait'),
                'correct_move': None,
                'show_answer': False,
                'pattern_complete': False,
                'computer_move': False
            }
        
        # 检查玩家走法是否正确
        if row == expected_row and col == expected_col:
            # 走法正确
            self.error_count = 0  # 重置错误计数
            self.last_error_move = None
            self.pattern_manager.advance_step()
            
            # 切换到电脑回合
            self.is_player_turn = False
            
            # 检查棋谱是否完成
            pattern_complete = self.pattern_manager.is_pattern_complete()
            
            return {
                'valid': True,
                'message': self._get_text('correct_move') if pattern_complete else self._get_text('correct_move_computer_thinking'),
                'correct_move': expected_move,
                'show_answer': False,
                'pattern_complete': pattern_complete,
                'computer_move': not pattern_complete  # 如果未完成则需要电脑走棋
            }
        else:
            # 走法错误
            self.error_count += 1
            self.last_error_move = (row, col, self.player_color)
            
            if self.error_count >= self.max_errors:
                # 达到最大错误次数，显示正确答案
                return {
                    'valid': False,
                    'message': f'{self._get_text("wrong_max_times", self.max_errors)} {self._format_position(expected_row, expected_col)}',
                    'correct_move': expected_move,
                    'show_answer': True,
                    'pattern_complete': False,
                    'computer_move': False
                }
            else:
                # 还有重试机会
                return {
                    'valid': False,
                    'message': f'{self._get_text("wrong_move_chances_left", self.max_errors - self.error_count)} {self._get_hint(expected_row, expected_col)}',
                    'correct_move': expected_move,
                    'show_answer': False,
                    'pattern_complete': False,
                    'computer_move': False
                }
    
    def _format_position(self, row, col):
        """
        格式化位置信息
        
        Args:
            row (int): 行
            col (int): 列
            
        Returns:
            str: 格式化的位置
        """
        # 将数字坐标转换为更友好的表示
        col_letter = chr(ord('A') + col)
        row_number = row + 1
        return f"{col_letter}{row_number} ({row}, {col})"
    
    def _get_hint(self, expected_row, expected_col):
        """
        获取位置提示
        
        Args:
            expected_row (int): 期望的行
            expected_col (int): 期望的列
            
        Returns:
            str: 提示信息
        """
        # 根据棋盘区域给出提示
        board_size = self.board.size
        
        # 确定区域
        if expected_row < board_size // 3:
            row_region = self._get_text("area_upper")
        elif expected_row < 2 * board_size // 3:
            row_region = self._get_text("area_middle")
        else:
            row_region = self._get_text("area_lower")
            
        if expected_col < board_size // 3:
            col_region = self._get_text("area_left")
        elif expected_col < 2 * board_size // 3:
            col_region = self._get_text("area_center")
        else:
            col_region = self._get_text("area_right")
        
        return self._get_text("area_hint", row_region, col_region)
    
    def make_computer_move(self):
        """
        电脑自动下棋（执行固定颜色）
        
        Returns:
            dict: {
                'move': tuple,           # 电脑走法 (row, col, player)
                'message': str,          # 提示信息
                'pattern_complete': bool # 棋谱是否完成
            }
        """
        # 检查是否轮到电脑
        if self.is_player_turn:
            return {
                'move': None,
                'message': self._get_text('its_player_turn'),
                'pattern_complete': False
            }
            
        expected_move = self.pattern_manager.get_current_move()
        
        if not expected_move:
            return {
                'move': None,
                'message': self._get_text('pattern_completed'),
                'pattern_complete': True
            }
            
        expected_row, expected_col, expected_color = expected_move
        
        # 确保这一步应该是电脑的颜色
        if expected_color != self.computer_color:
            return {
                'move': None,
                'message': self._get_text('its_player_turn'),
                'pattern_complete': False
            }
        
        # 电脑执行走法（使用棋谱中期望的颜色）
        if self.board.make_move(expected_row, expected_col, expected_color):
            self.pattern_manager.advance_step()
            # 切换到玩家回合
            self.is_player_turn = True
            
            # 检查棋谱是否完成
            pattern_complete = self.pattern_manager.is_pattern_complete()
            
            if pattern_complete:
                message = self._get_text('pattern_completed')
            else:
                message = self._get_text('computer_moved_your_turn')
            
            return {
                'move': (expected_row, expected_col, expected_color),
                'message': message,
                'pattern_complete': pattern_complete
            }
        
        return {
            'move': None,
            'message': self._get_text('computer_move_failed'),
            'pattern_complete': False
        }
    
    def auto_make_correct_move(self):
        """
        自动执行当前步骤的正确走法（用于3次错误后的自动演示）
        
        Returns:
            tuple: (row, col, player) 或 None
        """
        expected_move = self.pattern_manager.get_current_move()
        
        if expected_move:
            row, col, expected_color = expected_move
            # 根据期望颜色决定使用哪个玩家的颜色
            actual_color = expected_color  # 保持原有的颜色
            if self.board.make_move(row, col, actual_color):
                self.pattern_manager.advance_step()
                self.error_count = 0  # 重置错误计数
                
                # 正确处理回合切换：如果刚才是玩家的走法，现在轮到电脑；反之亦然
                if expected_color == self.player_color:
                    # 刚才是玩家走法，现在轮到电脑
                    self.is_player_turn = False
                else:
                    # 刚才是电脑走法，现在轮到玩家
                    self.is_player_turn = True
                    
                return (row, col, actual_color)
        
        return None
    
    def reset_errors(self):
        """重置错误计数"""
        self.error_count = 0
        self.last_error_move = None
    
    def initialize_player_colors(self):
        """初始化玩家和电脑的固定颜色"""
        # 根据棋谱设计：玩家执白子（2），电脑执黑子（1）
        self.player_color = 2  # 白子
        self.computer_color = 1  # 黑子
        
        if self.pattern_manager.current_pattern:
            first_move = self.pattern_manager.get_current_move()
            if first_move:
                first_color = first_move[2]
                # 判断第一手是玩家还是电脑
                self.is_player_turn = (first_color == self.player_color)
            else:
                # 如果没有走法，默认玩家先手
                self.is_player_turn = True
        else:
            # 默认玩家先手
            self.is_player_turn = True
    
    def reset_game(self):
        """重置游戏状态"""
        self.error_count = 0
        self.last_error_move = None
        # 重新初始化玩家颜色
        self.initialize_player_colors()
    
    def get_error_info(self):
        """
        获取错误信息
        
        Returns:
            dict: 错误信息
        """
        return {
            'error_count': self.error_count,
            'max_errors': self.max_errors,
            'remaining_chances': self.max_errors - self.error_count,
            'last_error_move': self.last_error_move
        }
    

    
    def is_computer_turn(self):
        """
        检查是否轮到电脑
        
        Returns:
            bool: 是否轮到电脑
        """
        # 使用实例属性判断是否轮到电脑
        return not self.is_player_turn