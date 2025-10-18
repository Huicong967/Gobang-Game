"""
Game Main Window
游戏主窗口
Create GUI using tkinter
使用tkinter创建图形界面
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
import os
import json

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game import Board, PatternManager, MoveValidator, sound_manager

# 简单的双语配置
CONFIG_FILE = "language_config.json"

# 翻译字典
TRANSLATIONS = {
    'english': {
        'app_title': 'Gobang Endgame Training System - by Xu Huicong',
        'choose_language': 'Choose Language',
        'language_english': 'English',
        'language_chinese': 'Chinese',
        'game_board': 'Game Board',
        'game_information': 'Game Information',
        'select_pattern': 'Select Pattern',
        'restart': 'Restart',
        'undo': 'Undo',
        'show_answer': 'Show Answer',
        'sound_on': '🔊 Sound ON',
        'sound_off': '🔇 Sound OFF',
        'hints': 'Hints:',
        'pattern_analysis': 'Pattern Analysis:',
        'select_pattern_title': 'Select Pattern',
        'select_pattern_prompt': 'Please select an endgame pattern for practice:',
        'ok': 'OK',
        'cancel': 'Cancel',
        'error': 'Error',
        'load_pattern_failed': 'Failed to load pattern!',
        'please_select_pattern': 'Please select an endgame pattern to practice',
        'please_select_first': 'Please select a pattern first!',
        'position_occupied': 'Position occupied, please choose another one!',
        'please_select_pattern_first': 'Please select an endgame pattern first!',
        'computer_turn_wait': "Computer's turn, please wait...",
        'no_moves_undo': 'No moves to undo!',
        'undid_one_move': 'Undid one move!',
        'undid_moves_back': 'Undid {} moves, back to your turn!',
        'undo_failed': 'Undo failed!',
        'hint_should_play': 'Hint: You should play at',
        'pattern_completed': 'Pattern completed!',
        'computer_turn_patient': "Computer's turn, please be patient!",
        'pattern_name': 'Pattern',
        'steps': 'Steps',
        'pattern_complete': 'Pattern completed!',
        'turn_player_white': 'Turn: Player(White) | Errors:',
        'computer_turn_thinking': "Computer's turn | Thinking...",
        'opening_analysis': 'Opening Analysis',
        'overall_strategy': 'Overall Strategy',
        'key_steps': 'Key Steps',
        'victory_principle': 'Victory Principle',
        'pattern_analysis_displayed': 'Pattern analysis displayed in right panel!',
        'endgame_restarted': 'Endgame restarted! You use WHITE stones, computer uses BLACK.',
        'system_demo_correct': 'System demo: Correct move',
        'sound_enabled': 'Sound enabled',
        'sound_disabled': 'Sound disabled',
        'black_stone': 'Black stone',
        'white_stone': 'White stone',
        'correct_move': 'Correct move!',
        'correct_move_computer_thinking': 'Correct move! Computer thinking...',
        'wrong_max_times': 'Wrong {} times, correct move is:',
        'wrong_move_chances_left': 'Wrong move! {} chances left. Hint:',
        'area_upper': 'upper',
        'area_middle': 'middle', 
        'area_lower': 'lower',
        'area_left': 'left',
        'area_center': 'center',
        'area_right': 'right',
        'area_hint': '{} {} area',
        'its_player_turn': "It's player's turn!",
        'computer_moved_your_turn': 'Computer moved, your turn!',
        'computer_move_failed': 'Computer move failed!'
    },
    'chinese': {
        'app_title': '五子棋残局训练系统 - 徐慧聪制作',
        'choose_language': '选择语言',
        'language_english': '英文',
        'language_chinese': '中文',
        'game_board': '游戏棋盘',
        'game_information': '游戏信息',
        'select_pattern': '选择棋谱',
        'restart': '重新开始',
        'undo': '悔棋',
        'show_answer': '显示答案',
        'sound_on': '🔊 音效开',
        'sound_off': '🔇 音效关',
        'hints': '提示信息:',
        'pattern_analysis': '棋谱分析:',
        'select_pattern_title': '选择棋谱',
        'select_pattern_prompt': '请选择要练习的残局棋谱：',
        'ok': '确定',
        'cancel': '取消',
        'error': '错误',
        'load_pattern_failed': '加载棋谱失败！',
        'please_select_pattern': '请选择残局棋谱进行练习',
        'please_select_first': '请先选择一个棋谱！',
        'position_occupied': '该位置已有棋子，请选择其他位置！',
        'please_select_pattern_first': '请先选择一个残局棋谱进行练习！',
        'computer_turn_wait': '现在轮到电脑下棋，请等待...',
        'no_moves_undo': '没有可以悔棋的步骤！',
        'undid_one_move': '已悔棋一步！',
        'undid_moves_back': '已悔棋{}步，回到你的回合！',
        'undo_failed': '悔棋失败！',
        'hint_should_play': '提示：你应该下在',
        'pattern_completed': '棋谱已完成！',
        'computer_turn_patient': '现在轮到电脑下棋，请耐心等待！',
        'pattern_name': '棋谱',
        'steps': '步骤',
        'pattern_complete': '棋谱完成！',
        'turn_player_white': '轮到：玩家(白子) | 错误：',
        'computer_turn_thinking': '电脑回合 | 思考中...',
        'opening_analysis': '开局分析',
        'overall_strategy': '整体策略', 
        'key_steps': '关键步骤',
        'victory_principle': '获胜原理',
        'pattern_analysis_displayed': '棋谱分析已显示在右侧面板！',
        'endgame_restarted': '残局重新开始！你执白子，电脑执黑子。',
        'system_demo_correct': '系统演示：正确走法',
        'sound_enabled': '音效已开启',
        'sound_disabled': '音效已关闭',
        'black_stone': '黑子',
        'white_stone': '白子',
        'correct_move': '走法正确！',
        'correct_move_computer_thinking': '走法正确！电脑思考中...',
        'wrong_max_times': '已错误{}次，正确走法是：',
        'wrong_move_chances_left': '走法错误！还有{}次机会。提示：',
        'area_upper': '上方',
        'area_middle': '中间',
        'area_lower': '下方', 
        'area_left': '左侧',
        'area_center': '中间',
        'area_right': '右侧',
        'area_hint': '棋盘{}{}区域',
        'its_player_turn': '现在轮到玩家下棋！',
        'computer_moved_your_turn': '电脑已下棋，轮到你了！',
        'computer_move_failed': '电脑下棋失败！'
    }
}

class LanguageManager:
    """语言管理器"""
    def __init__(self):
        self.current_language = 'english'
        self.load_language_config()
    
    def load_language_config(self):
        """加载语言配置"""
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)
                self.current_language = config.get('language', 'english')
        except:
            self.current_language = 'english'
    
    def save_language_config(self):
        """保存语言配置"""
        try:
            config = {'language': self.current_language}
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
        except:
            pass
    
    def set_language(self, language):
        """设置语言"""
        if language in TRANSLATIONS:
            self.current_language = language
            self.save_language_config()
    
    def get_text(self, key, *args):
        """获取翻译文本"""
        text = TRANSLATIONS[self.current_language].get(key, key)
        if args:
            return text.format(*args)
        return text
    
    def choose_language(self, parent=None):
        """显示语言选择对话框"""
        dialog = tk.Toplevel(parent) if parent else tk.Tk()
        dialog.title(TRANSLATIONS['english']['choose_language'])
        dialog.geometry("300x150")
        dialog.resizable(False, False)
        
        # 居中显示
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (300 // 2)
        y = (dialog.winfo_screenheight() // 2) - (150 // 2)
        dialog.geometry(f"300x150+{x}+{y}")
        
        if parent:
            dialog.transient(parent)
            dialog.grab_set()
        
        result = None
        
        def select_english():
            nonlocal result
            result = 'english'
            dialog.quit()
        
        def select_chinese():
            nonlocal result
            result = 'chinese'
            dialog.quit()
        
        # 创建界面
        main_frame = ttk.Frame(dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text=TRANSLATIONS['english']['choose_language'], font=("Arial", 12)).pack(pady=(0, 20))
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack()
        
        ttk.Button(button_frame, text=TRANSLATIONS['english']['language_english'], command=select_english).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text=TRANSLATIONS['chinese']['language_chinese'], command=select_chinese).pack(side=tk.LEFT, padx=10)
        
        if parent is None:
            dialog.protocol("WM_DELETE_WINDOW", dialog.quit)
        
        dialog.mainloop()
        
        if parent is None:
            dialog.destroy()
        else:
            dialog.destroy()
        
        return result

# 全局语言管理器
language_manager = LanguageManager()


class GameWindow:
    """游戏主窗口类"""
    
    def __init__(self):
        """初始化游戏窗口"""
        # 首先选择语言
        selected_language = language_manager.choose_language()
        if selected_language:
            language_manager.set_language(selected_language)
        
        self.root = tk.Tk()
        self.root.title(language_manager.get_text('app_title'))
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        
        # 游戏组件
        self.board = Board()
        self.pattern_manager = PatternManager()
        # 同步语言设置到棋谱管理器
        self.pattern_manager.set_language(language_manager.current_language)
        self.validator = MoveValidator(self.pattern_manager, self.board, language_manager)
        
        # 音效管理器
        self.sound_manager = sound_manager
        
        # GUI 变量
        self.canvas_size = 480
        self.cell_size = self.canvas_size // (self.board.size - 1)
        self.margin = 30
        
        # 创建界面
        self.create_widgets()
        self.show_pattern_selection()
        
        # 绑定事件
        self.canvas.bind("<Button-1>", self.on_canvas_click)
    
    def create_widgets(self):
        """创建界面组件"""
        # 主框架
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 左侧 - 游戏区域 / Left side - Game area
        game_frame = ttk.LabelFrame(main_frame, text=language_manager.get_text('game_board'), padding="10")
        game_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        # 棋盘画布
        self.canvas = tk.Canvas(
            game_frame,
            width=self.canvas_size + 2 * self.margin,
            height=self.canvas_size + 2 * self.margin,
            bg="burlywood"
        )
        self.canvas.pack()
        
        # 游戏控制按钮
        control_frame = ttk.Frame(game_frame)
        control_frame.pack(pady=(10, 0))
        
        ttk.Button(control_frame, text=language_manager.get_text('select_pattern'), command=self.show_pattern_selection).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text=language_manager.get_text('restart'), command=self.restart_pattern).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text=language_manager.get_text('undo'), command=self.undo_move).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text=language_manager.get_text('show_answer'), command=self.show_answer).pack(side=tk.LEFT, padx=5)
        
        # 音效控制按钮
        self.sound_button_text = tk.StringVar()
        self.update_sound_button_text()
        ttk.Button(control_frame, textvariable=self.sound_button_text, command=self.toggle_sound).pack(side=tk.LEFT, padx=5)
        
        # 右侧 - 信息区域 / Right side - Information area
        info_frame = ttk.LabelFrame(main_frame, text=language_manager.get_text('game_information'), padding="10")
        info_frame.grid(row=0, column=1, sticky="nsew")
        
        # 棋谱信息 / Pattern information
        self.pattern_info_var = tk.StringVar(value=language_manager.get_text('please_select_pattern'))
        pattern_info_label = ttk.Label(info_frame, textvariable=self.pattern_info_var, font=("Arial", 10, "bold"))
        pattern_info_label.pack(anchor="w", pady=(0, 10))
        
        # 当前状态 / Current status  
        self.status_var = tk.StringVar(value=language_manager.get_text('please_select_pattern'))
        status_label = ttk.Label(info_frame, textvariable=self.status_var, font=("Arial", 9))
        status_label.pack(anchor="w", pady=(0, 10))
        
        # 步骤信息
        self.step_var = tk.StringVar(value="")
        step_label = ttk.Label(info_frame, textvariable=self.step_var)
        step_label.pack(anchor="w", pady=(0, 10))
        
        # 提示信息区域 / Hint information area
        ttk.Label(info_frame, text=language_manager.get_text('hints'), font=("Arial", 9, "bold")).pack(anchor="w")
        self.hint_text = scrolledtext.ScrolledText(info_frame, width=40, height=8, wrap=tk.WORD)
        self.hint_text.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        
        # 棋谱分析区域 / Pattern analysis area
        ttk.Label(info_frame, text=language_manager.get_text('pattern_analysis'), font=("Arial", 9, "bold")).pack(anchor="w")
        self.analysis_text = scrolledtext.ScrolledText(info_frame, width=40, height=10, wrap=tk.WORD)
        self.analysis_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # 配置网格权重
        main_frame.columnconfigure(0, weight=0)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        # 绘制空棋盘
        self.draw_board()
    
    def draw_board(self):
        """绘制棋盘"""
        self.canvas.delete("all")
        
        # 绘制棋盘线条
        for i in range(self.board.size):
            x = self.margin + i * self.cell_size
            y = self.margin + i * self.cell_size
            
            # 垂直线
            self.canvas.create_line(
                x, self.margin,
                x, self.margin + (self.board.size - 1) * self.cell_size,
                fill="black", width=1
            )
            
            # 水平线
            self.canvas.create_line(
                self.margin, y,
                self.margin + (self.board.size - 1) * self.cell_size, y,
                fill="black", width=1
            )
        
        # 绘制星位点
        star_positions = [(3, 3), (3, 11), (11, 3), (11, 11), (7, 7)]
        for row, col in star_positions:
            x = self.margin + col * self.cell_size
            y = self.margin + row * self.cell_size
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")
        
        # 绘制棋子
        self.draw_stones()
    
    def draw_stones(self):
        """绘制棋子"""
        board_state = self.board.get_board_state()
        
        for row in range(self.board.size):
            for col in range(self.board.size):
                if board_state[row, col] != 0:
                    x = self.margin + col * self.cell_size
                    y = self.margin + row * self.cell_size
                    
                    color = "black" if board_state[row, col] == 1 else "white"
                    outline_color = "black"
                    
                    self.canvas.create_oval(
                        x-8, y-8, x+8, y+8,
                        fill=color, outline=outline_color, width=1
                    )
                    
                    # 为最后一手棋标记
                    if self.board.move_history and (row, col) == (self.board.move_history[-1][0], self.board.move_history[-1][1]):
                        self.canvas.create_oval(
                            x-4, y-4, x+4, y+4,
                            outline="red", width=2, fill=""
                        )
    
    def on_canvas_click(self, event):
        """处理棋盘点击事件 - 玩家vs电脑模式"""
        # 计算点击的网格位置
        x = event.x - self.margin
        y = event.y - self.margin
        
        col = round(x / self.cell_size)
        row = round(y / self.cell_size)
        
        # 检查是否在有效范围内
        if not (0 <= row < self.board.size and 0 <= col < self.board.size):
            return
        
        # 检查该位置是否已有棋子 / Check if position is occupied
        if not self.board.is_valid_move(row, col):
            self.add_hint(language_manager.get_text('position_occupied'))
            return
        
        # 检查是否已选择棋谱 / Check if pattern is selected
        if not self.pattern_manager.current_pattern:
            self.add_hint(language_manager.get_text('please_select_pattern_first'))
            return
        
        # 检查是否轮到玩家 / Check if it's player's turn
        if not self.validator.is_player_turn:
            self.add_hint(language_manager.get_text('computer_turn_wait'))
            return
        
        # 验证玩家走法（动态确定玩家颜色）
        result = self.validator.validate_player_move(row, col)
        if result['valid']:
            correct_move = result['correct_move']
            if correct_move:
                self.board.make_move(row, col, correct_move[2])
                self.sound_manager.play_stone_place()  # 播放落子音效
            self.draw_stones()
            self.add_hint(result['message'])
            self.update_status()
            if result['pattern_complete']:
                self.sound_manager.play_pattern_complete()  # 播放完成音效
                self.show_pattern_analysis()
            elif result.get('computer_move', False):
                # 延迟一点时间让玩家看到自己的走法，然后电脑走棋
                self.root.after(800, self.make_computer_move)
        else:
            self.sound_manager.play_error()  # 播放错误音效
            self.add_hint(result['message'])
            if result['show_answer']:
                self.root.after(1000, self.auto_make_correct_move)
    
    def make_computer_move(self):
        """电脑自动下棋"""
        if not self.validator.is_computer_turn():
            return
        
        result = self.validator.make_computer_move()
        
        if result['move']:
            row, col, player = result['move']
            self.sound_manager.play_stone_place()  # 播放落子音效
            self.draw_stones()  # 重新绘制棋盘
            self.add_hint(result['message'])
            self.update_status()
            
            if result['pattern_complete']:
                self.show_pattern_analysis()
        else:
            self.add_hint(result['message'])
    
    def auto_make_correct_move(self):
        """自动执行正确走法（3次错误后）"""
        correct_move = self.validator.auto_make_correct_move()
        if correct_move:
            self.draw_stones()
            # 显示正确走法
            self.add_hint(f"{language_manager.get_text('system_demo_correct')} {self._format_move(correct_move)}")
            self.update_status()
            
            # 检查棋谱是否完成
            if self.pattern_manager.is_pattern_complete():
                self.show_pattern_analysis()
            else:
                # 如果还没完成，继续下一步，可能需要电脑走棋
                if self.validator.is_computer_turn():
                    self.root.after(1500, self.make_computer_move)
    
    def show_pattern_selection(self):
        """显示棋谱选择对话框"""
        patterns = self.pattern_manager.get_patterns_list()
        
        # 创建选择窗口 / Create selection window
        selection_window = tk.Toplevel(self.root)
        selection_window.title(language_manager.get_text('select_pattern_title'))
        selection_window.geometry("500x350")
        selection_window.transient(self.root)
        selection_window.grab_set()
        
        # 棋谱列表 / Pattern list
        ttk.Label(selection_window, text=language_manager.get_text('select_pattern_prompt'), font=("Arial", 10, "bold")).pack(pady=10)
        
        listbox = tk.Listbox(selection_window, height=10)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 填充棋谱列表
        for pattern in patterns:
            listbox.insert(tk.END, f"[{pattern['difficulty']}] {pattern['name']}")
        
        # 选择按钮
        def on_select():
            selection = listbox.curselection()
            if selection:
                pattern_id = patterns[selection[0]]['id']
                if self.pattern_manager.load_pattern(pattern_id):
                    self.restart_pattern()
                    selection_window.destroy()
                else:
                    messagebox.showerror(language_manager.get_text('error'), language_manager.get_text('load_pattern_failed'))
        
        button_frame = ttk.Frame(selection_window)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text=language_manager.get_text('ok'), command=on_select).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text=language_manager.get_text('cancel'), command=selection_window.destroy).pack(side=tk.LEFT, padx=5)
    
    def restart_pattern(self):
        """重新开始当前棋谱 / Restart current pattern"""
        if not self.pattern_manager.current_pattern:
            self.add_hint(language_manager.get_text('please_select_first'))
            return
        
        self.sound_manager.play_game_start()  # 播放游戏开始音效
        self.board.reset()
        self.pattern_manager.reset_pattern()
        self.validator.reset_game()
        
        # 设置残局初始局面
        self.setup_endgame_initial_position()
        
        # 初始化固定的玩家和电脑颜色
        self.validator.initialize_player_colors()
        
        # 显示玩家执子颜色提示
        self.add_hint(language_manager.get_text('endgame_restarted'))
        
        self.draw_board()
        self.update_status()
        self.clear_analysis()
    
    def undo_move(self):
        """悔棋 - 撤销最近的一步或两步（玩家+电脑）"""
        if len(self.board.move_history) == 0:
            self.add_hint(language_manager.get_text('no_moves_undo'))
            return
        
        # 如果最后一步是电脑下的，需要撤销两步回到玩家回合
        moves_to_undo = 1
        if len(self.board.move_history) > 0:
            last_move = self.board.move_history[-1]
            # 动态判断最后一步是否是电脑下的
            expected_move = self.pattern_manager.get_current_move()
            is_computer_last = expected_move and last_move[2] != expected_move[2]
            if is_computer_last:  # 最后一步是电脑下的
                moves_to_undo = 2
        
        # 执行悔棋
        undone_moves = []
        for _ in range(min(moves_to_undo, len(self.board.move_history))):
            undone_move = self.board.undo_move()
            if undone_move:
                undone_moves.append(undone_move)
                # 回退棋谱步骤
                if self.pattern_manager.current_step > 0:
                    self.pattern_manager.current_step -= 1
        
        if undone_moves:
            self.validator.reset_errors()
            # 确保轮到玩家（根据棋谱动态确定）
            if self.pattern_manager.current_pattern:
                current_move = self.pattern_manager.get_current_move()
                if current_move:
                    # 根据当前应该下的棋子颜色判断轮到谁
                    self.validator.is_player_turn = (current_move[2] == self.validator.player_color)
            self.draw_board()
            self.update_status()
            if len(undone_moves) == 1:
                self.add_hint(language_manager.get_text('undid_one_move'))
            else:
                self.add_hint(language_manager.get_text('undid_moves_back').format(len(undone_moves)))
        else:
            self.add_hint(language_manager.get_text('undo_failed'))
    
    def show_answer(self):
        """显示当前步骤的正确答案"""
        if self.validator.is_player_turn:
            expected_move = self.pattern_manager.get_current_move()
            if expected_move:
                row, col, player = expected_move
                self.add_hint(f"{language_manager.get_text('hint_should_play')} {self._format_position(row, col)}")
            else:
                self.add_hint(language_manager.get_text('pattern_completed'))
        else:
            self.add_hint(language_manager.get_text('computer_turn_patient'))
    
    def update_status(self):
        """更新状态信息"""
        if not self.pattern_manager.current_pattern:
            return
        
        pattern_info = self.pattern_manager.get_pattern_info()
        
        # 更新棋谱信息
        colon = "：" if language_manager.current_language == 'chinese' else ": "
        info_text = f"{language_manager.get_text('pattern_name')}{colon}{pattern_info['name']} ({pattern_info['difficulty']})"
        self.pattern_info_var.set(info_text)
        
        # 更新步骤信息
        step_text = f"{language_manager.get_text('steps')}{colon}{pattern_info['current_step']}/{pattern_info['total_moves']}"
        self.step_var.set(step_text)
        
        # 更新当前状态 / Update current status
        if self.pattern_manager.is_pattern_complete():
            self.status_var.set(language_manager.get_text('pattern_complete'))
        else:
            if self.validator.is_player_turn:
                error_info = self.validator.get_error_info()
                status_text = f"{language_manager.get_text('turn_player_white')} {error_info['error_count']}/{error_info['max_errors']}"
            else:
                status_text = language_manager.get_text('computer_turn_thinking')
            self.status_var.set(status_text)
    
    def add_hint(self, message):
        """添加提示信息"""
        self.hint_text.insert(tk.END, f"• {message}\n")
        self.hint_text.see(tk.END)
    
    def show_pattern_analysis(self):
        """显示棋谱分析"""
        analysis = self.pattern_manager.get_pattern_analysis()
        if not analysis:
            return
        
        self.analysis_text.delete(1.0, tk.END)
        
        # 显示分析内容 / Display analysis content
        self.analysis_text.insert(tk.END, f"【{language_manager.get_text('opening_analysis')}】\n{analysis.get('opening', '')}\n\n")
        self.analysis_text.insert(tk.END, f"【{language_manager.get_text('overall_strategy')}】\n{analysis.get('strategy', '')}\n\n")
        
        key_points = analysis.get('key_points', [])
        if key_points:
            self.analysis_text.insert(tk.END, f"【{language_manager.get_text('key_steps')}】\n")
            for point in key_points:
                self.analysis_text.insert(tk.END, f"• {point}\n")
            self.analysis_text.insert(tk.END, "\n")
        
        win_reason = analysis.get('win_reason', '')
        if win_reason:
            self.analysis_text.insert(tk.END, f"【{language_manager.get_text('victory_principle')}】\n{win_reason}\n")
        
        self.add_hint(language_manager.get_text('pattern_analysis_displayed'))
    
    def clear_analysis(self):
        """清空分析区域"""
        self.analysis_text.delete(1.0, tk.END)
    
    def setup_endgame_initial_position(self):
        """设置残局初始局面"""
        if not self.pattern_manager.current_pattern:
            return
        
        # 获取初始局面设置
        initial_setup = self.pattern_manager.current_pattern.get('initial_setup', [])
        
        # 在棋盘上放置初始棋子
        for row, col, player in initial_setup:
            self.board.make_move(row, col, player)
        
        # 重新绘制棋盘
        self.draw_stones()
    
    def _format_move(self, move):
        """格式化走法"""
        row, col, player = move
        player_name = language_manager.get_text('black_stone') if player == 1 else language_manager.get_text('white_stone')
        return f"{player_name} {self._format_position(row, col)}"
    
    def _format_position(self, row, col):
        """格式化位置"""
        col_letter = chr(ord('A') + col)
        row_number = row + 1
        return f"{col_letter}{row_number}"
    
    def update_sound_button_text(self):
        """更新音效按钮文本"""
        text = language_manager.get_text('sound_on') if self.sound_manager.is_enabled() else language_manager.get_text('sound_off')
        self.sound_button_text.set(text)
    
    def toggle_sound(self):
        """切换音效开关 / Toggle sound on/off"""
        self.sound_manager.play_button_click()
        enabled = self.sound_manager.toggle_sound()
        self.update_sound_button_text()
        
        status = language_manager.get_text('sound_enabled') if enabled else language_manager.get_text('sound_disabled')
        self.add_hint(status)
    
    def run(self):
        """运行游戏"""
        self.root.mainloop()


if __name__ == "__main__":
    game = GameWindow()
    game.run()