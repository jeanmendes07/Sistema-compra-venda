# Sistema de Estoque e Vendas

## Descrição

Este projeto consiste em um sistema de linha de comando desenvolvido em Python para gerenciamento de produtos, controle de estoque e registro de vendas.

O sistema permite cadastrar, editar, remover e consultar produtos, além de registrar vendas e gerar relatórios de estoque.

Os dados são armazenados em um arquivo JSON, garantindo persistência entre diferentes execuções do programa.

---

# Como Executar

## Requisitos

- Python 3.10 ou superior

## Executando o sistema

Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

Ao iniciar, o sistema carregará automaticamente os produtos armazenados no arquivo:

```text
dados.json
```

Caso o arquivo não exista ou esteja vazio, o sistema iniciará sem produtos cadastrados.

---

# Utilizando o Menu

Ao iniciar o programa, será exibido o menu principal:

```text
============================================================
                 SISTEMA DE ESTOQUE E VENDAS
============================================================

[1] Cadastrar Produto
[2] Editar Produto
[3] Remover Produto

---------------- BUSCAS ----------------

[4] Buscar por Código
[5] Buscar por Nome

---------------- VENDAS ----------------

[6] Registrar Venda

-------------- RELATÓRIOS --------------

[7] Estoque Geral
[8] Produtos por Categoria
[9] Estoque Baixo

--------------- SISTEMA ----------------

[0] Salvar e Sair
============================================================
```

---

## 1 - Cadastrar Produto

Permite cadastrar um novo produto.

Informações solicitadas:

- Código
- Nome
- Categoria
- Preço
- Quantidade

Exemplo:

```text
Código: 1001
Nome: Mouse Gamer
Categoria: Periféricos
Preço: 89.90
Quantidade: 15
```

### Regras

- O código deve ser único.
- O preço deve ser maior que zero.
- A quantidade não pode ser negativa.

---

## 2 - Editar Produto

Permite alterar os dados de um produto já existente.

Informações solicitadas:

- Código do produto
- Novo nome
- Nova categoria
- Novo preço
- Nova quantidade

Caso o código não exista, será exibida uma mensagem informando que o produto não foi encontrado.

---

## 3 - Remover Produto

Permite excluir um produto utilizando seu código.

Exemplo:

```text
Código do produto: 1001
```

Se o produto existir, ele será removido do sistema.

---

## 4 - Buscar por Código

Realiza uma busca utilizando o código do produto.

Exemplo:

```text
Código: 1001
```

O sistema exibirá todas as informações do produto encontrado.

Esta operação utiliza busca binária.

---

## 5 - Buscar por Nome

Permite localizar produtos através do nome.

Exemplo:

```text
Nome: Mouse
```

O sistema exibirá todos os produtos que contenham o texto informado.

Esta operação utiliza busca linear.

---

## 6 - Registrar Venda

Permite registrar a venda de um produto.

Informações solicitadas:

```text
Código do produto
Quantidade vendida
```

Exemplo:

```text
Código do produto: 1001
Quantidade vendida: 2
```

O estoque será reduzido automaticamente.

### Regras

- Não é possível vender mais unidades do que existem em estoque.
- O produto deve existir.

---

## 7 - Estoque Geral

Exibe todos os produtos cadastrados no sistema.

Os produtos são apresentados em ordem crescente de código.

---

## 8 - Produtos por Categoria

Exibe somente os produtos pertencentes a uma categoria específica.

Exemplo:

```text
Categoria: Periféricos
```

---

## 9 - Estoque Baixo

Exibe os produtos com quantidade inferior ao limite informado.

Exemplo:

```text
Limite de estoque: 5
```

O sistema mostrará todos os produtos cuja quantidade seja menor que 5.

---

## 0 - Salvar e Sair

Salva os dados no arquivo JSON e encerra o programa.

---

# Estrutura do Projeto

```text
Projeto/
│
├── main.py
├── produto.py
├── estoque.py
├── arquivos.py
├── dados.json
└── README.md
```

---

# Explicação do Código

## main.py

Responsável pela interface do sistema.

Funções principais:

- Exibição do menu.
- Leitura dos dados digitados pelo usuário.
- Validação de entradas.
- Chamada das funções do sistema.
- Integração com persistência em JSON.

Também contém funções auxiliares para:

- Ler números inteiros.
- Ler números decimais.
- Validar textos.
- Validar preços.
- Validar quantidades.

---

## produto.py

Define a classe Produto.

A classe armazena:

```text
Código
Nome
Categoria
Preço
Quantidade
```

Também possui métodos para:

- Exibir os dados do produto.
- Converter o objeto para dicionário, permitindo salvar em JSON.

---

## estoque.py

Contém todas as regras de negócio do sistema.

Funções implementadas:

### Cadastro

```python
cadastrar_produto()
```

Insere um produto mantendo a lista ordenada por código.

---

### Busca Binária

```python
buscar_por_codigo()
```

Localiza produtos pelo código.

Complexidade:

```text
O(log n)
```

---

### Busca Linear

```python
buscar_por_nome()
```

Localiza produtos pelo nome.

Complexidade:

```text
O(n)
```

---

### Edição

```python
editar_produto()
```

Atualiza as informações de um produto.

---

### Remoção

```python
remover_produto()
```

Exclui um produto utilizando o código.

---

### Venda

```python
registrar_venda()
```

Reduz o estoque após uma venda.

---

### Relatórios

```python
listar_produtos()
listar_por_categoria()
estoque_baixo()
```

Geram os relatórios utilizados pelo menu.

---

## arquivos.py

Responsável pela persistência dos dados.

Funções:

### salvar_produtos()

Converte os objetos em dicionários e grava os dados em:

```text
dados.json
```

---

### carregar_produtos()

Lê os dados do JSON e recria os objetos Produto.

---

# Estruturas de Dados Utilizadas

## Vetor Ordenado

Os produtos são armazenados em uma lista mantida em ordem crescente de código.

Isso permite utilizar busca binária para localizar produtos de forma eficiente.

---

## Busca Binária

Utilizada para localizar produtos por código.

Complexidade:

```text
O(log n)
```

A cada comparação, metade do vetor é descartada.

---

## Busca Linear

Utilizada para localizar produtos por nome.

Complexidade:

```text
O(n)
```

É necessário percorrer os elementos até encontrar as correspondências.

---

# Regras de Negócio

O sistema implementa as seguintes regras:

- Não permitir códigos duplicados.
- Não permitir vendas com estoque insuficiente.
- Não permitir preços menores ou iguais a zero.
- Não permitir quantidades negativas.
- Manter os produtos ordenados por código.
- Garantir persistência dos dados em arquivo JSON.

---

# Autor

Projeto desenvolvido para a disciplina de Estruturas de Dados e Algoritmos utilizando Python.