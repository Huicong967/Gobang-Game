#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game.pattern import PatternManager

def check_all_patterns():
    pm = PatternManager()
    
    # 检查所有棋谱
    pattern_ids = ['two_move_31', 'two_move_32', 'two_move_33', 'two_move_34', 'two_move_35']
    
    for pattern_id in pattern_ids:
        pm.load_pattern(pattern_id)
        pattern = pm.current_pattern
        
        print(f"\n=== {pattern_id} ===")
        
        # 统计初始局面
        black_initial = sum(1 for _, _, p in pattern['initial_setup'] if p == 1)
        white_initial = sum(1 for _, _, p in pattern['initial_setup'] if p == 2)
        
        # 统计后续走法
        black_moves = sum(1 for _, _, p in pattern['moves'] if p == 1)  
        white_moves = sum(1 for _, _, p in pattern['moves'] if p == 2)
        
        # 总计
        total_black = black_initial + black_moves
        total_white = white_initial + white_moves
        total_moves = len(pattern['initial_setup']) + len(pattern['moves'])
        
        print(f"初始局面: 黑{black_initial}个, 白{white_initial}个")
        print(f"后续走法: 黑{black_moves}个, 白{white_moves}个") 
        print(f"总计: 黑{total_black}个, 白{total_white}个 (共{total_moves}手)")
        
        # 检查是否符合五子棋规则
        if total_black == total_white + 1:
            print("✓ 符合规则: 黑先手，黑子比白子多1")
        elif total_black == total_white:
            print("✓ 符合规则: 黑白数量相等")  
        else:
            print(f"✗ 不符合规则: 黑{total_black}个 vs 白{total_white}个")
        
        # 按手数验证
        expected_black = (total_moves + 1) // 2  # 奇数手黑子多1
        expected_white = total_moves // 2
        
        if total_black != expected_black or total_white != expected_white:
            print(f"✗ 手数验证失败: 应该是黑{expected_black}个，白{expected_white}个")
        else:
            print("✓ 手数验证通过")

if __name__ == "__main__":
    check_all_patterns()