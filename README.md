# Programação Orientada a Objetos (POO)

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

## Descrição

___

## Funcionalidades

### Menu Autenticação
Permite:
- [x] Login
- [x] Cadastrar novo Usuário (signin)
- - [x] Recebe Nome
- - [x] Recebe CPF
- - [x] Recebe E-mail
- - [x] Recebe Contato telefônico
- - [x] Recebe Senha
- - [x] Confirma Senha
- - [x] Cria conta de Usuário com os dados inseridos
- [x] Sair do sistema

### Menu Clientes
Permite:
- [x] Visualizar lista de Produtos
- [x] Listar Produtos do carrinho
- [x] Adicionar Produto ao carrinho
- [x] Remover Produto do carrinho
- [ ] Finalizar Venda
### Menu Super Usuário
Permite:
- [x] Visualizar lista de Produtos
- [ ] Visualizar Relatório de Vendas
- Caso Super Usuário seja 'Admin':
- [x] Gerenciar Administradores
- - [x] Listar Super Usuários
- - [x] Cadastrar Super Usuário
- - - [x] Recebe Nome
- - - [x] Recebe CPF
- - - [x] Recebe E-mail
- - - [x] Recebe Contato telefônico
- - - [x] Recebe Senha
- - - [x] Confirma Senha
- - - [x] Adiciona Permissões ao Super Usuário
- - - [x] Cria conta de Super Usuário com os dados inseridos
- - [x] Editar Super Usuário
- - [x] Remover Super Usuário
- [x] Gerenciar Clientes
- - [x] Listar Clientes
- - [x] Cadastrar Cliente (Redundante com "Cadastrar Super Usuário".)
- - [x] Editar Cliente (Redundante com "Editar Super Usuário".)
- - [x] Remover Cliente
- [x] Gerenciar Estoque
- - [x] Adicionar Produto
- - [x] Editar Produto
- - [x] Remover Produto

___

## Requisitos técnicos


