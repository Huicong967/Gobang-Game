"""
走法验证器
验证玩家的走法是否符合棋谱要求
"""

from typing import Tuple, Optional


class MoveValidator:
    """走法验证器"""
    
    def __init__(self, pattern_manager, board):
        """
        初始化验证器
        
        Args:
            pattern_manager: 棋谱管理器
            board: 棋盘对象
        """
        self.pattern_manager = pattern_manager
        self.board = board
        self.error_count = 0
        self.max_errors = 3
        self.last_error_move = None
    
    def validate_move(self, row, col, player):
        """
        验证玩家走法
        
        Args:
            row (int): 行位置
            col (int): 列位置  
            player (int): 玩家 (1=黑子, 2=白子)
            
        Returns:
            dict: 验证结果 {
                'valid': bool,           # 是否正确
                'message': str,          # 提示信息
                'correct_move': tuple,   # 正确走法 (row, col, player)
                'show_answer': bool,     # 是否显示答案
                'pattern_complete': bool # 棋谱是否完成
            }
        """
        expected_move = self.pattern_manager.get_current_move()
        
        if not expected_move:
            return {
                'valid': False,
                'message': '棋谱已完成！',
                'correct_move': None,
                'show_answer': False,
                'pattern_complete': True
            }
        
        expected_row, expected_col, expected_player = expected_move
        
        # 检查是否与期望走法匹配
        if (row == expected_row and col == expected_col and 
            player == expected_player):
            # 走法正确
            self.error_count = 0  # 重置错误计数
            self.last_error_move = None
            self.pattern_manager.advance_step()
            
            # 检查棋谱是否完成
            pattern_complete = self.pattern_manager.is_pattern_complete()
            
            if pattern_complete:
                return {
                    'valid': True,
                    'message': '恭喜！棋谱练习完成！',
                    'correct_move': expected_move,
                    'show_answer': False,
                    'pattern_complete': True
                }
            else:
                return {
                    'valid': True,
                    'message': '走法正确！继续加油！',
                    'correct_move': expected_move,
                    'show_answer': False,
                    'pattern_complete': False
                }
        else:
            # 走法错误
            self.error_count += 1
            self.last_error_move = (row, col, player)
            
            if self.error_count >= self.max_errors:
                # 达到最大错误次数，显示正确答案
                return {
                    'valid': False,
                    'message': f'已错误{self.max_errors}次，正确走法是：{self._format_position(expected_row, expected_col)}',
                    'correct_move': expected_move,
                    'show_answer': True,
                    'pattern_complete': False
                }
            else:
                # 还有重试机会
                return {
                    'valid': False,
                    'message': f'走法错误！还有{self.max_errors - self.error_count}次机会。正确位置在：{self._get_hint(expected_row, expected_col)}',
                    'correct_move': expected_move,
                    'show_answer': False,
                    'pattern_complete': False
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
        row_region = ""
        if expected_row < board_size // 3:
            row_region = "上方"
        elif expected_row < 2 * board_size // 3:
            row_region = "中间"
        else:
            row_region = "下方"
            
        col_region = ""
        if expected_col < board_size // 3:
            col_region = "左侧"
        elif expected_col < 2 * board_size // 3:
            col_region = "中间"
        else:
            col_region = "右侧"
        
        return f"棋盘{row_region}{col_region}区域"
    
    def auto_make_move(self):
        """
        自动执行当前步骤的正确走法
        
        Returns:
            tuple: (row, col, player) 或 None
        """
        expected_move = self.pattern_manager.get_current_move()
        
        if expected_move:
            row, col, player = expected_move
            if self.board.make_move(row, col, player):
                self.pattern_manager.advance_step()
                self.error_count = 0  # 重置错误计数
                return expected_move
        
        return None
    
    def reset_errors(self):
        """重置错误计数"""
        self.error_count = 0
        self.last_error_move = None
    
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
    
    def get_current_player(self):
        """
        获取当前应该下棋的玩家
        
        Returns:
            int: 当前玩家 (1=黑子, 2=白子) 或 None
        """
        expected_move = self.pattern_manager.get_current_move()
        if expected_move:
            return expected_move[2]
        return None