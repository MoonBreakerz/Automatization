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
