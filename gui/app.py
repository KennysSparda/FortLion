# gui/app.py

import tkinter as tk
from gui.product_frame import ProductFrame

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestão de Produtos e Estoque")
        self.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        # Adicionando o frame de produtos
        product_frame = ProductFrame(self)
        product_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
