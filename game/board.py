"""
Gobang Board Class
五子棋棋盘类
Handle board state, piece placement, win/loss judgment and other basic functions
处理棋盘状态、落子、胜负判断等基础功能
"""

import numpy as np


class Board:
    """Gobang Board Class / 五子棋棋盘类"""
    
    def __init__(self, size=15):
        """
        Initialize board / 初始化棋盘
        
        Args:
            size (int): Board size, default 15x15 / 棋盘大小，默认15x15
        """
        self.size = size
        self.board = np.zeros((size, size), dtype=int)  # 0=空, 1=黑子, 2=白子
        self.move_history = []  # 记录走棋历史
        
    def is_valid_move(self, row, col):
        """
        检查落子位置是否有效
        
        Args:
            row (int): 行位置
            col (int): 列位置
            
        Returns:
            bool: 是否可以落子
        """
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False
        return self.board[row, col] == 0
    
    def make_move(self, row, col, player):
        """
        落子
        
        Args:
            row (int): 行位置
            col (int): 列位置
            player (int): 玩家 (1=黑子, 2=白子)
            
        Returns:
            bool: 是否成功落子
        """
        if not self.is_valid_move(row, col):
            return False
            
        self.board[row, col] = player
        self.move_history.append((row, col, player))
        return True
    
    def undo_move(self):
        """
        悔棋 - 撤销最后一步
        
        Returns:
            tuple: 撤销的走法 (row, col, player) 或 None
        """
        if not self.move_history:
            return None
            
        last_move = self.move_history.pop()
        row, col, player = last_move
        self.board[row, col] = 0
        return last_move
    
    def check_winner(self, row, col, player):
        """
        检查是否有玩家获胜
        
        Args:
            row (int): 最后落子的行
            col (int): 最后落子的列
            player (int): 落子的玩家
            
        Returns:
            bool: 该玩家是否获胜
        """
        directions = [
            (0, 1),   # 水平
            (1, 0),   # 垂直
            (1, 1),   # 主对角线
            (1, -1)   # 反对角线
        ]
        
        for dr, dc in directions:
            count = 1  # 包含当前落子
            
            # 正方向检查
            r, c = row + dr, col + dc
            while (0 <= r < self.size and 0 <= c < self.size and 
                   self.board[r, c] == player):
                count += 1
                r += dr
                c += dc
            
            # 反方向检查
            r, c = row - dr, col - dc
            while (0 <= r < self.size and 0 <= c < self.size and 
                   self.board[r, c] == player):
                count += 1
                r -= dr
                c -= dc
            
            if count >= 5:
                return True
        
        return False
    
    def get_board_state(self):
        """
        获取当前棋盘状态
        
        Returns:
            numpy.ndarray: 棋盘状态副本
        """
        return self.board.copy()
    
    def reset(self):
        """重置棋盘"""
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.move_history = []
    
    def is_full(self):
        """
        检查棋盘是否已满
        
        Returns:
            bool: 棋盘是否已满
        """
        return np.all(self.board != 0)
    
    def get_empty_positions(self):
        """
        获取所有空位置
        
        Returns:
            list: 空位置列表 [(row, col), ...]
        """
        empty_positions = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row, col] == 0:
                    empty_positions.append((row, col))
        return empty_positions