# Programação Orientada a Objetos (POO)


## Estrutura do Projeto
~~~
Projeto/
├── data/
├── src/
│   ├── __init__.py
│   ├── client_System.py
│   ├── persistency.py
│   ├── products_System.py
│   └── store_System.py
├── tools/
│   ├── __init__.py
│   └── test_Mode.py
└── main.py
~~~

## Funcionalidades
~~~
Clientes (client_system):
├── Classe "Cliente".
│   ├── O objeto base para definir o que é o cliente.
│   ├── Possui os dados: CPF, nome e telefone.
│   └── Funções getter e setter para manipulação dos dados do cliente.
├── Funções de manipulação.
│   ├── Cadastrar cliente: cadastra um cliente e insere ele na lista de clientes.
│   ├── Editar cliente: edita os dados de um cliente.
│   ├── Remover cliente: remove um cliente de uma lista.
│   ├── Buscar cliente: busca por um cliente a partir do seu CPF na lista de clientes.
│   ├── Imprimir cliente: imprime as informações de um cliente.
│   └── Listar clientes: imprime todos os os clientes cadastrados na lista de clientes.

Produtos (product_system):

Loja (store_system)
├── Permite que um cliente inclua um produto ao seu carrinho.
│   └── O produto selecionado será "removido" do estoque da loja.
├── Permite que um cliente remova um produto do seu carrinho.
│   └── O produto selecionado será retornado ao estoque da loja.
├── Lista todos os produtos do carrinho de um cliente, informando também o valor total da compra.
├── Finaliza a compra do cliente.
│   └── Esvazia o carrinho do cliente por completo, sem retornar os produtos ao estoque da loja.
~~~
