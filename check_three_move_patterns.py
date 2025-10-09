#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game.pattern import PatternManager

def check_three_move_patterns():
    pm = PatternManager()
    
    # 检查三手胜棋谱
    pattern_ids = ['three_move_91', 'three_move_92', 'three_move_93', 'three_move_94', 'three_move_95']
    
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
        
        print(f"初始局面: {len(pattern['initial_setup'])}手 -> 黑{black_initial}个, 白{white_initial}个")
        print(f"后续走法: {len(pattern['moves'])}手 -> 黑{black_moves}个, 白{white_moves}个") 
        print(f"总计: {total_moves}手 -> 黑{total_black}个, 白{total_white}个")
        
        # 检查是否符合五子棋规则
        expected_black = (total_moves + 1) // 2  # 奇数手黑子多1
        expected_white = total_moves // 2
        
        if total_black == expected_black and total_white == expected_white:
            print("✓ 符合规则")
        else:
            print(f"✗ 不符合规则: 应该是黑{expected_black}个，白{expected_white}个")
        
        # 检查初始局面是否应该调整
        initial_moves = len(pattern['initial_setup'])
        if initial_moves % 2 == 0:  # 偶数手
            print(f"建议: 初始局面改为{initial_moves-1}手或{initial_moves+1}手（奇数）")
        else:
            print("初始局面手数合理（奇数）")

if __name__ == "__main__":
    check_three_move_patterns()