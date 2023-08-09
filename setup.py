from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="Balanca",
    version="1.0",
    description="webhook para envio de dados",
    executables=executables
)
