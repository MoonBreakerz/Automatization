from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    # Cenário: Logar com o usuário "standard_user"
    driver.get("https://www.saucedemo.com/")
    campo_usuario = driver.find_element("id", "user-name")
    campo_senha = driver.find_element("id", "password")

    campo_usuario.send_keys("standard_user")
    campo_senha.send_keys("secret_sauce")

    botao_login = driver.find_element("id", "login-button")
    botao_login.click()

    time.sleep(2)  

    # Verificação do redirecionamento para a página do inventário
    assert "inventory.html" in driver.current_url

    # Adicionar ao carrinho o produto com menor valor
    precos_produtos = driver.find_elements("css selector", ".inventory_item_price")
    precos = [float(preco.text.replace("$", "")) for preco in precos_produtos]
    menor_preco = min(precos)
    indice_produto_menor_preco = precos.index(menor_preco)
    botoes_adicionar_carrinho = driver.find_elements("css selector", ".btn_inventory")
    botoes_adicionar_carrinho[indice_produto_menor_preco].click()

    # Adicionar ao carrinho o produto com maior valor
    maior_preco = max(precos)
    indice_produto_maior_preco = precos.index(maior_preco)
    botoes_adicionar_carrinho = driver.find_elements("css selector", ".btn_inventory")
    botoes_adicionar_carrinho[indice_produto_maior_preco].click()

    # Ir para o carrinho
    link_carrinho_compras = driver.find_element("class name", "shopping_cart_link")
    link_carrinho_compras.click()

    time.sleep(2)  # Aguarda 2 segundos para a página carregar

    # Finalizar a compra
    botao_checkout = driver.find_element("id", "checkout")
    botao_checkout.click()

    # Preencher informações para finalizar a compra
    campo_primeiro_nome = driver.find_element("id", "first-name")
    campo_ultimo_nome = driver.find_element("id", "last-name")
    campo_cep = driver.find_element("id", "postal-code")

    campo_primeiro_nome.send_keys("Nome")
    campo_ultimo_nome.send_keys("Sobrenome")
    campo_cep.send_keys("CEP")

    botao_continuar = driver.find_element("id", "continue")
    botao_continuar.click()

    # Confirmar a compra
    botao_finalizar = driver.find_element("id", "finish")
    botao_finalizar.click()

    time.sleep(2)  # Aguarda 2 segundos para a página carregar

    # Verificar se a compra foi realizada com sucesso
    assert "checkout-complete.html" in driver.current_url
    print("Compra realizada com sucesso!")

except AssertionError as e:
    print("Teste falhou:", str(e))

finally:
    # Fechando o navegador após a execução dos testes
    driver.quit()
