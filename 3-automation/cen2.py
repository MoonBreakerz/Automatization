from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicialização do WebDriver (usando Chrome neste exemplo)
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

    time.sleep(2)  # Aguarda 2 segundos para a página carregar

    # Verificação do redirecionamento para a página do inventário
    assert "inventory.html" in driver.current_url

    # Verificar e informar o produto com menor valor
    precos_produtos = driver.find_elements("css selector", ".inventory_item_price")
    precos = [float(preco.text.replace("$", "")) for preco in precos_produtos]
    menor_preco = min(precos)
    indice_produto_menor_preco = precos.index(menor_preco)
    nome_produto_menor_preco = driver.find_elements("css selector", ".inventory_item_name")[indice_produto_menor_preco].text
    print(f"O produto com menor valor é '{nome_produto_menor_preco}' e custa R${menor_preco:.2f}.")

    # Verificar e informar o produto com maior valor
    maior_preco = max(precos)
    indice_produto_maior_preco = precos.index(maior_preco)
    nome_produto_maior_preco = driver.find_elements("css selector", ".inventory_item_name")[indice_produto_maior_preco].text
    print(f"O produto com maior valor é '{nome_produto_maior_preco}' e custa R${maior_preco:.2f}.")

except AssertionError as e:
    print("Teste falhou:", str(e))

finally:
    # Fechando o navegador após a execução dos testes
    driver.quit()
