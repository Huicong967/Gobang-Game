#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game.pattern import PatternManager

def test_all_two_move_patterns():
    pm = PatternManager()
    
    for pattern_id in ['two_move_31', 'two_move_32', 'two_move_33', 'two_move_34', 'two_move_35']:
        pm.load_pattern(pattern_id)
        pattern = pm.current_pattern
        
        print(f"\n=== {pattern_id} ===")
        black_count = sum(1 for _, _, p in pattern['initial_setup'] if p == 1)
        white_count = sum(1 for _, _, p in pattern['initial_setup'] if p == 2)
        print(f"初始局面: 黑子{black_count}个, 白子{white_count}个")
        
        # 检查是否符合五子棋规则（黑子数量 = 白子数量 或 黑子数量 = 白子数量 + 1）
        if black_count == white_count or black_count == white_count + 1:
            print("✓ 棋子数量符合规则")
        else:
            print("✗ 棋子数量不符合规则")
        
        # 检查位置冲突
        initial_positions = set((r, c) for r, c, _ in pattern['initial_setup'])
        move_positions = set((r, c) for r, c, _ in pattern['moves'])
        conflicts = initial_positions.intersection(move_positions)
        
        if conflicts:
            print(f"✗ 发现位置冲突: {conflicts}")
        else:
            print("✓ 没有位置冲突")
            
        # 显示走法顺序
        print("走法顺序:")
        for i, (r, c, p) in enumerate(pattern['initial_setup'], 1):
            color = "黑" if p == 1 else "白"
            pos = chr(ord('A') + c) + str(r + 1)
            print(f"  第{i}手: {color}{pos}")
        
        print("玩家操作:")    
        for i, (r, c, p) in enumerate(pattern['moves'], 1):
            color = "黑" if p == 1 else "白"
            pos = chr(ord('A') + c) + str(r + 1)
            step_num = len(pattern['initial_setup']) + i
            print(f"  第{step_num}手: {color}{pos}")

if __name__ == "__main__":
    test_all_two_move_patterns()