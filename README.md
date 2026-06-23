# Programação Orientada a Objetos (POO)

___

## Descrição:

Sistema simulando um _e-commerce_. Desenvolvido na linguagem de programação [Python](https://www.python.org/), utilizando os conceitos básicos da [Programação Orientada a Objetos](https://www.ibm.com/docs/pt-br/ws-and-kc?topic=language-object-oriented-programming). <br>

O projeto visa recriar outro projeto de trabalho final, feito por mim e por um colega de turma, da matéria Estrutura de Dados 1 ([Repositório do trabalho](https://github.com/nbg-cordeiro/Trabalho-ED1)). Esse trabalho foi o desenvolvimento de um sistema de mercado _e-commerce_ pelo terminal do Sistema Operacional.<br>

Nesse projeto, o modelo [MVC](https://pt.wikipedia.org/wiki/MVC) foi utilizado durante seu desenvolvimento.

___

## Estrutura do Projeto

~~~
Projeto/
├── src/
│   ├── data/
│   ├── controller/
│   │   ├── appController.py
│   │   ├── cartController.py
│   │   ├── productController.py
│   │   ├── storeController.py
│   │   └── userController.py
│   ├── models/
│   │   ├── cart.py
│   │   ├── productpy
│   │   └── user.py
│   └── view/
│   │   ├── adminView.py
│   │   ├── authView.py
│   │   ├── cartView.py
│   │   ├── storeView.py
│   │   ├── userView.py
│   │   └── ViewRouter.py
└── main.py
~~~

___

## Como executar:

### 1. Verificando o Python:
Certifique-se que o seu dispositivo tenha o [Python 3.x](https://www.python.org/downloads/) instalado.
Para verificar, digite no terminal do seu Sistema Operacional (PowerShell/Command Prompt no Windows, ou Bash no Linux):
~~~
Python --version
~~~
Caso não tenha instalado, baixe pelo site oficial do [python.org](https://www.python.org/downloads/).

### 2. Clonando os arquivos:
Clone este repositório na sua máquina utilizando o [Git](https://git-scm.com/about).
~~~
git clone https://github.com/EduardoSauber/POO-Project-1.git
~~~

### 3. Acessando os arquivos:
Navegue até a pasta do projeto pelo terminal:
~~~
cd POO-Project-1
~~~

### 4. Executando:
Execute o arquivo `main.py`:
~~~
python main.py
~~~

---

## Funcionalidades:

O programa sempre verifica a existência de, pelo menos, uma conta "admin" ao ser inicializado. Caso ela não tenha (primeira inicialização do sistema), uma conta com ID (CPF) "admin" e senha "admin123" é criada. <br>
Essa conta pode ser alterada futuramente da seguinte forma: <br>
1. acessar o arquivo `./src/controller/data/superuser_accounts.json` pelo seu editor de texto ou IDE de preferência e remover o usuário de CPF "admin" (não pode ser removido diretamente pelo sistema).
2. abrir userController.py pelo seu editor de texto ou IDE de preferência e alterar os dados inseridos no método `check_admins()`).
3. inicializar o programa.
### Menu Autenticação
Permite:
- [x] Login
- [x] Cadastrar novo Usuário
- [x] Sair do sistema

### Menu Clientes
Permite:
- [x] Visualizar lista de Produtos
- [x] Listar Produtos do carrinho
- [x] Adicionar Produto ao carrinho
- [x] Remover Produto do carrinho
- [x] Finalizar Venda
### Menu Super Usuário
Permite:
- [x] Visualizar lista de Produtos
- [x] Visualizar Relatório de Vendas
- Caso Super Usuário tenha permissão 'Admin':
- [x] Gerenciar Administradores
- - [x] Listar Super Usuários
- - [x] Cadastrar Super Usuário
- - [x] Editar Super Usuário
- - [x] Remover Super Usuário
- [x] Gerenciar Clientes
- - [x] Listar Clientes
- - [x] Cadastrar Cliente
- - [x] Editar Cliente
- - [x] Remover Cliente
- [x] Gerenciar Estoque
- - [x] Adicionar Produto
- - [x] Editar Produto
- - [x] Remover Produto

___



