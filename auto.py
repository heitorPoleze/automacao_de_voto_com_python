from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

URL = "https://www.agazeta.com.br/hz/gastronomia/qual-municipio-produz-o-melhor-cafe-especial-do-es-vote-na-enquete-de-hz-0326"
RADIO_ID = "PDI_answer73205146"
VOTE_BUTTON_ID = "pd-vote-button16704375"

CAMINHO_FIREFOX_DEV = r"C:\Program Files\Firefox Developer Edition\firefox.exe"
options = FirefoxOptions()
options.binary_location = CAMINHO_FIREFOX_DEV

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()), 
    options=options
)
options.add_argument("--headless")
qtdvotos = 0

try:
    while True:
        print("\n Acessando a URL")
        driver.get(URL)
        
        time.sleep(2)
        
        try:
            radio = driver.find_element(By.ID, RADIO_ID)
            
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio)
            time.sleep(0.5)
            
            driver.execute_script("arguments[0].click();", radio)
            print("Santa Teresa selecionada")
            
            time.sleep(0.5)
            
            vote_button = driver.find_element(By.ID, VOTE_BUTTON_ID)
            
            driver.execute_script("arguments[0].click();", vote_button)
            print("Votado com sucesso!")
        
            qtdvotos += 1
            print(f"Quantidade de votos: {qtdvotos}")

            time.sleep(1)
            
        except Exception as e:
            print(f"Erro no ciclo: Elemento obscured ou não carregado. Reiniciando...")
            time.sleep(2)

except KeyboardInterrupt:
    print("\nAutomação interrompida pelo usuário.")
finally:
    driver.quit()