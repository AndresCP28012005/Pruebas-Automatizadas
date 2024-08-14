from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configura el WebDriver para Brave (reemplaza el path con la ubicación de tu ChromeDriver y Brave)
driver_path = "F:/andres/Descargas/chromedriver-win64/chromedriver-win64/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

options = webdriver.ChromeOptions()
options.binary_location = brave_path

# Crear el servicio con la ruta del ChromeDriver
service = Service(executable_path=driver_path)

# Inicia el WebDriver con el servicio y las opciones configuradas
driver = webdriver.Chrome(service=service, options=options)

usuario = "Usuario"
contraseña = "*************"
# Configura el WebDriver para Brave (reemplaza el path con la ubicación de tu ChromeDriver y Brave)



try:
    # Abre GitHub
    driver.get("https://github.com/login")

    # Encuentra el campo de nombre de usuario y escribe el nombre de usuario
    username = driver.find_element(By.ID, "login_field")
    username.send_keys(usuario)

    # Encuentra el campo de contraseña y escribe la contraseña
    password = driver.find_element(By.ID, "password")
    password.send_keys(contraseña)

    # Envía el formulario de inicio de sesión
    password.send_keys(Keys.RETURN)

    # Espera para asegurarse de que la página haya cargado completamente
    time.sleep(10)

       # Encuentra el enlace por el href y haz clic en él
    repo_link = driver.find_element(By.XPATH, '//a[@href="/Laupint307/PROYECTO_KIDSBOX"]')
    repo_link.click()

    # Espera para ver el resultado
    time.sleep(5)


finally:
    # Cierra el navegador
    driver.quit()
