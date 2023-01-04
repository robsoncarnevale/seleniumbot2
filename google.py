from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
#variavel para indicar o webdriver que vamos trabalhar

#abrindo o navegador
driver.get("https://google.com")
#comandos basicos selenium

#verifica url
print(driver.current_url)
#verifiCA ttulo da pagina
print(driver.title)
#versão do google
print(driver.capabilities['browserVersion'])

element = driver.find_element('xpath', "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
element.click()
element.send_keys("base Corinthians")
element.submit()

assert driver.title == "base Corinthians - Pesquisa Google"
sleep(3)
#fechar navegador
driver.close()