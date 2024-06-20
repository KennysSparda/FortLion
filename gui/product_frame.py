import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.database import create_connection, add_product, get_products, update_product

class ProductFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.load_products()

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
        tk.Button(frame, text="Atualizar Produto", command=self.update_product).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(frame, text="Excluir Produto", command=self.delete_product).grid(row=7, column=0, columnspan=2, pady=10)
        
        # Frame para exibição dos produtos
        self.tree = ttk.Treeview(self, columns=("Codigo", "Nome", "Valor_Pago", "Valor_Venda", "Data_Entrada", "Validade"), show='headings')
        self.tree.heading("Codigo", text="Codigo", command=lambda: self.sort_column("Codigo", False))
        self.tree.heading("Nome", text="Nome", command=lambda: self.sort_column("Nome", False))
        self.tree.heading("Valor_Pago", text="Valor Pago", command=lambda: self.sort_column("Valor_Pago", True))
        self.tree.heading("Valor_Venda", text="Valor Venda", command=lambda: self.sort_column("Valor_Venda", True))
        self.tree.heading("Data_Entrada", text="Data Entrada", command=lambda: self.sort_column("Data_Entrada", False))
        self.tree.heading("Validade", text="Validade", command=lambda: self.sort_column("Validade", False))
        
        self.tree.pack(pady=20)

        self.tree.bind("<ButtonRelease-1>", self.select_product)
      
    def select_product(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            self.nome_entry.delete(0, tk.END)
            self.valor_pago_entry.delete(0, tk.END)
            self.valor_venda_entry.delete(0, tk.END)
            self.data_entrada_entry.delete(0, tk.END)
            self.validade_entry.delete(0, tk.END)
            
            self.nome_entry.insert(0, values[1])
            self.valor_pago_entry.insert(0, values[2])
            self.valor_venda_entry.insert(0, values[3])
            self.data_entrada_entry.insert(0, values[4])
            self.validade_entry.insert(0, values[5])
        
    def add_product(self):
        nome = self.nome_entry.get()
        valor_pago_str = self.valor_pago_entry.get()
        valor_venda_str = self.valor_venda_entry.get()
        data_entrada = self.data_entrada_entry.get()
        validade = self.validade_entry.get()
        
        if not nome or not valor_pago_str or not valor_venda_str:
            messagebox.showwarning("Campos Vazios", "Preencha todos os campos obrigatórios.")
            return
        
        try:
            valor_pago = float(valor_pago_str)
            valor_venda = float(valor_venda_str)
        except ValueError:
            messagebox.showerror("Erro de Valor", "Valor Pago e Valor Venda devem ser números válidos.")
            return
        
        add_product(nome, valor_pago, valor_venda, data_entrada, validade)
        self.load_products()

    def update_product(self):
        selected_item = self.tree.focus()
        if selected_item:
            codigo = self.tree.item(selected_item, "values")[0]
            nome = self.nome_entry.get()
            valor_pago = float(self.valor_pago_entry.get() or 0)
            valor_venda = float(self.valor_venda_entry.get() or 0)
            data_entrada = self.data_entrada_entry.get()
            validade = self.validade_entry.get()
            
            update_product(codigo, nome, valor_pago, valor_venda, data_entrada, validade)
            self.load_products()
            self.clear_entries()
        else:
            messagebox.showwarning("Seleção Necessária", "Selecione um produto para atualizar.")
    
    def delete_product(self):
        selected_item = self.tree.focus()
        if selected_item:
            codigo = self.tree.item(selected_item, "values")[0]
            
            conn = create_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM Produto WHERE Codigo=?', (codigo,))
            
            conn.commit()
            conn.close()
            
            self.load_products()
            self.clear_entries()
        else:
            messagebox.showwarning("Seleção Necessária", "Selecione um produto para excluir.")
    
    def load_products(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        rows = get_products()
        for row in rows:
            self.tree.insert('', 'end', values=row)
    
    def sort_column(self, col, reverse):
        items = self.tree.get_children('')
        data = [(self.tree.set(item, col), item) for item in items]
        data.sort(reverse=reverse)
        
        for index, (val, item) in enumerate(data):
            self.tree.move(item, '', index)
    
    def clear_entries(self):
        self.nome_entry.delete(0, tk.END)
        self.valor_pago_entry.delete(0, tk.END)
        self.valor_venda_entry.delete(0, tk.END)
        self.data_entrada_entry.delete(0, tk.END)
        self.validade_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductFrame(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
