from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome()

start = 1

def store_data(table_data, soup):
    for row in soup.find_all("tr"):
        row_data = []
        for cell in row.find_all(["th", "td"]):
            row_data.append(cell.get_text())
        
        table_data.append(row_data)


table_data = []
for i in range(427):

    s = 'https://finviz.com/screener.ashx?v=111&p=w&o=price&r='+str(start)
    driver.get(s)

    table_element = driver.find_element(By.CLASS_NAME, 'table-light')

    table_html = table_element.get_attribute("outerHTML")

    soup = BeautifulSoup(table_html, "html.parser")
    
    
    
    store_data(table_data, soup)
    start+=20

driver.quit()

df = pd.DataFrame(table_data)

df.to_csv("stocks.csv", index = False)
