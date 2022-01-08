import tkinter as tk
from tkinter import font

DEFAULT_BG_COLOR = 'White'
BG_COLOR1 = 'mint cream'
BG_COLOR2 = 'alice blue'
PRIMARY_BUTTON_COLOR = 'LightSkyBlue1'
SECONDARY_BUTTON_COLOR = 'LightSkyBlue3'
BUTTON_HOVER_COLOR = 'snow'
BUTTON_PRESSED_COLOR = 'lavender blush'
OTHER = ['LightSkyBlue', 'LightSkyBlue1', 'LightSkyBlue2', 'SkyBlue']
DEFAULT_BORDER = 'ROYALBLUE4'
FONT_COLOR = 'black'
FONT = 'Segoe UI Semilight'
# ACTIVE_FG_COLOR = 'LightSkyBlue'
# HIGHTLIGHT_COLOR = ''


class Boogle_GUI:
    def __init__(self, board=None):
        self.board = board
        # todo: add cute cursor

        # build tkinter base
        root = tk.Tk()
        root.title('Welcome to Boogle!')
        root.resizable(False, False)
        self._main_window = root

        # build outer frame
        self._outer_frame = tk.Frame(root, bg=DEFAULT_BG_COLOR)
        self._outer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # build upper frame
        self._upper_frame = tk.Frame(self._outer_frame, bg=BG_COLOR1)
        self._upper_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        test_top = tk.Label(self._upper_frame, text='upper_frame', height=25, width=25, bg='red')
        # test_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        test_top.pack(side=tk.TOP)

        # build lower frame
        self._lower_frame = tk.Frame(self._outer_frame, bg=BG_COLOR2)
        self._lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        test_bottom = tk.Label(self._lower_frame, text='lower_frame', height=25, width=25, bg='black')
        # test_bottom.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        test_bottom.pack(side=tk.TOP)

        # self.build_top_grid(root)
        # self.build_letter_grid(bottom_frame)

    def build_top_grid(self, parent):
        top_frame = tk.Frame(parent, bg='White', height=5)
        top_frame.grid(row=0)
        title = tk.Label(top_frame, text='Welcome to Boogle!', fg='MidnightBlue', font=('Segoe UI Semilight', 30, 'bold'))
        title.grid(row=0)

    def build_letter_grid(self, root):
        for row in range(4):
            for col in range(4):
                cell = tk.Frame(root, bg='White', width=30, height=30)
                cell.grid(row=row, column=col, padx=5, pady=5)
                button = tk.Button(text=f'{self.board[row][col]}', bg=DEFAULT_COLOR, width=4, height=1, activebackground=PRESSED_COLOR, font=('Segoe UI Semilight', 20, 'bold'))
                button.grid(row=row, column=col, pady=2, padx=2)

        """
        # outer frame
        self._outer_frame = tk.Frame(root, bg='black', highlightthickness= 5)
        self._outer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # upper frame - timer, word display, score
        self._upper_frame = tk.Frame(self._outer_frame, height=5, width=10, bg='yellow')
        self._upper_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # word display box
        self._word_display_label = tk.Label(self._upper_frame, text='Yo Zuk', bg='skyblue', font=('Courier', 30))
        self._word_display_label.pack(side=tk.RIGHT)

        self._lower_frame = tk.Frame(self._outer_frame, height=10, width=10, bg='black')
        self._lower_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        """

    def build_outer_frame(self):
        pass

    def build_entry_screen(self):
        pass

    def make_GUI(self, board):
        pass

    def handle_word(self):
        pass

    # def set_display(self, display_text: str) -> None:
    #     self._word_display_label["text"] = display_text

    def run(self) -> None:
        self._main_window.mainloop()

    def build_footer(self):
        pass

    def build_finish_screen(self):
        pass

    def build_timer(self):
        pass

    def build_message_box(self):
        pass


if __name__ == '__main__':

    b1 = [['T', 'H', 'E', 'T'],
          ['O', 'H', 'N', 'D'],
          ['V', 'U', 'F', 'U'],
          ['H', 'O', 'A', 'V']]
    boggle = Boogle_GUI(b1)
    # boggle.set_display("TEST MODE")
    boggle.run()


    """
       for i in range(16):
          current_row = i // 4
          current_col = i % 4
          button = tk.Button(
             text=f'{i}',
             width=5,
             height=2,
             bg="#4A7A8C",
             fg="white")
          button.grid(row=current_row, column=current_col)
       root.mainloop()
    
    #    use: focus
    
    """

