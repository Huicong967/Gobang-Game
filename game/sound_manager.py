"""
Sound Manager for Gobang Game
五子棋游戏音效管理器

Handles all sound effects using pygame
使用pygame处理所有音效
"""

import pygame
import os
import sys
from pathlib import Path


class SoundManager:
    """Sound Manager Class / 音效管理器类"""
    
    def __init__(self):
        """Initialize sound manager / 初始化音效管理器"""
        self.enabled = True
        self.volume = 0.7
        self.sounds = {}
        
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            self._load_sounds()
        except pygame.error as e:
            print(f"Sound initialization failed / 音效初始化失败: {e}")
            self.enabled = False
    
    def _load_sounds(self):
        """Load sound files / 加载音效文件"""
        # Get sounds directory / 获取音效目录
        sounds_dir = Path(__file__).parent / "sounds"
        
        # If sounds directory doesn't exist, create it / 如果音效目录不存在则创建
        if not sounds_dir.exists():
            sounds_dir.mkdir(exist_ok=True)
            self._create_default_sounds(sounds_dir)
        
        # Load sound files / 加载音效文件
        sound_files = {
            "stone_place": "stone_place.wav",      # 落子音效
            "pattern_complete": "pattern_complete.wav",  # 棋谱完成音效
            "error": "error.wav",                  # 错误音效
            "button_click": "button_click.wav",    # 按钮点击音效
            "game_start": "game_start.wav"         # 游戏开始音效
        }
        
        for sound_name, filename in sound_files.items():
            sound_path = sounds_dir / filename
            if sound_path.exists():
                try:
                    self.sounds[sound_name] = pygame.mixer.Sound(str(sound_path))
                    self.sounds[sound_name].set_volume(self.volume)
                except pygame.error as e:
                    print(f"Failed to load sound {filename} / 加载音效文件失败 {filename}: {e}")
            else:
                # Create a simple beep sound as fallback / 创建简单的提示音作为备用
                self.sounds[sound_name] = self._create_beep_sound(sound_name)
    
    def _create_default_sounds(self, sounds_dir):
        """Create default sound files info / 创建默认音效文件信息"""
        readme_content = """# Sound Files Directory / 音效文件目录

This directory contains sound effects for the Gobang game.
此目录包含五子棋游戏的音效文件。

## Required Files / 必需文件:
- stone_place.wav      # Stone placement sound / 落子音效
- pattern_complete.wav # Pattern completion sound / 棋谱完成音效  
- error.wav           # Error sound / 错误音效
- button_click.wav    # Button click sound / 按钮点击音效
- game_start.wav      # Game start sound / 游戏开始音效

## Audio Format / 音频格式:
- Format: WAV
- Sample Rate: 22050 Hz or 44100 Hz
- Channels: Mono or Stereo
- Bit Depth: 16-bit

## Notes / 说明:
If sound files are not found, the game will use generated beep sounds as fallback.
如果找不到音效文件，游戏将使用生成的提示音作为备用。
"""
        
        readme_path = sounds_dir / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
    
    def _create_beep_sound(self, sound_type):
        """Create simple beep sound as fallback / 创建简单提示音作为备用"""
        try:
            # Generate different frequency beeps for different sound types
            # 为不同音效类型生成不同频率的提示音
            frequencies = {
                "stone_place": 800,       # 落子音效 - 中频
                "pattern_complete": 1200, # 完成音效 - 高频
                "error": 400,             # 错误音效 - 低频
                "button_click": 600,      # 按钮音效 - 中低频
                "game_start": 1000        # 开始音效 - 中高频
            }
            
            frequency = frequencies.get(sound_type, 800)
            duration = 0.1  # 100ms
            sample_rate = 22050
            
            # Generate sine wave / 生成正弦波
            import numpy as np
            frames = int(duration * sample_rate)
            arr = np.zeros((frames, 2))  # Stereo
            
            for i in range(frames):
                wave = 0.3 * np.sin(2 * np.pi * frequency * i / sample_rate)
                arr[i] = [wave, wave]
            
            # Convert to pygame sound / 转换为pygame音效
            arr = (arr * 32767).astype(np.int16)
            sound = pygame.sndarray.make_sound(arr)
            sound.set_volume(self.volume)
            
            return sound
            
        except Exception as e:
            print(f"Failed to create beep sound / 创建提示音失败: {e}")
            return None
    
    def play_sound(self, sound_name):
        """Play sound effect / 播放音效"""
        if not self.enabled or sound_name not in self.sounds:
            return
        
        try:
            sound = self.sounds[sound_name]
            if sound:
                sound.play()
        except pygame.error as e:
            print(f"Error playing sound {sound_name} / 播放音效错误 {sound_name}: {e}")
    
    def play_stone_place(self):
        """Play stone placement sound / 播放落子音效"""
        self.play_sound("stone_place")
    
    def play_pattern_complete(self):
        """Play pattern completion sound / 播放棋谱完成音效"""
        self.play_sound("pattern_complete")
    
    def play_error(self):
        """Play error sound / 播放错误音效"""
        self.play_sound("error")
    
    def play_button_click(self):
        """Play button click sound / 播放按钮点击音效"""
        self.play_sound("button_click")
    
    def play_game_start(self):
        """Play game start sound / 播放游戏开始音效"""
        self.play_sound("game_start")
    
    def set_volume(self, volume):
        """Set volume (0.0 to 1.0) / 设置音量 (0.0 到 1.0)"""
        self.volume = max(0.0, min(1.0, volume))
        for sound in self.sounds.values():
            if sound:
                sound.set_volume(self.volume)
    
    def toggle_sound(self):
        """Toggle sound on/off / 切换音效开关"""
        self.enabled = not self.enabled
        return self.enabled
    
    def is_enabled(self):
        """Check if sound is enabled / 检查音效是否启用"""
        return self.enabled
    
    def cleanup(self):
        """Cleanup sound resources / 清理音效资源"""
        try:
            pygame.mixer.quit()
        except:
            pass


# Global sound manager instance / 全局音效管理器实例
sound_manager = SoundManager()