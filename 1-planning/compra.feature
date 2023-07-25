Funcionalidade: Realizar a compra de dois produtos

Cenário: Adicionar produtos ao carrinho e finalizar a compra
    Dado que acesso a página "https://www.saucedemo.com/inventory.html"
    Quando adiciono o produto de menor valor ao carrinho
    E adiciono o produto de maior valor ao carrinho
    E acesso o carrinho de compras
    E finalizo a compra
    Então sou redirecionado para a página de confirmação da compra
