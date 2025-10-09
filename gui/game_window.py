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

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game import Board, PatternManager, MoveValidator


class GameWindow:
    """游戏主窗口类"""
    
    def __init__(self):
        """初始化游戏窗口"""
        self.root = tk.Tk()
        self.root.title("Gobang Endgame Training System - by Xu Huicong / 五子棋残局训练系统 - 徐慧聪制作")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        
        # 游戏组件
        self.board = Board()
        self.pattern_manager = PatternManager()
        self.validator = MoveValidator(self.pattern_manager, self.board)
        
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
        game_frame = ttk.LabelFrame(main_frame, text="Board / 棋盘", padding="10")
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
        
        ttk.Button(control_frame, text="Select Pattern / 选择棋谱", command=self.show_pattern_selection).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Restart / 重新开始", command=self.restart_pattern).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Undo / 悔棋", command=self.undo_move).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Show Answer / 显示答案", command=self.show_answer).pack(side=tk.LEFT, padx=5)
        
        # 右侧 - 信息区域 / Right side - Information area
        info_frame = ttk.LabelFrame(main_frame, text="Game Info / 游戏信息", padding="10")
        info_frame.grid(row=0, column=1, sticky="nsew")
        
        # 棋谱信息 / Pattern information
        self.pattern_info_var = tk.StringVar(value="Please select an endgame pattern to practice / 请选择残局棋谱进行练习")
        pattern_info_label = ttk.Label(info_frame, textvariable=self.pattern_info_var, font=("Arial", 10, "bold"))
        pattern_info_label.pack(anchor="w", pady=(0, 10))
        
        # 当前状态 / Current status  
        self.status_var = tk.StringVar(value="Please select an endgame pattern / 请选择残局棋谱")
        status_label = ttk.Label(info_frame, textvariable=self.status_var, font=("Arial", 9))
        status_label.pack(anchor="w", pady=(0, 10))
        
        # 步骤信息
        self.step_var = tk.StringVar(value="")
        step_label = ttk.Label(info_frame, textvariable=self.step_var)
        step_label.pack(anchor="w", pady=(0, 10))
        
        # 提示信息区域 / Hint information area
        ttk.Label(info_frame, text="Hints / 提示信息:", font=("Arial", 9, "bold")).pack(anchor="w")
        self.hint_text = scrolledtext.ScrolledText(info_frame, width=40, height=8, wrap=tk.WORD)
        self.hint_text.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        
        # 棋谱分析区域 / Pattern analysis area
        ttk.Label(info_frame, text="Pattern Analysis / 棋谱分析:", font=("Arial", 9, "bold")).pack(anchor="w")
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
            self.add_hint("Position occupied, please choose another one! / 该位置已有棋子，请选择其他位置！")
            return
        
        # 检查是否已选择棋谱 / Check if pattern is selected
        if not self.pattern_manager.current_pattern:
            self.add_hint("Please select an endgame pattern first! / 请先选择一个残局棋谱进行练习！")
            return
        
        # 检查是否轮到玩家 / Check if it's player's turn
        if not self.validator.is_player_turn:
            self.add_hint("Computer's turn, please wait... / 现在轮到电脑下棋，请等待...")
            return
        
        # 验证玩家走法（动态确定玩家颜色）
        result = self.validator.validate_player_move(row, col)
        
        if result['valid']:
            # 玩家走法正确，落子（颜色由验证器中的正确走法确定）
            correct_move = result['correct_move']
            if correct_move:
                self.board.make_move(row, col, correct_move[2])
            
            self.draw_stones()
            self.add_hint(result['message'])
            self.update_status()
            
            if result['pattern_complete']:
                self.show_pattern_analysis()
            elif result['computer_move']:
                # 延迟执行电脑走法，让玩家看到自己的落子
                self.root.after(1000, self.make_computer_move)
        else:
            # 玩家走法错误
            self.add_hint(result['message'])
            
            if result['show_answer']:
                # 3次错误后自动执行正确走法
                self.root.after(2000, self.auto_make_correct_move)
    
    def make_computer_move(self):
        """电脑自动下棋"""
        if not self.validator.is_computer_turn():
            return
        
        result = self.validator.make_computer_move()
        
        if result['move']:
            row, col, player = result['move']
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
            # 动态确定玩家和电脑
            expected_move = self.pattern_manager.get_current_move()
            if expected_move and expected_move[2] == correct_move[2]:
                player_name = "玩家"
            else:
                player_name = "电脑"
            self.add_hint(f"系统演示：{player_name}正确走法 {self._format_move(correct_move)}")
            self.update_status()
            
            # 如果刚才是玩家的走法，现在轮到电脑
            if player_name == "玩家" and self.validator.is_computer_turn():
                self.root.after(1500, self.make_computer_move)
    
    def show_pattern_selection(self):
        """显示棋谱选择对话框"""
        patterns = self.pattern_manager.get_patterns_list()
        
        # 创建选择窗口 / Create selection window
        selection_window = tk.Toplevel(self.root)
        selection_window.title("Select Pattern / 选择棋谱")
        selection_window.geometry("500x350")
        selection_window.transient(self.root)
        selection_window.grab_set()
        
        # 棋谱列表 / Pattern list
        ttk.Label(selection_window, text="Please select an endgame pattern for practice / 请选择要练习的残局棋谱：", font=("Arial", 10, "bold")).pack(pady=10)
        
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
                    messagebox.showerror("Error / 错误", "Failed to load pattern! / 加载棋谱失败！")
        
        button_frame = ttk.Frame(selection_window)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="OK / 确定", command=on_select).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel / 取消", command=selection_window.destroy).pack(side=tk.LEFT, padx=5)
    
    def restart_pattern(self):
        """重新开始当前棋谱 / Restart current pattern"""
        if not self.pattern_manager.current_pattern:
            self.add_hint("Please select a pattern first! / 请先选择一个棋谱！")
            return
        
        self.board.reset()
        self.pattern_manager.reset_pattern()
        self.validator.reset_game()
        
        # 设置残局初始局面
        self.setup_endgame_initial_position()
        
        # 初始化固定的玩家和电脑颜色
        self.validator.initialize_player_colors()
        
        # 显示玩家执子颜色提示
        if self.validator.player_color == 1:
            self.add_hint("Endgame restarted! You use BLACK stones, computer uses WHITE. / 残局重新开始！你执黑子，电脑执白子。")
        else:
            self.add_hint("Endgame restarted! You use WHITE stones, computer uses BLACK. / 残局重新开始！你执白子，电脑执黑子。")
        
        self.draw_board()
        self.update_status()
        self.clear_analysis()
    
    def undo_move(self):
        """悔棋 - 撤销最近的一步或两步（玩家+电脑）"""
        if len(self.board.move_history) == 0:
            self.add_hint("No moves to undo! / 没有可以悔棋的步骤！")
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
                first_move = self.pattern_manager.get_current_move()
                if first_move:
                    self.validator.current_turn = first_move[2]
            self.draw_board()
            self.update_status()
            if len(undone_moves) == 1:
                self.add_hint("Undid one move! / 已悔棋一步！")
            else:
                self.add_hint(f"Undid {len(undone_moves)} moves, back to your turn! / 已悔棋{len(undone_moves)}步，回到你的回合！")
        else:
            self.add_hint("Undo failed! / 悔棋失败！")
    
    def show_answer(self):
        """显示当前步骤的正确答案"""
        if self.validator.is_player_turn:
            expected_move = self.pattern_manager.get_current_move()
            if expected_move:
                row, col, player = expected_move
                if self.validator.is_player_turn:  # 动态判断是否玩家回合
                    self.add_hint(f"Hint: You should play at {self._format_position(row, col)} / 提示：你应该下在 {self._format_position(row, col)}")
                else:
                    self.add_hint("It should be computer's turn now! / 现在应该轮到电脑下棋！")
            else:
                self.add_hint("Pattern completed! / 棋谱已完成！")
        else:
            self.add_hint("Computer's turn, please be patient! / 现在轮到电脑下棋，请耐心等待！")
    
    def update_status(self):
        """更新状态信息"""
        if not self.pattern_manager.current_pattern:
            return
        
        pattern_info = self.pattern_manager.get_pattern_info()
        
        # 更新棋谱信息
        info_text = f"棋谱：{pattern_info['name']} ({pattern_info['difficulty']})"
        self.pattern_info_var.set(info_text)
        
        # 更新步骤信息
        step_text = f"步骤：{pattern_info['current_step']}/{pattern_info['total_moves']}"
        self.step_var.set(step_text)
        
        # 更新当前状态 / Update current status
        if self.pattern_manager.is_pattern_complete():
            self.status_var.set("Pattern completed! / 棋谱完成！")
        else:
            if self.validator.is_player_turn:
                error_info = self.validator.get_error_info()
                # 动态确定玩家颜色
                expected_move = self.pattern_manager.get_current_move()
                if expected_move:
                    player_color = "Black" if expected_move[2] == 1 else "White" 
                    player_color_cn = "黑子" if expected_move[2] == 1 else "白子"
                    status_text = f"Turn: Player({player_color}) | Errors: {error_info['error_count']}/{error_info['max_errors']} / 轮到：玩家({player_color_cn}) | 错误：{error_info['error_count']}/{error_info['max_errors']}"
                else:
                    status_text = "Your turn / 轮到你了"
            else:
                status_text = "Computer's turn | Thinking... / 轮到电脑 | 思考中..."
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
        self.analysis_text.insert(tk.END, f"【Opening Analysis / 开局分析】\n{analysis.get('opening', '')}\n\n")
        self.analysis_text.insert(tk.END, f"【Overall Strategy / 整体策略】\n{analysis.get('strategy', '')}\n\n")
        
        key_points = analysis.get('key_points', [])
        if key_points:
            self.analysis_text.insert(tk.END, "【Key Steps / 关键步骤】\n")
            for point in key_points:
                self.analysis_text.insert(tk.END, f"• {point}\n")
            self.analysis_text.insert(tk.END, "\n")
        
        win_reason = analysis.get('win_reason', '')
        if win_reason:
            self.analysis_text.insert(tk.END, f"【Victory Principle / 胜利原理】\n{win_reason}\n")
        
        self.add_hint("Pattern analysis displayed in right panel! / 棋谱分析已显示在右侧分析区域！")
    
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
        player_name = "黑子" if player == 1 else "白子"
        return f"{player_name} {self._format_position(row, col)}"
    
    def _format_position(self, row, col):
        """格式化位置"""
        col_letter = chr(ord('A') + col)
        row_number = row + 1
        return f"{col_letter}{row_number}"
    
    def run(self):
        """运行游戏"""
        self.root.mainloop()


if __name__ == "__main__":
    game = GameWindow()
    game.run()