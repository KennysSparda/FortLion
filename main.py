# main.py

import sys
from tkinter import Tk  # Exemplo de importação de biblioteca
from gui.app import Application
from model.database import create_tables  # Importa a função create_tables do database.py

if __name__ == "__main__":
    create_tables()  # Chama a função para criar as tabelas no banco de dados SQLite
    app = Application()
    app.mainloop()