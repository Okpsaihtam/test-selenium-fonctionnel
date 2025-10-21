from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Remplace l'IP ci-dessous par celle de ton Raspberry Pi ou de ta VM
GRID_URL = "http://192.168.0.237:4444/wd/hub"

options = Options()
# options.add_argument("--headless")  # Décommente si tu veux exécuter sans interface graphique
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

def wait_and_click(driver, xpath, timeout=10):
    time.sleep(2)
    bouton = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", bouton)
    bouton.click()

def slow_scroll_to_bottom(driver, step=100, delay=0.2):
    max_y = driver.execute_script("return document.body.scrollHeight")
    current_y = driver.execute_script("return window.pageYOffset;")
    while current_y + step < max_y:
        current_y += step
        driver.execute_script(f"window.scrollTo(0, {current_y});")
        time.sleep(delay)
        max_y = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {max_y});")
    time.sleep(delay)

driver = None
try:
    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )
    driver.set_window_size(640, 720)
    driver.set_window_position(0, 0)

    time.sleep(30)

    driver.get("https://okpsaihtam.github.io/histoire-asse/")
    time.sleep(2)
    slow_scroll_to_bottom(driver)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    wait_and_click(driver, "//a[contains(text(), \"En savoir plus sur la création du club\")]")
    time.sleep(2)
    slow_scroll_to_bottom(driver)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    wait_and_click(driver, "//a[contains(text(), \"Retour à l'Accueil\")]")
    time.sleep(2)
    slow_scroll_to_bottom(driver)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    wait_and_click(driver, "//a[contains(text(), \"Découvrez les moments de gloire de l'ASSE\")]")
    time.sleep(2)
    slow_scroll_to_bottom(driver)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    wait_and_click(driver, "//a[contains(text(), \"Retour à l'Accueil\")]")
    time.sleep(2)

except Exception as e:
    print(f"Erreur détectée : {e}")
finally:
    if driver:
        try:
            driver.quit()
        except Exception:
            pass
