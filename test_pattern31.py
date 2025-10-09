#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game.pattern import PatternManager

def test_pattern_31():
    pm = PatternManager()
    pm.load_pattern('two_move_31')
    pattern = pm.current_pattern
    
    print("第31题初始局面棋子数量:")
    black_count = sum(1 for _, _, p in pattern['initial_setup'] if p == 1)
    white_count = sum(1 for _, _, p in pattern['initial_setup'] if p == 2)
    print(f"黑子: {black_count}个, 白子: {white_count}个")
    
    print("\n初始局面详情:")
    for i, (r, c, p) in enumerate(pattern['initial_setup'], 1):
        color = "黑子" if p == 1 else "白子"
        pos_letter = chr(ord('A') + c)
        pos_number = r + 1
        print(f"第{i}手: {color} 位置{pos_letter}{pos_number} ({r},{c})")
    
    print("\n后续走法:")
    for i, (r, c, p) in enumerate(pattern['moves'], 1):
        color = "黑子" if p == 1 else "白子" 
        pos_letter = chr(ord('A') + c)
        pos_number = r + 1
        print(f"第{6+i}手: {color} 位置{pos_letter}{pos_number} ({r},{c})")
    
    # 检查是否有位置冲突
    initial_positions = set((r, c) for r, c, _ in pattern['initial_setup'])
    move_positions = set((r, c) for r, c, _ in pattern['moves'])
    conflicts = initial_positions.intersection(move_positions)
    
    if conflicts:
        print(f"\n警告：发现位置冲突: {conflicts}")
    else:
        print("\n✓ 没有位置冲突")

if __name__ == "__main__":
    test_pattern_31()