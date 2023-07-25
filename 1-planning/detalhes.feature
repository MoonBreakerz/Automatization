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
