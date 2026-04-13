########################################################################################################################
# IMPORT


########################################################################################################################
# CLASSES
class Cliente:
    def __init__(self,cpf:str,nome:str,telefone:str):
        self._cpf = ""                  # 123.456.789.xx
        self._nome = ""                 # tralaleiro da silva junior
        self._telefone = ""             # +55 (ddd) 9 1234-5678
        self.carrinho  = []             # lista de compras do cliente

        self.set_cpf(cpf)
        self.set_nome(nome)
        self.set_telefone(telefone)

    def get_cpf(self) -> str:
        return self._cpf
    def set_cpf(self,value:str) -> None:
        if not isinstance(value,str):
            raise TypeError("O valor inserido deve ser uma string!")
        entrada = value.strip()
        if entrada != "":
            entrada.replace(".","").replace("_","")
            self._cpf = entrada
        else:
            raise ValueError("Entrada de dado inválido!")

    def get_nome(self) -> str:
        return self._nome
    def set_nome(self,value:str) -> None:
        if not isinstance(value,str):
            raise TypeError("O valor inserido deve ser uma string!")
        entrada = value.strip()
        if entrada != "":
            entrada.upper()
            self._nome = entrada
        else:
            raise ValueError("Entrada de dado inválido!")

    def get_telefone(self) -> str:
        return self._telefone
    def set_telefone(self,value:str) -> None:
        if not isinstance(value,str):
            TypeError("O valor inserido deve ser uma string!")
        entrada = value.strip()
        if entrada != "":
            entrada.replace("+","").replace(" ","").replace("-","")
            self._telefone = entrada

########################################################################################################################
# FUNCOES
def cadastrar_cliente():
    print("\n")
    print(f"=== {'CADASTRAR CLIENTE':^30} ===")
    print("-" * 38)


def editar_cliente():
    print("\n")
    print(f"=== {'EDITAR CLIENTE':^30} ===")
    print("-" * 38)


def remover_cliente():
    print("\n")
    print(f"=== {'REMOVER CLIENTE':^30} ===")
    print("-" * 38)


def buscar_cliente():
    print("\n")
    print(f"=== {'BUSCAR CLIENTE':^30} ===")
    print("-" * 38)


def imprimir_cliente(cliente : Cliente):
    temp_nome = cliente.get_nome()
    temp_cpf = cliente.get_cpf()
    temp_telefone = cliente.get_telefone()

    print(f"Nome: {temp_nome}\nCPF: {temp_cpf}\nTelefone: {temp_telefone}")

def listar_clientes(listaClientes : list['Cliente']) -> None:
    print("\n")
    print(f"=== {'LISTA DE CLIENTES':^30} ===")
    print("-"*38)

    for index,client in enumerate(listaClientes,start=1):
        print(f"[ Cliente {index} ]")
        imprimir_cliente(client)
        print("-"*38)

########################################################################################################################
# TEST_BENCH
def workspace():
    print("-- Rodando modo teste em client_system --")

    clientes_teste = [] # SIMULANDO LISTA DE CLIENTES DA MAIN

    ####################################################################################################################
    # TESTE DE CADASTRO
    dado1 = str(input("CPF: "))
    dado2 = str(input("NOME: "))
    dado3 = str(input("TELEFONE: "))
    cliente1_teste = Cliente(dado1,dado2,dado3)
    clientes_teste.append(cliente1_teste)
    for attr,value in vars(cliente1_teste).items():
        print(f"{attr} : {value}")
    ####################################################################################################################
    # TESTE DE LISTAGEM
    cliente2_teste = Cliente("12345678912","TESTUDO DA SILVA TESTE","5561912345678")
    cliente3_teste = Cliente("21987654321","ROBERNILSON TESTADO","5562987654321")
    clientes_teste.append(cliente2_teste)
    clientes_teste.append(cliente3_teste)

    listar_clientes(clientes_teste)
    ####################################################################################################################
    # TESTE DE EDICAO DE DADOS


if __name__ == "__main__":
    workspace()