# gui.py

import tkinter as tk
from tkinter import ttk
from database import create_connection

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestão de Produtos e Estoque")
        self.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        # Frame para entrada de dados do produto
        frame = tk.Frame(self)
        frame.pack(pady=20)
        
        tk.Label(frame, text="Nome:").grid(row=0, column=0)
        self.nome_entry = tk.Entry(frame)
        self.nome_entry.grid(row=0, column=1)
        
        tk.Label(frame, text="Valor Pago:").grid(row=1, column=0)
        self.valor_pago_entry = tk.Entry(frame)
        self.valor_pago_entry.grid(row=1, column=1)
        
        tk.Label(frame, text="Valor Venda:").grid(row=2, column=0)
        self.valor_venda_entry = tk.Entry(frame)
        self.valor_venda_entry.grid(row=2, column=1)
        
        tk.Label(frame, text="Data Entrada:").grid(row=3, column=0)
        self.data_entrada_entry = tk.Entry(frame)
        self.data_entrada_entry.grid(row=3, column=1)
        
        tk.Label(frame, text="Validade:").grid(row=4, column=0)
        self.validade_entry = tk.Entry(frame)
        self.validade_entry.grid(row=4, column=1)
        
        tk.Button(frame, text="Adicionar Produto", command=self.add_product).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Frame para exibição dos produtos
        self.tree = ttk.Treeview(self, columns=("Codigo", "Nome", "Valor_Pago", "Valor_Venda", "Data_Entrada", "Validade"), show='headings')
        self.tree.heading("Codigo", text="Codigo")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Valor_Pago", text="Valor Pago")
        self.tree.heading("Valor_Venda", text="Valor Venda")
        self.tree.heading("Data_Entrada", text="Data Entrada")
        self.tree.heading("Validade", text="Validade")
        
        self.tree.pack(pady=20)
        self.load_products()

    def add_product(self):
        nome = self.nome_entry.get()
        valor_pago = float(self.valor_pago_entry.get())
        valor_venda = float(self.valor_venda_entry.get())
        data_entrada = self.data_entrada_entry.get()
        validade = self.validade_entry.get()
        
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO Produto (Nome, Valor_Pago, Valor_Venda, Data_Entrada, Validade)
        VALUES (?, ?, ?, ?, ?)
        ''', (nome, valor_pago, valor_venda, data_entrada, validade))
        
        conn.commit()
        conn.close()
        
        self.load_products()

    def load_products(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        conn = create_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM Produto')
        rows = cursor.fetchall()
        
        for row in rows:
            self.tree.insert('', 'end', values=row)
        
        conn.close()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
