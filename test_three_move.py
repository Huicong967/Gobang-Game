#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game.pattern import PatternManager

def test_all_three_move_patterns():
    pm = PatternManager()
    
    for pattern_id in ['three_move_91', 'three_move_92', 'three_move_93', 'three_move_94', 'three_move_95']:
        pm.load_pattern(pattern_id)
        pattern = pm.current_pattern
        
        print(f"\n=== {pattern_id} ===")
        black_count = sum(1 for _, _, p in pattern['initial_setup'] if p == 1)
        white_count = sum(1 for _, _, p in pattern['initial_setup'] if p == 2)
        print(f"初始局面: 黑子{black_count}个, 白子{white_count}个")
        
        # 检查是否符合五子棋规则
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
            
        # 显示前几手
        print("前几手已下:")
        for i, (r, c, p) in enumerate(pattern['initial_setup'], 1):
            color = "黑" if p == 1 else "白"
            pos = chr(ord('A') + c) + str(r + 1)
            print(f"  第{i}手: {color}{pos}")
        
        print("后续走法:")    
        for i, (r, c, p) in enumerate(pattern['moves'], 1):
            color = "黑" if p == 1 else "白"
            pos = chr(ord('A') + c) + str(r + 1)
            step_num = len(pattern['initial_setup']) + i
            print(f"  第{step_num}手: {color}{pos}")

if __name__ == "__main__":
    test_all_three_move_patterns()