import tkinter as tk
from tkinter import font
from typing import Optional, Tuple, List, Dict, Any
from boogle_theme import *

DEFAULT_TIME = '00:00'


# todo: add cute cursor
# todo: check if i am mixing grid and pack
# todo: enry widgeet

class Boogle_GUI:
    def __init__(self, board):
        self.__board = board
        # build tkinter base
        root = tk.Tk()
        root.title('Welcome to Boogle!')
        root.resizable(False, False)
        self._main_window = root

        # general attributes
        self.__current_key = None
        self.time = DEFAULT_TIME
        self.__word_ended = False
        self.__letters = {}

        # build upper frame
        self._upper_frame = tk.Frame(root, bg=BG_COLOR1)
        self._upper_frame.grid(row=0)

        # build lower frame
        self._lower_frame = tk.Frame(root, bg=BG_COLOR2)
        self._lower_frame.grid(row=1)

        self.build_top_grid(self._upper_frame)
        self.build_letter_grid(self._lower_frame)

    ######## BUILDERS ########
    # todo: do i want to use the self or now? - ASK TOMER
    def build_top_grid(self, parent):
        top_frame = tk.Frame(parent)
        top_frame.grid(row=0)
        title = tk.Label(top_frame, text='Welcome to Boogle!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                         font=(FONT, 30, 'bold'))
        title.grid(row=0)
        secondary_title = tk.Label(top_frame, text='ARE YOU READY?!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                   font=(FONT, 15, 'bold'))
        secondary_title.grid(row=1)
        start_button = tk.Button(top_frame, text='START', bg=PRIMARY_BUTTON_COLOR, fg='black', width=6, height=1,
                                 activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 7))
        start_button.grid(row=2)

    def build_letter_grid(self, parent):
        board_contrainer = tk.Frame(parent, bg=DEFAULT_BG_COLOR)
        board_contrainer.grid(row=0)
        for row in range(4):
            for col in range(4):
                cell = tk.Frame(board_contrainer, bg=DEFAULT_BG_COLOR, width=30, height=30)
                cell.grid(row=row, column=col, padx=5, pady=5)
                label = f'{self.__board[row][col]}'
                letter = self.create_button(cell, row, col, label)
                self.__letters[(row, col)] = letter

    def create_button(self, parent, row, col, label, rowspan: int = 1, columnspan: int = 1) -> tk.Button:
        button = tk.Button(parent, text=label, **BUTTON_STYLE)
        button.grid(row=row, column=col, pady=2, padx=2, sticky=tk.NSEW)

        def _on_enter(event: Any) -> None:
            button['background'] = BUTTON_HOVER_COLOR

        def _on_leave(event: Any) -> None:
            button['background'] = PRIMARY_BUTTON_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)

        return button

    def build_entry_screen(self):
        pass

    def make_GUI(self, board):
        pass


    ######## SETTERS ########
    def color_picked_letters(self, letters_picked: List[Tuple[int, int]]):
        # color the letters on the board + make them unclickable
        for loc in letters_picked:
            cur_letter = self.__letters[loc]
            self.color_button(cur_letter, LETTER_PICKED_COLOR)
            self.deactivate_button(cur_letter)


    def reactivate_buttons(self):
        for button in self.__letters.values():
            if button.get('state') != tk.NORMAL:
                self.deactivate_button(button, deactivate=False)
        # todo: test this
        # todo: maybe use this https://www.delftstack.com/howto/python-tkinter/how-to-change-tkinter-button-state/

    def color_possible_letters(self, optional_letters: List[Tuple[int, int]]):
        # color the letters on the board
        for loc in optional_letters:
            cur_letter = self.__letters[loc]
            self.color_button(cur_letter, LETTER_OPTION_COLOR)

    def set_score(self, score: int):
        self.__score = score

    def set_time(self, time: str):
        # get the time, update my timer attribute
        self.__time = time

    def color_button(self, button, new_color):
        button.configure(bg=new_color)

    def set_word_ended(self):
        # todo: make it
        # todo: only run when key is pressed. add an event of clicked on button - end
        self.__word_ended = True


    def update_chosen_words(self, words: List[str]):
        # show the chosen words
        self.__chosen_words = words

    def update_message_box(self, message: str):
        # update the message box (error, congrats, etc)
        self.__message = message
        pass

    def set_pressed_key(self):
        # todo: make private
        """
        event - get the key that is pressed now and set it in the init.
        :return:
        """



    ######## GETTERS #######
    def get_word_ended(self):
        word_ended_flag = False
        if self.__word_ended:
            word_ended_flag = self.__word_ended
            self.__word_ended = False
        return word_ended_flag


    def get_pressed_key(self) -> Optional[Tuple[int, int]]:
        cur_key = self.__current_key
        self.__current_key = None
        return cur_key



    ######## EVENTS ########
    def deactivate_button(self, button: tk.Button, deactivate=True):
        if deactivate:
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL



    # def set_display(self, display_text: str) -> None:
    #     self._word_display_label["text"] = display_text

    def run(self) -> None:
        self._main_window.mainloop()

    def build_exit_screen(self):
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

    #    use: focus
