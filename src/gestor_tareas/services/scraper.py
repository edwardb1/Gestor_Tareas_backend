from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
import time
import random

def buscar_ofertas_trabajo():
    # 1. Configuración de Edge
    options = EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--guest") # Entrar como invitado a veces ayuda
    
    # Truco anti-detección
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0")

    driver = None
    try:
        # 2. INTENTO DIRECTO (Sin Gestor externo)
        # Selenium 4.6+ es inteligente y buscará el driver solo.
        print("Conexion con el driver de navegador")
        driver = webdriver.Edge(options=options)
        
    except Exception as e:
        print(f"Error fatal iniciando Edge: {e}")
        print("PISTA: Si esto falla, necesitaremos descargar el archivo msedgedriver.exe manualmente.")
        return []

    datos_encontrados = []

    try:
        
        url_objetivo = "https://www.python.org/jobs/"
        print(f"Entrando a: {url_objetivo}")
        driver.get(url_objetivo)

        time.sleep(3) 

        ofertas = driver.find_elements(By.CSS_SELECTOR, ".list-recent-jobs li")
        print(f"Se encontraron {len(ofertas)} posibles ofertas.")

        for oferta in ofertas[:5]:
            try:
                elemento_titulo = oferta.find_element(By.TAG_NAME, "a")
                titulo = elemento_titulo.text
                url_detalle = elemento_titulo.get_attribute("href")
                
                empresa_texto = oferta.find_element(By.CLASS_NAME, "listing-company-name").text
                empresa = empresa_texto.split("\n")[0].strip()
                
                ubicacion = oferta.find_element(By.CLASS_NAME, "listing-location").text

                print(f" Detectado: {titulo} en {empresa}")

                datos_encontrados.append({
                    "titulo": titulo,
                    "empresa": empresa,
                    "url": url_detalle,
                    "ubicacion": ubicacion,
                    "salario": "No especificado",
                    "fecha_publicacion": "2026-01-01"
                })
                time.sleep(random.uniform(0.5, 1.0))

            except Exception as e:
                print(f"Error leyendo una oferta: {e}")

    except Exception as e:
        print(f"Error navegando: {e}")
    finally:
        if driver:
            print("El robot ha terminado su turno.")
            driver.quit()
    
    return datos_encontrados

def ruta_buscar(self, URL=str):
    URL=input(str())

if __name__ == "__main__":
    resultados = buscar_ofertas_trabajo()
    print(f"Resumen: Se extrajeron {len(resultados)} ofertas.")