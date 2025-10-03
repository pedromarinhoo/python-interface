import tkinter as tk
from tkinter import ttk, messagebox
from db.database import criarTabela, inserirCliente, listarClientes, atualizarCliente, excluirCliente

# Criar tabela se não existir
criarTabela()

def inserir():
    nome = entry_nome.get()
    telefone = entry_telefone.get()

    if not nome:
        messagebox.showwarning("Atenção", "O campo Nome é obrigatório")
        return
    
    inserirCliente(nome, telefone)
    listar()
    limparCampos()

def listar():
    for item in tree.get_children():
        tree.delete(item)
    for row in listarClientes():
        tree.insert("", tk.END, values=row)

def excluir():
    item = tree.selection()
    if not item:
        messagebox.showwarning("Atenção", "Selecione um registro para excluir")
        return
    id_cliente = tree.item(item, "values")[0]
    excluirCliente(id_cliente)
    listar()

def limparCampos():
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

window = tk.Tk()
window.title("CRUD Clientes")

# Labels e Entrys
tk.Label(window, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(window); entry_nome.grid(row=0, column=1)

tk.Label(window, text="Telefone").grid(row=1, column=0)
entry_telefone = tk.Entry(window); entry_telefone.grid(row=1, column=1)

# Botões coloridos
tk.Button(window, text="Inserir", command=inserir, bg="green", fg="white").grid(row=2, column=0, pady=5)
tk.Button(window, text="Excluir", command=excluir, bg="red", fg="white").grid(row=2, column=2, pady=5)
tk.Button(window, text="Listar", command=listar, bg="orange", fg="black").grid(row=2, column=3, pady=5)

# Treeview
tree = ttk.Treeview(window, columns=("ID","Nome","Telefone"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Telefone", text="Telefone")
tree.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

listar()

window.mainloop()
