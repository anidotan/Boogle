import tkinter as tk
from tkinter import font
from typing import Optional, Tuple, List, Dict, Any
from boogle_theme import *

DEFAULT_TIME = '00:00'


# todo: entry widget, cursor
# todo: do we want a display widget?

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
        self.__time = DEFAULT_TIME
        self.__word_ended = False
        self.__letters = {}
        self.__message = ''
        self.__chosen_words = []
        self.__score = 0

        # build upper frame
        self._upper_frame = tk.Frame(root, bg=BG_COLOR1)
        self._upper_frame.grid(row=0)

        # build lower frame
        self._lower_frame = tk.Frame(root, bg=BG_COLOR2)
        self._lower_frame.grid(row=1)

        # build footer frame
        self._footer = tk.Frame(root, bg=BG_COLOR2)
        self._footer.grid(row=2)

        self.build_top_grid(self._upper_frame)
        self.build_letter_grid(self._lower_frame)
        self.build_bottom_panel(self._footer)

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
                letter = self.create_button(cell, row, col, label, is_letter_button=True)
                letter_loc = (row, col)
                letter.configure(command=lambda: self.set_current_key(letter_loc))
                self.__letters[(row, col)] = letter
        # for loc, letter in self.__letters.items():
        #     # print(loc)
        #     letter.configure(command=lambda: self.set_current_key(loc))
        #     # letter.bind("<Button-1>", lambda loc: self.set_current_key(loc))

    def create_button(self, parent, row, col, label, rowspan: int = 1, columnspan: int = 1, sticky = tk.NSEW, is_letter_button=False) -> tk.Button:
        if is_letter_button:
            cur_key = (row, col)
            button = tk.Button(parent, text=label, command=lambda: self.set_current_key(cur_key), **BUTTON_STYLE)
            button.grid(row=row, column=col, pady=2, padx=2, rowspan=rowspan, columnspan=columnspan, sticky=sticky)
        else:
            button = tk.Button(parent, text=label, **BUTTON_STYLE)
            button.grid(row=row, column=col, pady=2, padx=2, rowspan=rowspan, columnspan=columnspan, sticky=sticky)

        return button

    def get_location_from_button(self, button):
        # tood: imporve this
        pass

    def build_entry_screen(self):
        pass

    def make_GUI(self, board):
        pass

    def build_bottom_panel(self, parent):
        score = tk.Label(parent, text=f'Score: {self.__score}', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                         font=(FONT, 30, 'bold'))
        score.grid(row=0)
        message_box = tk.Label(parent, text=f'Message: {self.__message}', bg=DEFAULT_BG_COLOR, fg=FONT_COLOR,
                                   font=(FONT, 15, 'bold'))
        message_box.grid(row=1)
        end_word = tk.Button(parent, text='END WORD', bg=PRIMARY_BUTTON_COLOR, fg='black', width=10, height=2,
                                 activebackground=BUTTON_PRESSED_COLOR, font=(FONT, 7), command=self.set_word_ended())
        end_word.grid(row=2)

    ######## SETTERS / PROP UPDATES ########
    def color_picked_letters(self, letters_picked: List[Tuple[int, int]]):
        # color the letters on the board + make them unclickable
        for loc in letters_picked:
            self.color_button_by_loc(loc, LETTER_PICKED_COLOR)
            cur_button = self.__letters[loc]
            self.deactivate_button(cur_button)

    def reactivate_buttons(self):
        for button in self.__letters.values():
            if button['state'] != tk.NORMAL:
                self.deactivate_button(button, deactivate=False)
                self.color_button(button, LETTER_COLOR)


        # todo: maybe use this https://www.delftstack.com/howto/python-tkinter/how-to-change-tkinter-button-state/


    def color_possible_letters(self, optional_letters: List[Tuple[int, int]]):
        # color the letters on the board
        for loc in optional_letters:
            self.color_button_by_loc(loc, LETTER_OPTION_COLOR)

    def set_score(self, score: int):
        self.__score = score

    def set_time(self, time: str):
        # get the time, update my timer attribute
        self.__time = time

    def color_button_by_loc(self, button_loc, new_color):
        self.__letters[button_loc].configure(bg=new_color)

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

    def set_current_key(self, key):
        self.__current_key = key
        # print(f'key clicked: {type(self.__current_key)}')


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

    def get_letters(self):
        return self.__letters

    ######## EVENTS ########
    def deactivate_button(self, button: tk.Button, deactivate=True):
        if deactivate:
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL

    def handle_letter_clicked(self, button):
        pass
    """
    # def set_display(self, display_text: str) -> None:
    #     self._word_display_label["text"] = display_text
    """

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
    letters = boggle.get_letters()
    boggle.color_picked_letters([(0,1), (0,0)])
    boggle.color_possible_letters(([(1,1), (3,0)]))
    boggle.run()

    # boggle.set_display("TEST MODE")

    #    use: focus

    "zuk was here! i came to terrorize your code!"