from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

# URL of the website
url = "https://dli.suntrackertech.com/"


# Read the "miss_fr_del1b.csv" file and the lat-lon values in it
lat_lon_values = []

with open("missing_p2.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  #Skip the header line if there is one
    for row in reader:
        lat_lon_values.append(row[0])

#Open your browser and navigate to the page
driver = webdriver.Chrome()

#First, install the Chrome browser driver
driver.get(url)

# The names of the months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Open a CSV file for writing
with open("missing_p2.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["LatLon"] + months)

# Let's use Selenium to press the "Submit" button and get the results
for lat_lon in lat_lon_values:
    input_field = driver.find_element(By.ID, "latlonInput")
    
    # Fill the input field with the value
    input_field.clear()
    input_field.send_keys(lat_lon)

    # Press "Enter" in the field to send the data
    input_field.send_keys(Keys.RETURN)

    # Wait a short time for the page to load the results (you can set this timing)
    driver.implicitly_wait(5)

    # We are now on the page with the results
    # Here you have to search and extract the results

    # As an example, I'm just writing the results to the console here
    results = driver.find_elements(By.CLASS_NAME, "card-text")
    dli_values = [result.text for result in results]

    # Write the values ​​to the CSV file
    with open("missing_p2.csv", "a", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([lat_lon] + dli_values)

# Close browser
driver.quit()