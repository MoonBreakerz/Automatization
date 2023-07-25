Funcionalidade: Realizar Login na página

Cenário I: Realizar Login com o usuário standard_user
Dado que acesso a página "https://www.saucedemo.com/"
Quando insiro o usuário "standard_user" e a senha "secret_sauce"
E clico no botão de login
Então sou redirecionado para a página "inventory.html"

Cenário II: Login com usuário bloqueado "locked_out_user"
Dado que acesso a página "https://www.saucedemo.com/"
Quando insiro o usuário "locked_out_user" e a senha "secret_sauce"
E clico no botão de login
Então vejo a mensagem de erro "Epic sadface: Sorry, this user has been locked out."