from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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

    campo_ordenacao = Select(driver.find_element("css selector", ".product_sort_container"))
    campo_ordenacao.select_by_value("lohi")

    precos_produtos = driver.find_elements("css selector", ".inventory_item_price")
    precos = [float(preco.text.replace("$", "")) for preco in precos_produtos]

    produtos_ordenados = sorted(precos)
    assert precos == produtos_ordenados, "Produtos não estão listados em ordem crescente de preço."

    print("Produtos estão listados em ordem crescente de preço.")

    campo_ordenacao = Select(driver.find_element("css selector", ".product_sort_container"))
    campo_ordenacao.select_by_value("hilo")

    precos_produtos = driver.find_elements("css selector", ".inventory_item_price")
    precos = [float(preco.text.replace("$", "")) for preco in precos_produtos]

    produtos_ordenados = sorted(precos, reverse=True)
    assert precos == produtos_ordenados, "Produtos não estão listados em ordem decrescente de preço."

    print("Produtos estão listados em ordem decrescente de preço.")

except AssertionError as e:
    print("Teste falhou:", str(e))

finally:
    driver.quit()
