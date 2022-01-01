import tkinter as tk

if __name__ == '__main__':
   root = tk.Tk()
   root.title('Welcome to Boogle!')
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

