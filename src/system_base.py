########################################################################################################################
# IMPORT

########################################################################################################################
# FUNCOES
def limpar_terminal():
    # subprocess.run(('cls' if os.name == 'nt' else 'clear'), shell=True)
    print('\033[H\033[J', end='')

def criar_titulo(titulo:str,final:bool):
    t_size = 19 - (len(titulo)/2)
    if final:
        print("-" * (t_size*2 + len(titulo) + 2))
    else:
        print("=" * t_size, titulo, "=" * t_size)
        print("-" * (t_size*2 + len(titulo) + 2))

########################################################################################################################
# TESTBENCH
def workspace():
    limpar_terminal()

if __name__ == "__main__":
    workspace()