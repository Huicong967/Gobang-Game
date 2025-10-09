#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game.pattern import PatternManager

def check_all_patterns_final():
    pm = PatternManager()
    
    print("=== 最终检查所有棋谱类型 ===\n")
    
    # 检查各类型的代表题目
    test_patterns = [
        ('one_move_1', '一手胜'),
        ('two_move_31', '两手胜'), 
        ('three_move_91', '三手胜')
    ]
    
    for pattern_id, pattern_type in test_patterns:
        try:
            pm.load_pattern(pattern_id)
            pattern = pm.current_pattern
            
            print(f"=== {pattern_type} - {pattern_id} ===")
            
            # 统计
            black_initial = sum(1 for _, _, p in pattern['initial_setup'] if p == 1)
            white_initial = sum(1 for _, _, p in pattern['initial_setup'] if p == 2)
            black_moves = sum(1 for _, _, p in pattern['moves'] if p == 1)  
            white_moves = sum(1 for _, _, p in pattern['moves'] if p == 2)
            total_black = black_initial + black_moves
            total_white = white_initial + white_moves
            total_moves = len(pattern['initial_setup']) + len(pattern['moves'])
            
            print(f"初始局面: {len(pattern['initial_setup'])}手 -> 黑{black_initial}个, 白{white_initial}个")
            print(f"后续走法: {len(pattern['moves'])}手 -> 黑{black_moves}个, 白{white_moves}个") 
            print(f"总计: {total_moves}手 -> 黑{total_black}个, 白{total_white}个")
            
            # 验证规则
            expected_black = (total_moves + 1) // 2
            expected_white = total_moves // 2
            
            if total_black == expected_black and total_white == expected_white:
                print("✓ 符合五子棋规则")
            else:
                print(f"✗ 不符合规则: 应该是黑{expected_black}个，白{expected_white}个")
                
            # 显示完整序列验证
            print("完整走法序列:")
            all_moves = []
            for i, (r, c, p) in enumerate(pattern['initial_setup'], 1):
                all_moves.append((i, r, c, p, "初局"))
            for i, (r, c, p) in enumerate(pattern['moves'], 1):
                step = len(pattern['initial_setup']) + i
                all_moves.append((step, r, c, p, "玩家操作"))
            
            for step, r, c, p, stage in all_moves:
                color = '黑' if p == 1 else '白'
                expected = '黑' if step % 2 == 1 else '白'
                status = '✓' if color == expected else '✗'
                pos = chr(ord('A') + c) + str(r + 1)
                print(f"  {status} 第{step}手: {color}{pos} ({stage})")
            print()
            
        except Exception as e:
            print(f"无法加载 {pattern_id}: {e}\n")

if __name__ == "__main__":
    check_all_patterns_final()