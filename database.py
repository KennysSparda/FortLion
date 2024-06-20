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
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
