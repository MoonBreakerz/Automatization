from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    campo_usuario = driver.find_element("id", "user-name")
    campo_senha = driver.find_element("id", "password")

    campo_usuario.send_keys("standard_user")
    campo_senha.send_keys("secret_sauce")

    botao_login = driver.find_element("id", "login-button")
    botao_login.click()

    time.sleep(2)  

    assert "inventory.html" in driver.current_url

    produtos = driver.find_elements("css selector", ".btn_inventory")
    for produto in produtos:
        produto.click()

    distintivo_carrinho = driver.find_element("css selector", ".shopping_cart_badge")
    quantidade_no_carrinho = int(distintivo_carrinho.text)

    log_esperado = f"Quantidade de itens no carrinho esperado: {len(produtos)}, Obtido: {quantidade_no_carrinho}"
    print(log_esperado)

    if quantidade_no_carrinho == len(produtos):
        print("Quantidade de itens no carrinho está correta.")
    else:
        print("Quantidade de itens no carrinho está incorreta.")

    link_carrinho = driver.find_element("css selector", ".shopping_cart_link")
    link_carrinho.click()

    itens_carrinho = driver.find_elements("css selector", ".cart_item")
    precos_produtos = driver.find_elements("css selector", ".inventory_item_price")
    precos = [float(preco.text.replace("$", "")) for preco in precos_produtos]

    for _ in range(2):
        menor_preco = min(precos)
        indice_menor_preco = precos.index(menor_preco)
        itens_carrinho[indice_menor_preco].find_element("css selector", ".cart_button").click()
        precos.pop(indice_menor_preco)
        itens_carrinho = driver.find_elements("css selector", ".cart_item")

    distintivo_carrinho = driver.find_element("css selector", ".shopping_cart_badge")
    quantidade_no_carrinho = int(distintivo_carrinho.text)

    log_esperado = f"Quantidade de itens no carrinho após a remoção esperado: {len(produtos) - 2}, Obtido: {quantidade_no_carrinho}"
    print(log_esperado)

    if quantidade_no_carrinho == len(produtos) - 2:
        print("Quantidade de itens no carrinho após a remoção está correta.")
    else:
        print("Quantidade de itens no carrinho após a remoção está incorreta.")

except AssertionError as e:
    print("Teste falhou:", str(e))

finally:
    driver.quit()
