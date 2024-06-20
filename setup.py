import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["sqlite3", "tkinter"],
    "include_files": [
        ("model/gerencial.db", "model/gerencial.db")  # Inclui o arquivo do banco de dados
    ],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Para ocultar a janela de console no Windows

setup(
    name="FortiLion",
    version="1.0",
    description="Gerenciador de estoque em desenvolvimento !!",
    options={
        "build_exe": build_exe_options,
    },
    executables=[
        Executable("main.py", base=base, icon="favicon.ico")  # Arquivo principal e ícone
    ],

)
