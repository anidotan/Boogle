import tkinter as tk

BUTTON_HOVER_COLOR = 'gray'
DEFAULT_COLOR = "#4A7A8C"
PRESSED_COLOR = 'slateblue'


class Boogle_GUI:
    def __init__(self, board=None):
        root = tk.Tk()
        root.title('Welcome to Boogle!')
        root.resizable(False, False)
        self._main_window = root
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

    def set_display(self, display_text: str) -> None:
        self._word_display_label["text"] = display_text

    def run(self) -> None:
        self._main_window.mainloop()


if __name__ == '__main__':
    boggle = Boogle_GUI()
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

