"""
Gobang Game Core Module / 五子棋游戏核心模块

AI-Assisted Development / AI辅助开发
This module was developed with the assistance of AI coding agents.
本模块由AI代理辅助编码完成。
"""

from .board import Board
from .pattern import PatternManager
from .validator import MoveValidator
from .sound_manager import SoundManager, sound_manager

__all__ = ['Board', 'PatternManager', 'MoveValidator', 'SoundManager', 'sound_manager']