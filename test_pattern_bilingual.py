#!/usr/bin/env python3
"""
测试棋谱双语功能
Test pattern bilingual functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from game.pattern import PatternManager

def test_pattern_bilingual():
    """测试棋谱双语功能"""
    print("=" * 60)
    print("🎯 棋谱双语功能测试 / Pattern Bilingual Test")
    print("=" * 60)
    
    pm = PatternManager()
    
    # 测试英文模式
    print("\n📝 English Mode:")
    print("-" * 40)
    pm.set_language('english')
    patterns = pm.get_patterns_list()
    
    for i, pattern in enumerate(patterns[:3]):  # 只显示前3个
        print(f"{i+1:2d}. {pattern['name']:<15} | {pattern['difficulty']:<12} | {pattern['description']}")
    
    print("\n📝 Chinese Mode:")
    print("-" * 40)
    pm.set_language('chinese')
    patterns = pm.get_patterns_list()
    
    for i, pattern in enumerate(patterns[:3]):  # 只显示前3个
        print(f"{i+1:2d}. {pattern['name']:<15} | {pattern['difficulty']:<12} | {pattern['description']}")
    
    # 测试棋谱分析
    print(f"\n🔍 Testing pattern analysis:")
    print("-" * 40)
    
    # 测试英文模式的棋谱分析
    pm.set_language('english')
    if pm.load_pattern('one_move_1'):
        analysis = pm.get_pattern_analysis()
        if analysis:
            print("English Analysis:")
            print(f"  Strategy: {analysis['strategy']}")
            print(f"  Key Points: {analysis['key_points']}")
    
    # 测试中文模式的棋谱分析
    pm.set_language('chinese')
    if pm.load_pattern('one_move_1'):
        analysis = pm.get_pattern_analysis()
        if analysis:
            print("\nChinese Analysis:")
            print(f"  Strategy: {analysis['strategy']}")
            print(f"  Key Points: {analysis['key_points']}")
    
    print("\n" + "=" * 60)
    print("✅ 棋谱双语测试完成！Pattern bilingual test completed!")
    print("=" * 60)

if __name__ == "__main__":
    test_pattern_bilingual()