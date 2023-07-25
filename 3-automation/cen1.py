from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicialização do WebDriver (usando Chrome neste exemplo)
driver = webdriver.Chrome()  # Substitua pelo caminho correto do ChromeDriver

try:
    # Cenário: Realizar login com o usuário standard_user
    driver.get("https://www.saucedemo.com/")
    username_input = driver.find_element("id", "user-name")
    password_input = driver.find_element("id", "password")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element("id", "login-button")
    login_button.click()

    time.sleep(2)  # Aguarda 2 segundos para a página carregar

    # Verificação do redirecionamento para a página do inventário
    assert "inventory.html" in driver.current_url

    # Cenário: Tentar fazer login com o usuário bloqueado "locked_out_user"
    driver.get("https://www.saucedemo.com/")
    username_input = driver.find_element("id", "user-name")
    password_input = driver.find_element("id", "password")

    username_input.clear()  # Limpa o campo de usuário
    username_input.send_keys("locked_out_user")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element("id", "login-button")
    login_button.click()

    time.sleep(2)  # Aguarda 2 segundos para a página carregar

    # Verificação da mensagem de erro de usuário bloqueado
    error_message = driver.find_element("css selector", "h3[data-test='error']")
    assert "Epic sadface: Sorry, this user has been locked out." in error_message.text

    print("Testes automatizados concluídos com sucesso!")

except AssertionError as e:
    print("Teste falhou:", str(e))

finally:
    # Fechando o navegador após a execução dos testes
    driver.quit()