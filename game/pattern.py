"""
Pattern Manager
棋谱管理器
Handle pattern loading, parsing and management
处理棋谱的加载、解析和管理
"""

import json
import os
from typing import List, Dict, Tuple, Optional


class PatternManager:
    """棋谱管理器"""
    
    def __init__(self, patterns_dir="patterns"):
        """
        初始化棋谱管理器
        
        Args:
            patterns_dir (str): 棋谱文件目录
        """
        self.patterns_dir = patterns_dir
        self.current_pattern = None
        self.current_step = 0
        self.patterns_list = []
        self._load_patterns_list()
    
    def _load_patterns_list(self):
        """加载可用的棋谱列表"""
        self.patterns_list = []
        
        # 添加内置棋谱
        built_in_patterns = [
            {
                "id": "classic_1",
                "name": "Classic Opening - Tian Yuan / 经典开局-天元开局",
                "difficulty": "Beginner / 初级",
                "description": "Most classic Tian Yuan opening pattern, learn basic offense and defense / 最经典的天元开局棋谱，学习基础攻防"
            },
            {
                "id": "classic_2", 
                "name": "Classic Opening - Hua Yue / 经典开局-花月局",
                "difficulty": "Intermediate / 中级",
                "description": "Classic Hua Yue play, learn complex offense-defense transitions / 花月局的经典下法，学习复杂攻防转换"
            },
            {
                "id": "classic_3",
                "name": "Classic Opening - Pu Yue / 经典开局-浦月局",
                "difficulty": "Advanced / 高级",
                "description": "Exquisite Pu Yue variations, learn advanced tactics / 浦月局的精妙变化，学习高级战术"
            }
        ]
        
        self.patterns_list.extend(built_in_patterns)
    
    def get_patterns_list(self):
        """
        获取棋谱列表
        
        Returns:
            list: 棋谱信息列表
        """
        return self.patterns_list
    
    def load_pattern(self, pattern_id):
        """
        加载指定棋谱
        
        Args:
            pattern_id (str): 棋谱ID
            
        Returns:
            bool: 是否加载成功
        """
        try:
            # 这里使用内置的示例棋谱数据
            patterns_data = self._get_built_in_patterns()
            
            if pattern_id in patterns_data:
                self.current_pattern = patterns_data[pattern_id]
                self.current_step = 0
                return True
            else:
                return False
        except Exception as e:
            print(f"加载棋谱失败: {e}")
            return False
    
    def _get_built_in_patterns(self):
        """获取内置棋谱数据"""
        return {
            "classic_1": {
                "id": "classic_1",
                "name": "经典开局-天元开局",
                "difficulty": "初级",
                "description": "最经典的天元开局棋谱，学习基础攻防",
                "moves": [
                    (7, 7, 1),   # 黑子天元
                    (6, 6, 2),   # 白子
                    (8, 8, 1),   # 黑子
                    (6, 8, 2),   # 白子
                    (5, 9, 1),   # 黑子
                    (7, 9, 2),   # 白子
                    (4, 10, 1),  # 黑子
                    (8, 10, 2),  # 白子
                    (3, 11, 1),  # 黑子胜
                ],
                "analysis": {
                    "opening": "天元开局是五子棋的经典开局之一，黑子占据中心位置。",
                    "strategy": "黑子通过天元开局控制中心，然后向右下方发展攻势。",
                    "key_points": [
                        "第1手：天元开局，控制全局中心",
                        "第3手：斜线发展，保持攻势",
                        "第5手：继续斜线攻击，形成威胁",
                        "第7手：扩大攻击范围",
                        "第9手：完成五连，取得胜利"
                    ],
                    "win_reason": "黑子通过连续的斜线攻击，在白子无法有效防守的情况下完成五连胜利。"
                }
            },
            "classic_2": {
                "id": "classic_2",
                "name": "经典开局-花月局",
                "difficulty": "中级", 
                "description": "花月局的经典下法，学习复杂攻防转换",
                "moves": [
                    (7, 7, 1),   # 黑子天元
                    (7, 8, 2),   # 白子
                    (6, 7, 1),   # 黑子
                    (8, 7, 2),   # 白子
                    (6, 8, 1),   # 黑子
                    (8, 8, 2),   # 白子
                    (5, 9, 1),   # 黑子
                    (9, 6, 2),   # 白子
                    (4, 10, 1),  # 黑子
                    (6, 9, 2),   # 白子
                    (3, 11, 1),  # 黑子胜
                ],
                "analysis": {
                    "opening": "花月局是较为复杂的开局，需要精确的计算。",
                    "strategy": "黑子需要在白子的干扰下寻找突破口，形成多重威胁。",
                    "key_points": [
                        "第1手：天元开局",
                        "第3-5手：形成局部优势",
                        "第7手：转换攻击方向",
                        "第9手：创造决定性威胁",
                        "第11手：完成胜利"
                    ],
                    "win_reason": "通过巧妙的攻防转换和多重威胁，最终找到致胜一击。"
                }
            },
            "classic_3": {
                "id": "classic_3",
                "name": "经典开局-浦月局", 
                "difficulty": "高级",
                "description": "浦月局的精妙变化，学习高级战术",
                "moves": [
                    (7, 7, 1),   # 黑子天元
                    (6, 7, 2),   # 白子
                    (8, 7, 1),   # 黑子
                    (7, 6, 2),   # 白子  
                    (7, 8, 1),   # 黑子
                    (6, 8, 2),   # 白子
                    (8, 6, 1),   # 黑子
                    (8, 8, 2),   # 白子
                    (5, 7, 1),   # 黑子
                    (9, 7, 2),   # 白子
                    (4, 7, 1),   # 黑子胜
                ],
                "analysis": {
                    "opening": "浦月局是高级开局，变化复杂，需要深度计算。",
                    "strategy": "黑子通过精密的布局，在看似平衡的局面下寻找突破。",
                    "key_points": [
                        "第1手：天元开局",
                        "第3-7手：形成复杂局面",
                        "第9手：关键突破",
                        "第11手：完成五连"
                    ],
                    "win_reason": "在复杂的攻防中，黑子通过精确计算找到了唯一的获胜路径。"
                }
            }
        }
    
    def get_current_move(self):
        """
        获取当前步骤的走法
        
        Returns:
            tuple: (row, col, player) 或 None
        """
        if not self.current_pattern or self.current_step >= len(self.current_pattern["moves"]):
            return None
        
        return self.current_pattern["moves"][self.current_step]
    
    def get_next_move(self):
        """
        获取下一步的走法（不移动步骤指针）
        
        Returns:
            tuple: (row, col, player) 或 None
        """
        if not self.current_pattern or (self.current_step + 1) >= len(self.current_pattern["moves"]):
            return None
            
        return self.current_pattern["moves"][self.current_step + 1]
    
    def advance_step(self):
        """推进到下一步"""
        if self.current_pattern and self.current_step < len(self.current_pattern["moves"]):
            self.current_step += 1
    
    def is_pattern_complete(self):
        """
        检查棋谱是否已完成
        
        Returns:
            bool: 棋谱是否完成
        """
        if not self.current_pattern:
            return True
        return self.current_step >= len(self.current_pattern["moves"])
    
    def get_pattern_analysis(self):
        """
        获取当前棋谱的分析
        
        Returns:
            dict: 棋谱分析信息
        """
        if not self.current_pattern:
            return None
        return self.current_pattern.get("analysis", {})
    
    def get_pattern_info(self):
        """
        获取当前棋谱的基本信息
        
        Returns:
            dict: 棋谱信息
        """
        if not self.current_pattern:
            return None
        
        return {
            "id": self.current_pattern["id"],
            "name": self.current_pattern["name"],
            "difficulty": self.current_pattern["difficulty"],
            "description": self.current_pattern["description"],
            "total_moves": len(self.current_pattern["moves"]),
            "current_step": self.current_step
        }
    
    def reset_pattern(self):
        """重置棋谱到开始状态"""
        self.current_step = 0