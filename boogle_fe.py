import tkinter as tk
from tkinter import font
from typing import Optional, Tuple, List, Dict, Any, Callable, Set
from boogle_theme import *

DEFAULT_TIME = '00:00'


# todo: entry widget, cursor
# todo: do we want a display widget?
# todo: make ethe colored pressed + letter optional colors


class Boogle_GUI:
    def __init__(self, board):
        self.__board = board
        # build tkinter base
        root = tk.Tk()
        root.title('Welcome to Boogle!')
        root.resizable(False, False)
        self._main_window = root

        # general attributes
        self._letters = {}
        self._buttons = {}

        self.__current_key = None
        self.__word_ended = False

        # build upper frame
        self._upper_frame = tk.Frame(root, bg=BG_COLOR1)
        self._upper_frame.grid(row=0)

        # build middle frame
        self._middle_frame = tk.Frame(root, bg=BG_COLOR2)
        self._middle_frame.grid(row=1)

        # build bottom frame
        self._bottom_frame = tk.Frame(root, bg=BG_COLOR2)
        self._bottom_frame.grid(row=2)

        self.build_top_grid(self._upper_frame)
        self.build_letter_grid(self._middle_frame)
        self.build_side_grid(self._middle_frame)
        self.build_bottom_grid(self._bottom_frame)

    ######## BUILDERS ########
    # todo: do i want to use the self or now? - ASK TOMER
    def build_top_grid(self, parent):
        title = tk.Label(parent, text='Welcome to Boogle!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                         font=(FONT, 30, 'bold'))
        title.grid(row=0)
        secondary_title = tk.Label(parent, text='ARE YOU READY?!', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                   font=(FONT, 15, 'bold'))
        secondary_title.grid(row=1)
        self._start_button = tk.Button(parent, text='START', bg=PRIMARY_BUTTON_COLOR, fg='black', width=6, height=1,
                                 activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 7))
        self._start_button.grid(row=2)
        self._buttons['start_button'] = self._start_button
        self._time = tk.Label(parent, text=DEFAULT_TIME, bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                         font=(FONT, 30, 'bold'))

    def build_letter_grid(self, parent):
        self._board_contrainer = tk.Frame(parent, bg=DEFAULT_BG_COLOR)
        self._board_contrainer.grid(row=0, column=0)
        for row in range(4):
            for col in range(4):
                cell = tk.Frame(self._board_contrainer, bg=DEFAULT_BG_COLOR, width=30, height=30)
                cell.grid(row=row, column=col, padx=5, pady=5)
                label = f'{self.__board[row][col]}'
                letter = self.create_button(cell, row, col, label)
                letter_loc = (row, col)
                self._letters[letter_loc] = letter

    def create_button(self, parent, row, col, label, rowspan: int = 1, columnspan: int = 1,
                      sticky=tk.NSEW) -> tk.Button:
        button = tk.Button(parent, text=label, **BUTTON_STYLE)
        button.grid(row=row, column=col, pady=2, padx=2, rowspan=rowspan, columnspan=columnspan, sticky=sticky)
        return button

    def build_bottom_grid(self, parent):
        # todo: make private + self
        # self._score = tk.Label(parent, text=f'Score:', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
        #                  font=(FONT, 10, 'bold'))
        # self._score.grid(row=0)
        self._message_box = tk.Label(parent, text=f'Message:', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                               font=(FONT, 15, 'bold'))
        self._message_box.grid(row=1)
        self._end_word = tk.Button(parent, text='END WORD', bg=PRIMARY_BUTTON_COLOR, fg='black', width=10, height=2,
                             activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 7))
        self._end_word.grid(row=2)
        self._buttons['end word'] = self._end_word

    def build_side_grid(self, parent):
        self._side_frame = tk.Frame(parent, bg=DEFAULT_BG_COLOR)
        self._side_frame.grid(row=0, column=1)
        self._score = tk.Label(self._side_frame, text=f'Score:', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                               font=(FONT, 20, 'bold'))
        self._score.grid(row=0, column=0)
        self._chosen_words_title = tk.Label(self._side_frame, text='Chosen Words:', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR, font=(FONT, 10, 'bold'))
        self._chosen_words_title.grid(row=1, column=0)
        self._chosen_words = tk.Label(self._side_frame, text='\n\n\n\n\n\n', bg=TEXTBOX_BG_COLOR, fg=FONT_COLOR, font=(FONT, 10, 'bold'))
        self._chosen_words.grid(row=2, column=0)

    ######## SETTERS / PROP UPDATES ########

    def set_button_command(self, button_name: str, cmd: Callable[[], None]) -> None:
        self._buttons[button_name].configure(command=cmd)

    def set_letter_command(self, letter_loc: Tuple[int,int], cmd: Callable[[], None]):
        self._letters[letter_loc].configure(command=cmd)

    def color_picked_letters(self, letters_picked: List[Tuple[int, int]]):
        # color the letters on the board + make them unclickable
        for loc in letters_picked:
            self.color_button_by_loc(loc, LETTER_PICKED_COLOR)
            cur_button = self._letters[loc]
            self.deactivate_button(cur_button)

    def color_and_disable_letters(self, letters_disabled: Set[Tuple[int, int]]):
        # color the letters on the board + make them unclickable
        for loc in letters_disabled:
            self.color_button_by_loc(loc, LETTER_DISABLED_COLOR)
            cur_button = self._letters[loc]
            print(f'type: {type(cur_button)}, {cur_button}')
            self.deactivate_button(cur_button)

    def reactivate_buttons(self):
        for button in self._letters.values():
            if button['state'] != tk.NORMAL:
                self.deactivate_button(button, deactivate=False)
                self.color_button(button, LETTER_COLOR)

        # todo: maybe use this https://www.delftstack.com/howto/python-tkinter/how-to-change-tkinter-button-state/

    def color_possible_letters(self, optional_letters: List[Tuple[int, int]]):
        # color the letters on the board
        for loc in optional_letters:
            self.color_button_by_loc(loc, LETTER_OPTION_COLOR)

    def set_score(self, score: int):
        # self.__score = score
        self._score.configure(text=f'Score: {score}')

    def set_time(self, time: str):
        # get the time, update my timer attribute
        # todo: change the way set score is
        self._time = time

    def color_button_by_loc(self, button_loc, new_color):
        self._letters[button_loc].configure(bg=new_color)

    def color_button(self, button, new_color):
        button.configure(bg=new_color)

    def set_word_ended(self):
        # todo: doesn't change the word on the screen
        # todo: only run when key is pressed. add an event of clicked on button - end
        self.__word_ended = True
    # todo: REMOVE?

    def update_chosen_words(self, words: List[str]):
        # show the chosen words
        words_str = '\n'.join(words)
        self._chosen_words.configure(text=words_str)
    #     todo: update the panel

    def update_message_box(self, message: str):
        # update the message box (error, congrats, etc)
        self._message_box.configure(text=f'Message: {message}')

    def set_current_key(self, key):
        self.__current_key = key
        # print(f'key clicked: {type(self.__current_key)}')
    #     todo: remove this and move it to the logic

    ######## GETTERS #######
    def get_word_ended(self):
        word_ended_flag = False
        if self.__word_ended:
            word_ended_flag = self.__word_ended
            self.__word_ended = False
            self.reactivate_buttons()
        return word_ended_flag
    # todo: move to the logic

    def get_pressed_key(self) -> Optional[Tuple[int, int]]:
        cur_key = self.__current_key
        self.__current_key = None
        return cur_key

    def get_letters(self):
        return self._letters

    def get_letter_loc(self, button):
        for loc,letter in self._letters:
            if letter == button:
                return loc

    ######## EVENTS ########
    def deactivate_button(self, button: tk.Button, deactivate=True):
        if deactivate:
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL

    def run(self) -> None:
        self._main_window.mainloop()

"""
if __name__ == '__main__':
    b1 = [['T', 'H', 'E', 'T'],
          ['O', 'H', 'N', 'D'],
          ['V', 'U', 'F', 'U'],
          ['H', 'O', 'A', 'V']]
    boggle = Boogle_GUI(b1)
    letters = boggle.get_letters()
    # boggle.color_picked_letters([(0,1), (0,0)])
    # boggle.color_possible_letters(([(1,1), (3,0)]))
    boggle.set_score(10)
    boggle.run()

    # boggle.set_display("TEST MODE")

    #    use: focus

    "zuk was here! i came to terrorize your code!"
"""
