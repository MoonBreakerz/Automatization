Funcionalidade: Realizar Login na página

Cenário: Login com o usuário "standard_user"

Dado que acesso a página "https://www.saucedemo.com/"
Quando insiro o usuário "standard_user" e a senha "secret_sauce"
E clico no botão de login
Então sou redirecionado para a página "inventory.html"



Funcionalidade: Verificar Maior e Menor Valor dos Produtos

Cenário: Maior e menor valor dos produtos

Dado que acesso a página "https://www.saucedemo.com/"
E faço login com o usuário "standard_user" e senha "secret_sauce"
Quando verifico os preços dos produtos listados na página de inventário
Então informo o nome e preço do produto com menor valor
E informo o nome e preço do produto com maior valor



Funcionalidade: Realizar a compra de dois produtos

Cenário: Adicionar produtos ao carrinho e finalizar a compra

Dado que acesso a página "https://www.saucedemo.com/inventory.html"
Quando adiciono o produto de menor valor ao carrinho
E adiciono o produto de maior valor ao carrinho
E acesso o carrinho de compras
E finalizo a compra
Então sou redirecionado para a página de confirmação da compra



Funcionalidade: Adicionar e excluir produtos do carrinho

Cenário: Adicionar todos os produtos ao carrinho e excluir os dois de menores valores

Dado que acesso a página "https://www.saucedemo.com/inventory.html"
E verifico a lista de produtos disponíveis
Quando adiciono todos os produtos ao carrinho
Então a quantidade de itens no carrinho é igual ao total de produtos disponíveis
E acesso o carrinho de compras
E identifico os dois produtos de menores valores no carrinho
Quando removo os dois produtos de menores valores do carrinho
Então a quantidade de itens no carrinho é reduzida em 2



Funcionalidade: Filtrar produtos por preço

Cenário: Filtrar produtos pelo preço mais baixo

Dado que acesso a página "https://www.saucedemo.com/inventory.html"
E seleciono a opção "Preço (do menor ao maior)" no filtro de ordenação
Quando verifico a lista de produtos exibidos
Então os produtos estão listados em ordem crescente de preço

Cenário: Filtrar produtos pelo preço mais alto

Dado que acesso a página "https://www.saucedemo.com/inventory.html"
E seleciono a opção "Preço (do maior ao menor)" no filtro de ordenação
Quando verifico a lista de produtos exibidos
Então os produtos estão listados em ordem decrescente de preço



Funcionalidade: Verificar detalhes de um produto

Cenário: Verificar detalhes de um produto específico

Dado que acesso a página "https://www.saucedemo.com/inventory.html"
E seleciono um produto específico da lista
Quando clico no produto selecionado
Então sou redirecionado para a página de detalhes do produto

Cenário: Verificar informações do produto na página de detalhes

Dado que acesso a página de detalhes de um produto específico
Então vejo o nome do produto, descrição, preço e outras informações

Cenário: Adicionar produto ao carrinho a partir da página de detalhes

Dado que acesso a página de detalhes de um produto específico
Quando clico no botão "Adicionar ao Carrinho"
Então o produto é adicionado ao carrinho de compras
E o ícone do carrinho exibe a quantidade de itens corretamente

Cenário: Voltar para a página de inventário a partir da página de detalhes

Dado que acesso a página de detalhes de um produto específico
Quando clico no botão "Voltar para o Inventário"
Então sou redirecionado de volta para a página de inventário