"""
Pattern Manager
棋谱管理器
Handle pattern loading, parsing and management
处理棋谱的加载、解析和管理
"""

import json
import os
from typing import List, Dict, Tuple, Optional


def coord_to_pos(coord_str):
    """将棋谱坐标转换为数组坐标 (如 'H8' -> (7, 7))"""
    if not coord_str or len(coord_str) < 2:
        return None
    
    col_letter = coord_str[0].upper()
    row_number = int(coord_str[1:])
    
    # 列：A=0, B=1, ..., O=14
    col = ord(col_letter) - ord('A')
    # 行：1=0, 2=1, ..., 15=14  
    row = row_number - 1
    
    return (row, col)


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
        
        # 一手胜题目 (1-30)
        for i in range(1, 31):
            self.patterns_list.append({
                "id": f"one_move_{i}",
                "name": f"One Move Victory #{i} / 一手胜 第{i}题",
                "difficulty": "Beginner / 初级",
                "description": f"Find the winning move in one step / 一手制胜第{i}题"
            })
        
        # 两手胜题目 (31-35)  
        for i in range(31, 36):
            self.patterns_list.append({
                "id": f"two_move_{i}",
                "name": f"Two Move Victory #{i} / 两手胜 第{i}题", 
                "difficulty": "Intermediate / 中级",
                "description": f"Find the winning sequence in two moves / 两手制胜第{i}题"
            })
        
        # 三手胜题目 (91-95)
        for i in range(91, 96):
            self.patterns_list.append({
                "id": f"three_move_{i}",
                "name": f"Three Move Victory #{i} / 三手胜 第{i}题",
                "difficulty": "Advanced / 高级", 
                "description": f"Find the winning sequence in three moves / 三手制胜第{i}题"
            })
    
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
        """获取内置残局棋谱数据"""
        patterns = {}
        
        # 一手胜题目 (1-30) - 重新设计，第4手轮到白子制胜
        one_move_data = [
            # 题1: 前3手已下完，第4手白子制胜
            ("one_move_1", [("H8",1), ("I8",2), ("G8",1)], [("F8",2)], 
             "前3手已下完，白子寻找制胜一手", "一手制胜：白子F8完成横向制胜"),
            
            # 题2: 前3手已下完，第4手白子制胜  
            ("one_move_2", [("H6",1), ("H7",2), ("H8",1)], [("H5",2)],
             "前3手已下完，白子寻找制胜一手", "一手制胜：白子H5形成纵向四连威胁获胜"),
             
            # 题3: 前3手已下完，第4手白子制胜
            ("one_move_3", [("G7",1), ("H7",2), ("F7",1)], [("I7",2)],
             "前3手已下完，白子寻找横向突破", "一手制胜：白子I7完成横向制胜"),
             
            # 题4: 前3手已下完，第4手白子制胜
            ("one_move_4", [("H5",1), ("I5",2), ("G5",1)], [("J5",2)],
             "前3手已下完，白子寻找横向制胜", "一手制胜：白子J5完成横向四连获胜"),
             
            # 题5: 前3手已下完，第4手白子制胜
            ("one_move_5", [("G6",1), ("G7",2), ("G8",1)], [("G5",2)],
             "前3手已下完，白子寻找纵向制胜", "一手制胜：白子G5形成纵向四连获胜"),
             
            # 题6-10: 继续添加平衡的题目
            ("one_move_6", [("I7",1), ("H7",2), ("G7",1)], [("F7",2)],
             "前3手已下完，白子横向布局", "一手制胜：白子F7完成横向威胁"),
             
            ("one_move_7", [("H7",1), ("H8",2), ("H9",1)], [("H6",2)],
             "前3手已下完，白子纵向进攻", "一手制胜：白子H6完成纵向制胜"),
             
            ("one_move_8", [("K5",1), ("K6",2), ("K7",1)], [("K4",2)],
             "前3手已下完，白子纵向威胁", "一手制胜：白子K4完成纵向获胜"),
             
            ("one_move_9", [("H4",1), ("I4",2), ("G4",1)], [("F4",2)],
             "前3手已下完，白子横向攻击", "一手制胜：白子F4完成横向连接"),
             
            ("one_move_10", [("G5",1), ("H5",2), ("I5",1)], [("J5",2)],
             "前3手已下完，白子寻找突破", "一手制胜：白子J5完成横向制胜"),
        ]
        
        # 继续添加题11-20 (保持3手初局+1手白子制胜的模式)
        one_move_data.extend([
            ("one_move_11", [("M6",1), ("M7",2), ("M8",1)], [("M5",2)],
             "前3手已下完，白子纵向威胁", "一手制胜：白子M5完成纵向制胜"),
             
            ("one_move_12", [("I12",1), ("H12",2), ("G12",1)], [("F12",2)],
             "前3手已下完，白子横向进攻", "一手制胜：白子F12完成横向突破"),
             
            ("one_move_13", [("G5",1), ("H6",2), ("I7",1)], [("J8",2)],
             "前3手已下完，白子斜向布局", "一手制胜：白子J8完成斜向制胜"),
             
            ("one_move_14", [("K5",1), ("J6",2), ("I7",1)], [("H8",2)],
             "前3手已下完，白子斜向连击", "一手制胜：白子H8完成斜向获胜"),
             
            ("one_move_15", [("L9",1), ("K10",2), ("J11",1)], [("I12",2)],
             "前3手已下完，白子斜向威胁", "一手制胜：白子I12完成斜向制胜"),
             
            ("one_move_16", [("J11",1), ("I10",2), ("H9",1)], [("G8",2)],
             "前3手已下完，白子斜向布局", "一手制胜：白子G8完成斜向连接"),
             
            # 题17-20: 继续白子制胜题目
            ("one_move_17", [("F7",1), ("G7",2), ("H7",1)], [("I7",2)],
             "前3手已下完，白子横向反击", "一手制胜：白子I7完成横向制胜"),
             
            ("one_move_18", [("D9",1), ("D10",2), ("D11",1)], [("D8",2)],
             "前3手已下完，白子纵向威胁", "一手制胜：白子D8完成纵向获胜"),
             
            ("one_move_19", [("K8",1), ("K9",2), ("K10",1)], [("K7",2)],
             "前3手已下完，白子纵向进攻", "一手制胜：白子K7完成纵向制胜"),
             
            ("one_move_20", [("I9",1), ("J9",2), ("K9",1)], [("H9",2)],
             "前3手已下完，白子横向反击", "一手制胜：白子H9完成横向获胜"),
        ])
        
        # 继续添加题21-30 (保持平衡的3手+1手白子制胜模式)  
        one_move_data.extend([
            ("one_move_21", [("J10",1), ("J11",2), ("J12",1)], [("J9",2)],
             "前3手已下完，白子纵向威胁", "一手制胜：白子J9完成纵向制胜"),
             
            ("one_move_22", [("F12",1), ("G12",2), ("H12",1)], [("I12",2)],
             "前3手已下完，白子横向进攻", "一手制胜：白子I12完成横向获胜"),
             
            ("one_move_23", [("J9",1), ("K9",2), ("L9",1)], [("M9",2)],
             "前3手已下完，白子横向布局", "一手制胜：白子M9完成横向突破"),
             
            ("one_move_24", [("E10",1), ("F11",2), ("G12",1)], [("H13",2)],
             "前3手已下完，白子斜向威胁", "一手制胜：白子H13完成斜向制胜"),
             
            ("one_move_25", [("J7",1), ("K8",2), ("L9",1)], [("M10",2)],
             "前3手已下完，白子斜向威胁", "一手制胜：白子M10完成斜向制胜"),
             
            ("one_move_26", [("D7",1), ("E7",2), ("F7",1)], [("G7",2)],
             "前3手已下完，白子横向进攻", "一手制胜：白子G7完成横向获胜"),
             
            ("one_move_27", [("H8",1), ("I9",2), ("J10",1)], [("K11",2)],
             "前3手已下完，白子斜向布局", "一手制胜：白子K11完成斜向制胜"),
             
            ("one_move_28", [("G11",1), ("G10",2), ("G9",1)], [("G8",2)],
             "前3手已下完，白子纵向威胁", "一手制胜：白子G8完成纵向制胜"),
             
            ("one_move_29", [("F8",1), ("G9",2), ("H10",1)], [("I11",2)],
             "前3手已下完，白子斜向进攻", "一手制胜：白子I11完成斜向获胜"),
             
            ("one_move_30", [("C8",1), ("D8",2), ("E8",1)], [("F8",2)],
             "前3手已下完，白子横向布局", "一手制胜：白子F8完成横向制胜"),
        ])
        
        # 处理一手胜题目
        for pattern_id, setup, moves, description, analysis in one_move_data:
            initial_setup = [coord_to_pos(pos) + (player,) for pos, player in setup if coord_to_pos(pos)]
            move_sequence = [coord_to_pos(pos) + (player,) for pos, player in moves if coord_to_pos(pos)]
            
            patterns[pattern_id] = {
                "id": pattern_id,
                "name": pattern_id.replace("_", " ").title(),
                "difficulty": "初级",
                "description": description,
                "initial_setup": initial_setup,
                "moves": move_sequence,
                "analysis": {
                    "opening": description,
                    "strategy": "观察残局局面，找出制胜的关键一手",
                    "key_points": ["分析当前棋型", "寻找突破点", "一手制胜"],
                    "win_reason": analysis
                }
            }
        
        # 两手胜题目 (31-35) - 修正冲突，确保棋子数量和位置正确
        two_move_data = [
            # 题31: 前5手：黑F6,白F7,黑E7,白G7,黑E6 -> 第6手白子开始应对
            ("two_move_31", [("F6",1), ("F7",2), ("E7",1), ("G7",2), ("E6",1)], 
             [("H6",2), ("F5",1), ("G5",2), ("H5",1)], "前5手已下完，白子先应对黑子威胁", 
             "白第6手H6防守，黑第7手F5冲四逼白G5，随即H5形成斜向跳四，白无法同时堵住两个威胁，黑成五。"),
             
            # 题32: 前5手：黑I6,白I7,黑L7,白L8,黑I9 -> 第6手白子开始应对
            ("two_move_32", [("I6",1), ("I7",2), ("L7",1), ("L8",2), ("I9",1)],
             [("H9",2), ("J6",1), ("K9",2), ("L9",1)], "前5手已下完，白子先防守", 
             "白第6手H9防守，黑第7手J6冲四逼白K9挡，随后L9形成跳四，白已无法同时防守两线，黑成五。"),
             
            # 题33: 前5手：黑I6,白I5,黑H5,白J5,黑I4 -> 第6手白子开始应对
            ("two_move_33", [("I6",1), ("I5",2), ("H5",1), ("J5",2), ("I4",1)],
             [("I7",2), ("H6",1), ("G6",2), ("I3",1)], "前5手已下完，白子先防守纵向", 
             "白第6手I7防守，黑第7手H6冲四逼白G6挡，接着I3形成竖向连五威胁，白无法阻止，黑成五。"),
             
            # 题34: 前5手：黑M5,白J5,黑K5,白L5,黑M6 -> 第6手白子开始应对
            ("two_move_34", [("M5",1), ("J5",2), ("K5",1), ("L5",2), ("M6",1)],
             [("M4",2), ("N5",1), ("M7",2), ("I5",1)], "前5手已下完，白子先防守右侧", 
             "白第6手M4防守，黑第7手N5冲四逼白M7挡，随后I5形成横向连五威胁，白缺乏防守点，黑成五。"),
             
            # 题35: 前5手：黑E9,白E10,黑F10,白D10,黑F9 -> 第6手白子开始应对
            ("two_move_35", [("E9",1), ("E10",2), ("F10",1), ("D10",2), ("F9",1)],
             [("G9",2), ("E8",1), ("F8",2), ("E11",1)], "前5手已下完，白子先防守多向威胁", 
             "白第6手G9防守，黑第7手E8冲四逼白F8挡，接着E11形成竖向连五威胁，白无法阻止，黑成五。"),
        ]
        
        for pattern_id, setup, moves, description, analysis in two_move_data:
            initial_setup = [coord_to_pos(pos) + (player,) for pos, player in setup if coord_to_pos(pos)]
            move_sequence = [coord_to_pos(pos) + (player,) for pos, player in moves if coord_to_pos(pos)]
            
            patterns[pattern_id] = {
                "id": pattern_id,
                "name": pattern_id.replace("_", " ").title(),
                "difficulty": "中级",
                "description": description,
                "initial_setup": initial_setup,
                "moves": move_sequence,
                "analysis": {
                    "opening": description,
                    "strategy": "通过连续两手棋的配合，形成冲四战术，迫使对手防守后完成制胜",
                    "key_points": ["观察棋形", "找出冲四点", "计算后续连击", "完成制胜"],
                    "win_reason": analysis
                }
            }        # 三手胜题目 (91-95) - 修正为7手初始局面，更合理的棋子分布
        three_move_data = [
            # 题91: 前7手已下完，第8手白子先应对，第9手黑子开始连续冲四制胜
            ("three_move_91", [("I5",1), ("J5",2), ("K4",1), ("K6",2), ("J6",1), ("I6",2), ("H5",1)],
             [("H6",2), ("L5",1), ("J4",2), ("L4",1), ("L6",2), ("L3",1)], "前7手已下完，白子先应对威胁", 
             "白第8手H6防守，黑第9手L5冲四逼白J4挡，接着L4再次冲四逼白L6，最后L3形成连五，白无法阻止。"),
             
            # 题92: 前7手已下完，第8手白子先防守，第9手黑子开始多线攻击
            ("three_move_92", [("K7",1), ("J7",2), ("K9",1), ("K8",2), ("J9",1), ("L9",2), ("J8",1)],
             [("H7",2), ("I7",1), ("K6",2), ("I9",1), ("H9",2), ("I8",1)], "前7手已下完，白子先防守K线J线", 
             "白第8手H7防守，黑第9手I7冲四逼白K6挡，接着I9冲四逼白H9，最后I8形成连五制胜。"),
             
            # 题93: 前7手已下完，第8手白子先应对，第9手黑子开始斜向连击
            ("three_move_93", [("D11",1), ("E11",2), ("F10",1), ("G11",2), ("C11",1), ("B11",2), ("E12",1)],
             [("F12",2), ("A11",1), ("D10",2), ("G10",1), ("F11",2), ("H9",1)], "前7手已下完，白子先防守左下角", 
             "白第8手F12防守，黑第9手A11冲四逼白D10挡，接着G10冲四逼白F11，最后H9形成斜向连五制胜。"),
             
            # 题94: 前7手已下完，第8手白子先防守，第9手黑子开始交叉攻击
            ("three_move_94", [("H7",1), ("G7",2), ("F9",1), ("F8",2), ("G9",1), ("E9",2), ("H8",1)],
             [("H6",2), ("I7",1), ("G8",2), ("I9",1), ("E7",2), ("I8",1)], "前7手已下完，白子先防守中心区域", 
             "白第8手H6防守，黑第9手I7冲四逼白G8挡，接着I9冲四逼白E7，最后I8形成竖向连五制胜。"),
             
            # 题95: 前7手已下完，第8手白子先防守，第9手黑子开始横向连击
            ("three_move_95", [("F10",1), ("G10",2), ("H10",1), ("I10",2), ("J8",1), ("K8",2), ("J10",1)],
             [("K10",2), ("E10",1), ("G9",2), ("L10",1), ("I9",2), ("M10",1)], "前7手已下完，白子先防守横向", 
             "白第8手K10防守，黑第9手E10冲四逼白G9挡，接着L10冲四逼白I9，最后M10形成横向连五制胜。"),
        ]
        
        for pattern_id, setup, moves, description, analysis in three_move_data:
            initial_setup = [coord_to_pos(pos) + (player,) for pos, player in setup if coord_to_pos(pos)]
            move_sequence = [coord_to_pos(pos) + (player,) for pos, player in moves if coord_to_pos(pos)]
            
            patterns[pattern_id] = {
                "id": pattern_id,
                "name": pattern_id.replace("_", " ").title(),
                "difficulty": "高级",
                "description": description, 
                "initial_setup": initial_setup,
                "moves": move_sequence,
                "analysis": {
                    "opening": description,
                    "strategy": "通过三手棋的精密配合，连续冲四形成多重威胁，迫使对手疲于防守最终获胜",
                    "key_points": ["第一步冲四", "第二步威胁", "第三步制胜", "连续计算", "双重威胁"],
                    "win_reason": analysis
                }
            }
        
        return patterns
    
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