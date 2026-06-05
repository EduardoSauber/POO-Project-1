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
- [x] Adicionar Produto ao carrinho
- [ ] Remover Produto do carrinho
- [ ] Finalizar venda (também visualiza todos os itens no carrinho)
### Menu Super Usuário
Permite:
- [x] Visualizar lista de Produtos
- [ ] Ver relatório de Vendas
- Caso Super Usuário seja 'Caixa':
- [ ] Processar venda física
- Caso Super Usuário seja 'Admin':
- [ ] Gerenciar Administradores
- - [ ] Listar Super Usuários
- - [x] Cadastrar Super Usuário
- - - [x] Recebe Nome
- - - [x] Recebe CPF
- - - [x] Recebe E-mail
- - - [x] Recebe Contato telefônico
- - - [x] Recebe Senha
- - - [x] Confirma Senha
- - - [x] Adiciona Permissões ao Super Usuário
- - - [x] Cria conta de Super Usuário com os dados inseridos
- - [ ] Editar Super Usuário
- - [ ] Remover Super Usuário
- [ ] Gerenciar Clientes
- - [ ] Listar Clientes
- - [ ] Cadastrar Cliente
- - [ ] Editar Cliente
- - [ ] Remover Cliente
- [ ] Gerenciar Estoque
- - [ ] Adicionar Produto
- - [ ] Editar Produto
- - [ ] Remover Produto

___

## Requisitos técnicos


