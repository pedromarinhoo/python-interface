import tkinter as tk

# configurando a janela principal
window = tk.Tk()
window.title("CRUD em Python + Tkinter")
window.geometry("2000x2000")
window.configure(bg="#000")
window.attributes('-zoomed', True)

# dividindo os frames da aplicação
upperFrame = tk.Frame(window, width=400, height=50, bg="#338BF2", relief="flat")
upperFrame.grid(row=0, column=0)

bottomFrame = tk.Frame(window, width=400, height=2000, bg="#FFFFFF")
bottomFrame.grid(row=1, column=0, sticky=tk.NSEW, padx=0, pady=1)

rightFrame = tk.Frame(window, width=1000, height=1000, bg="#FFFFFF", relief="flat")
rightFrame.grid(row=0, column=1, sticky=tk.NSEW, padx=1, pady=1)



lblMsg = tk.Label(window, text="CRUDs em Python")

window.mainloop()