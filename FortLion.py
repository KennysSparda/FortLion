import subprocess
import sys
import os

def install_dependencies():
    # Instalar dependências usando o pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def initialize_database():
    # Inicializar o banco de dados executando database.py
    subprocess.check_call([sys.executable, "database.py"])

def run_main_script():
    # Executar o main.py após instalar dependências e inicializar o banco de dados
    subprocess.check_call([sys.executable, "main.py"])

if __name__ == "__main__":
    # Instalar dependências e inicializar banco de dados
    install_dependencies()
    initialize_database()

# Executar o script principal
run_main_script()
