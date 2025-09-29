import tkinter as tk

window = tk.Tk()
window.title("Teste")
window.geometry("1000x1000+20+20")

lblMsg = tk.Label(window, text="Teste de janela")
lblMsg.pack()

window.mainloop()