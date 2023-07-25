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
