from selenium import web driver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
import timeimport ramdon

class scraper():

    def IniciarNavegador():
        Configuracion=EdgeOptions
        Configuracion.add_argument("--start-maximized")
        Configuracion.add_argument("--guest")
        Configuracion.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebkit/537.36 (KHTML,like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0")
        driver = None

        try:
            driver=webdriver.Edge(options=Configuracion)
            print("Iniciando Navegacion")
        except:
            print(f"fallo en el inicio de navegador {e}")

    def BusquedaElementos(self):
        link=self.link
        driver.get(link)
        ofertas = driver.find_elements(By.TAG_NAME, "a")
        
