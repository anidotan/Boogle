import tkinter as tk
from tkinter import font
from typing import Optional, Tuple, List, Dict

DEFAULT_BG_COLOR = 'White'
BG_COLOR1 = 'mint cream'
BG_COLOR2 = 'alice blue'
PRIMARY_BUTTON_COLOR = 'LightSkyBlue1'
SECONDARY_BUTTON_COLOR = 'LightSkyBlue3'
BUTTON_HOVER_COLOR = 'snow'
# BUTTON_PRESSED_COLOR = 'lavender blush'
BUTTON_PRESSED_COLOR = 'snow'
OTHER = ['LightSkyBlue', 'LightSkyBlue1', 'LightSkyBlue2', 'SkyBlue']
DEFAULT_BORDER = 'ROYALBLUE4'
FONT_COLOR = 'black'
FONT = 'Segoe UI Semilight'


# ACTIVE_FG_COLOR = 'LightSkyBlue'
# HIGHTLIGHT_COLOR = ''

        # todo: add cute cursor
        # todo: check if i am mixing grid and pack

class Boogle_GUI:
    def __init__(self, board):
        self.__board = board
        # build tkinter base
        root = tk.Tk()
        root.title('Welcome to Boogle!')
        root.resizable(False, False)
        self._main_window = root

        # genral attributes
        self.__current_key = None

        # build upper frame
        self._upper_frame = tk.Frame(root, bg=BG_COLOR1)
        self._upper_frame.grid(row=0)
        # self._upper_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # build lower frame
        self._lower_frame = tk.Frame(root, bg=BG_COLOR2)
        self._lower_frame.grid(row=1)
        # self._lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.build_top_grid(self._upper_frame)
        self.build_letter_grid(self._lower_frame)

    def build_footer(self):
        pass

    def build_top_grid(self, parent):
        top_frame = tk.Frame(parent)
        top_frame.grid(row=0)
        title = tk.Label(top_frame, text='Welcome to Boogle!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR, font=(FONT, 30, 'bold'))
        title.grid(row=0)
        secondary_title = tk.Label(top_frame, text='ARE YOU READY?!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR, font=(FONT, 15, 'bold'))
        secondary_title.grid(row=1)
        start_button = tk.Button(top_frame, text='START', bg=PRIMARY_BUTTON_COLOR, fg='black', width=6, height=1, activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 7))
        start_button.grid(row=2)
        print('added top grid')

    def build_letter_grid(self, parent):
        # for col in range(4):
        #     # todo: do i want to change this to self
        #     tk.Grid.columnconfigure(parent, col, weight=1)    # type: ignore
        #
        # for row in range(4):
        #     # todo: do i want to change this to self
        #     tk.Grid.rowconfigure(parent, row, weight=1)    # type: ignore
        board_contrainer = tk.Frame(parent, bg=DEFAULT_BG_COLOR)
        board_contrainer.grid(row=0)

        for row in range(4):
            for col in range(4):
                cell = tk.Frame(board_contrainer, bg=DEFAULT_BG_COLOR, width=30, height=30)
                cell.grid(row=row, column=col, padx=5, pady=5)
                button = tk.Button(cell, text=f'{self.__board[row][col]}', bg=PRIMARY_BUTTON_COLOR, width=4, height=1,
                                   activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 10))
                button.grid(row=row, column=col, pady=2, padx=2, sticky=tk.NSEW)

    def color_letters(self, letters_picked: List[Tuple[int,int]], optional_letters: List[Tuple[int,int]]):
        # todo: maybe separate this
        pass

    def show_time(self, time: str):
        pass

    def show_chosen_words(self):
        pass

    def update_message_box(self):
        pass

    def cur_pressed_key(self) -> Optional[Tuple[int,int]]:
        cur_key = self.__current_key
        self.__current_key = None
        return cur_key

    def get_pressed_key(self):
        """
        event - get the key that is pressed now and set it in the init.
        :return:
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
