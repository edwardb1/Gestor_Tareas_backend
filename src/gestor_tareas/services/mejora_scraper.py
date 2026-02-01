from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
import time
import random

from src.gestor_tareas.logger import log

class scraper():

    def __init__(self, initial_link):
        self.link = initial_link
        self.driver = None
        self.datos_encontrados = []

    def IniciarNavegador(self):
        Configuracion=EdgeOptions()
        Configuracion.add_argument("--start-maximized")
        Configuracion.add_argument("--guest")
        Configuracion.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebkit/537.36 (KHTML,like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0")

        try:
            self.driver=webdriver.Edge(options=Configuracion)
            log.debug("conexion")
        except Exception as e:
            print(f"fallo en el inicio de navegador {e}")
            log.error("conexcion inf")

    def BusquedaElementos(self):

        link = self.link
        driver = self.driver

        if not self.driver:
            self.IniciarNavegador()
            if not self.driver: 
                return[]

        try:
            driver.get(link)
            time.sleep(2)
            ofertas = driver.find_elements(By.CSS_SELECTOR, ".list-recent-jobs li")
            log.info("si se encomtraron ofertas")

            for oferta in ofertas[:5]:
                try:
                    log.inf("conexcion exitosa")
                    elemento_titulo= oferta.find_element(By.TAG_NAME,"a")
                    titulo = elemento_titulo
                    url_detalle = elemento_titulo.get_attribute("href")

                    empresa_descrip_trabaj = oferta.find_element(By.CLASS_NAME,"listing-location").text
                    empresa = empresa_descrip_trabaj.split("\n")[0].strip()

                    ubicacion = oferta.find_element(By.CLASS_NAME,"listing-location").text

                    log.info("se encontro")

                    datos_encontrados.append({
                        "titulo": titulo,
                        "empresa": empresa,
                        "url": url_detalle,
                        "ubicacion": ubicacion,
                        "salario": "no especificado",
                        "fecha_publicacion": "2026-01-01",
                        "estado": "Nuevo"
                    })

                    time.sleep(random.uniform(0.4,1.3))
                except Exception as e:
                    log.warning(f"error en la navegacion: {e}")
        except Exception as e:
            log.info("no se logro conexion")

        finally:
            if driver:
                driver.quit()
                log.inf("cerrado de navegador")
        return self.datos_encontrados

if __name__ == "__main__":
    URL_link = scraper("https://www.python.org/jobs/")

    resultados = URL_link.BusquedaElementos()


        
