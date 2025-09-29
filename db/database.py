import sqlite3 as database

con = database.connect("crud.db")

#Criação das tabelas
sql_clientes = '''
    CREATE TABLE IF NOT EXISTS Cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rg VARCHAR (12) NOT NULL,
    nome VARCHAR (100) NOT NULL,
    telefone VARCHAR (12),
    rua VARCHAR (40),
    numero VARCHAR (5),
    bairro VARCHAR (25)
    );
'''

sql_produtos = '''
    CREATE TABLE IF NOT EXISTS Produto (
    ID_Produto INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_Produto VARCHAR (30) NOT NULL,
    Tipo_Produto VARCHAR (25) NOT NULL,
    Preco DECIMAL(10,2) NOT NULL,
    Qtde_Estoque SMALLINT NOT NULL
    );
'''

sql_vendas = '''
    CREATE TABLE IF NOT EXISTS Venda (
    ID_Transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    Nota_Fiscal SMALLINT NOT NULL,
    ID_Cliente INTEGER NOT NULL,
    Data_Compra DATETIME,
    ID_Produto INTEGER NOT NULL,
    Quantidade SMALLINT NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
    FOREIGN KEY (ID_Produto) REFERENCES Produtos(ID_Produto)
    );
'''

try:
    connect = database.connect('')
    cursor = connect.cursor()

    cursor.execute(sql_clientes)
    cursor.execute(sql_produtos)
    cursor.execute(sql_vendas)    

    connect.commit()

except connect.DatabaseError as error:
    print("Erro ao conectar ao banco de dados", error)

finally:
    if(connect):
        connect.close()
