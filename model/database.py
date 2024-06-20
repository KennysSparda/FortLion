# database.py

import sqlite3

def create_connection():
    return sqlite3.connect('gerencial.db')

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produto (
        Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Valor_Pago REAL NOT NULL,
        Valor_Venda REAL NOT NULL,
        Data_Entrada TEXT NOT NULL,
        Validade TEXT
    )
    ''')
    print("Tabela Produto criada")
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estoque (
        Codigo_Produto_FK INTEGER NOT NULL,
        Quantidade_Entrada INTEGER NOT NULL,
        Quantidade_Saida INTEGER NOT NULL,
        Quantidade_Atual INTEGER NOT NULL,
        Data_Registro TEXT NOT NULL,
        FOREIGN KEY (Codigo_Produto_FK) REFERENCES Produto (Codigo)
    )
    ''')
    print("Tabela Estoque criada")
    
    conn.commit()
    conn.close()

def add_product(nome, valor_pago, valor_venda, data_entrada, validade):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO Produto (Nome, Valor_Pago, Valor_Venda, Data_Entrada, Validade)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, valor_pago, valor_venda, data_entrada, validade))
    
    conn.commit()
    conn.close()

def get_products():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM Produto')
    rows = cursor.fetchall()
    
    conn.close()
    return rows

if __name__ == "__main__":
    create_tables()

def update_product(codigo, nome, valor_pago, valor_venda, data_entrada, validade):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE Produto
    SET Nome=?, Valor_Pago=?, Valor_Venda=?, Data_Entrada=?, Validade=?
    WHERE Codigo=?
    ''', (nome, valor_pago, valor_venda, data_entrada, validade, codigo))
    
    conn.commit()
    conn.close()