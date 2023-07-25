Funcionalidade: Verificar Maior e Menor Valor dos Produtos

Cenário: Maior e menor valor dos produtos
	Dado que acesso a página "https://www.saucedemo.com/"
	E faço login com o usuário "standard_user" e senha "secret_sauce"
	Quando verifico os preços dos produtos listados na página de inventário
	Então informo o nome e preço do produto com menor valor
	E informo o nome e preço do produto com maior valor