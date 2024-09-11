from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

# URL of the website
url = "https://dli.suntrackertech.com/"

# Olvasd be a "miss_fr_del1b.csv" fájlt és a benne található lat-lon értékeket
lat_lon_values = []

with open("bang_b.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Átugorjuk a fejléc sort, ha van
    for row in reader:
        lat_lon_values.append(row[0])

# Nyisd meg a böngészőt és navigálj az oldalra
driver = webdriver.Chrome()  # Először telepítsd a Chrome böngésző driverét

driver.get(url)

# Az évszakok nevei
seasons = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Nyisd meg egy CSV fájlt az írásra
with open("DLI_results.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["LatLon"] + seasons)

# Használjuk a Selenium-ot a "Submit" gomb megnyomására és az eredmények lekérésére
for lat_lon in lat_lon_values:
    input_field = driver.find_element(By.ID, "latlonInput")
    
    # Töltsd ki az input mezőt az értékkel
    input_field.clear()
    input_field.send_keys(lat_lon)

    # Nyomd meg a "Enter" billentyűt a mezőben az adat elküldéséhez
    input_field.send_keys(Keys.RETURN)

    # Várj egy rövid ideig, hogy az oldal betöltse az eredményeket (ezt az időzítést beállíthatod)
    driver.implicitly_wait(5)

    # Most már az oldalon vagyunk, ahol az eredmények találhatók
    # Itt meg kell keresni és kinyerni az eredményeket

    # Példaként itt csak kiírom a konzolra az eredményeket
    results = driver.find_elements(By.CLASS_NAME, "card-text")
    dli_values = [result.text for result in results]

    # Írd ki az értékeket a CSV fájlba
    with open("DLI_results.csv", "a", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([lat_lon] + dli_values)

# Böngésző bezárása
driver.quit()