from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C:\TestFiles\geckodriver.exe")
driver.get('http://eve.ii.pw.edu.pl:9007/#/start_page')
title = driver.title
print(title)
assert 'DnaAssembler' == title
time.sleep(2)
text = driver.findElement(By.xpath("/(@class,'ng-binding')/h1")).getText()
print(text)




