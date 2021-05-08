from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

currentdateandtime = datetime.now()
print(currentdateandtime)

print("selenium tests")

driver = webdriver.Firefox(executable_path="C:\TestFiles\geckodriver.exe")
driver.get('http://eve.ii.pw.edu.pl:9007/#/start_page')
time.sleep(2)
button = driver.find_element_by_id("showHelpWindowButton")
button.click()
time.sleep(2)

string1 = driver.find_element_by_tag_name("h1").text
assert string1 == "DnaAssembler - Help"

string2 = driver.find_element_by_id("file_formats_href").text
assert string2 == "Input and output file formats"

string3 = driver.find_element_by_id("algorithms_href").text
assert string3 == 'Parameters and algorithms used in application'

string4 = driver. find_element_by_xpath("//body/div[1]/div[2]/div[2]/h4[5]").text
assert string4 == "For more information send an email:\nr.m.nowak@elka.pw.edu.pl"

string5 = driver.find_element_by_xpath("//h3[contains(text(),'Authors')]").text
assert string5 == "Authors"

string6 = driver.find_element_by_xpath("//span[@id='authors']").text
assert string6 == "Robert Nowak - r.m.nowak@elka.pw.edu.pl\nWiktor Kuśmirek\n\nWarsaw University of Technology,\nFaculty of Electronics and Information Technology,\nWarsaw 2015"

string7 = driver.find_element_by_xpath("//h3[contains(text(),'Application parameters')]").text
assert string7 == "Application parameters"

#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
#string8 = driver.find_element_by_id("server_time").text
#print(string8)
#print(current_time)
#assert string8 == current_time

#currentdate = date.today()
#print(currentdate)


string9 = driver.find_element_by_xpath("//li[@id='db_version']").text
assert string9 == "db version: PostgreSQL 9.4.18 on x86_64-unknown-linux-gnu"

string10 = driver.find_element_by_id("server_version").text
assert string10 == "server version: 0.07.1635; Python: 3.5.3; Arch: ; Os: Linux #1 SMP Debian 4.9.110-1 (2018-07-05); Django: 2.0.2"

string11 = driver.find_element_by_xpath("//li[@id='client_version']").text
assert string11 == "client version: 0.06.1634"

string12 = driver.find_element_by_xpath("//legend[@id='demo_files_legend']").text
assert string12 == "Files from demo"

string13 = driver.find_element_by_xpath("//a[@id='reads_PET_R1.fq_href']").text
assert string13 == "reads_PET_R1.fq"

string14 = driver.find_element_by_xpath("//a[@id='reads_PET_R2.fq_href']").text
assert string14 == "reads_PET_R2.fq"

string15 = driver.find_element_by_xpath("//a[@id='ref.fa_href']").text
assert string15 == "ref.fa"

string16 = driver.find_element_by_xpath("//a[@id='seq.fa_href']").text
assert string16 == "seq.fa"

string17 = driver.find_element_by_xpath("//a[@id='cmp.vcf_href']").text
assert string17 == "cmp.vcf"

button1 = driver.find_element_by_id("showHelpWindowButton").text
assert button1 == "Help"

button2 = driver.find_element_by_id("showLoginWindowButton").text
assert button2 == "Log in"

button3 = driver.find_element_by_id("showNewUserWindowButton").text
assert button3 == "Create new user"

button4 = driver.find_element_by_id("loginAsGuestButton").text
assert button4 == "Log in as guest"

linkview1 = driver.find_element_by_xpath("//a[@id='file_formats_href']")
ActionChains(driver).move_to_element(linkview1).perform()
time.sleep(3)
tooltiptext = linkview1.get_attribute("title")
assert tooltiptext == "Click to view description of input file formats accepted by application and output file formats produced by application"
time.sleep(3)

linkview2 = driver.find_element_by_xpath("//a[@id='algorithms_href']")
ActionChains(driver).move_to_element(linkview2).perform()
time.sleep(3)
tooltiptext1 = linkview2.get_attribute("title")
assert tooltiptext1 == "Click to view description of parameters and algorithms used in application"
time.sleep(3)


###########################PL###########################################
button = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/img[1]")
button.click()

string1pl = driver.find_element_by_tag_name("h1").text
assert string1pl == "DnaAssembler - Pomoc"

string2pl = driver.find_element_by_id("file_formats_href").text
assert string2pl == "Formaty plików wejściowych i wyjściowych"

string3pl = driver.find_element_by_id("algorithms_href").text
assert string3pl == 'Parametry i algorytmy wykorzystane w aplikacji'

string4pl = driver. find_element_by_xpath("//body/div[1]/div[2]/div[2]/h4[5]").text
assert string4pl == "Uzyskaj więcej informacji wysyłając wiadomość:\nr.m.nowak@elka.pw.edu.pl"

string5pl = driver.find_element_by_xpath("//h3[contains(text(),'Autorzy')]").text
assert string5pl == "Autorzy"

string6pl = driver.find_element_by_xpath("//span[@id='authors']").text
assert string6pl == "Robert Nowak - r.m.nowak@elka.pw.edu.pl\nWiktor Kuśmirek\n\nPolitechnika Warszawska,\nWydział Elektroniki i Technik Informacyjnych,\nWarszawa 2015"

string7pl = driver.find_element_by_xpath("//h3[contains(text(),'Parametry aplikacji')]").text
assert string7pl == "Parametry aplikacji"

#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
#string8 = driver.find_element_by_id("server_time").text
#print(string8)
#print(current_time)
#assert string8 == current_time

string9pl = driver.find_element_by_xpath("//li[@id='db_version']").text
assert string9pl == "wersja bazy danych: PostgreSQL 9.4.18 on x86_64-unknown-linux-gnu"

string10 = driver.find_element_by_id("server_version").text
assert string10 == "wersja serwera: 0.07.1635; Python: 3.5.3; Arch: ; Os: Linux #1 SMP Debian 4.9.110-1 (2018-07-05); Django: 2.0.2"

string11pl = driver.find_element_by_xpath("//li[@id='client_version']").text
assert string11pl == "wersja klienta: 0.06.1634"

string12pl = driver.find_element_by_xpath("//legend[@id='demo_files_legend']").text
assert string12pl == "Pliki z filmu"

string13pl = driver.find_element_by_xpath("//a[@id='reads_PET_R1.fq_href']").text
assert string13pl == "reads_PET_R1.fq"

string14pl = driver.find_element_by_xpath("//a[@id='reads_PET_R2.fq_href']").text
assert string14pl == "reads_PET_R2.fq"

string15pl = driver.find_element_by_xpath("//a[@id='ref.fa_href']").text
assert string15pl == "ref.fa"

string16pl = driver.find_element_by_xpath("//a[@id='seq.fa_href']").text
assert string16pl == "seq.fa"

string17pl = driver.find_element_by_xpath("//a[@id='cmp.vcf_href']").text
assert string17pl == "cmp.vcf"

button1 = driver.find_element_by_id("showHelpWindowButton").text
assert button1 == "Pomoc"

button2 = driver.find_element_by_id("showLoginWindowButton").text
assert button2 == "Zaloguj się"

button3 = driver.find_element_by_id("showNewUserWindowButton").text
assert button3 == "Dodaj użytkownika"

button4 = driver.find_element_by_id("loginAsGuestButton").text
assert button4 == "Zaloguj się jako gość"

linkview3 = driver.find_element_by_xpath("//a[@id='file_formats_href']")
ActionChains(driver).move_to_element(linkview3).perform()
time.sleep(3)
tooltiptext2 = linkview3.get_attribute("title")
assert tooltiptext2 == "Kliknij, aby zobaczyć opis formatów plików wejściowych akceptowanych przez aplikację i opis formatów plików wyjściowych produkowanych przez aplikację"
time.sleep(3)

linkview4 = driver.find_element_by_xpath("//a[@id='algorithms_href']")
ActionChains(driver).move_to_element(linkview4).perform()
time.sleep(3)
tooltiptext3 = linkview4.get_attribute("title")
assert tooltiptext3 == "Kliknij, aby zobaczyć opis parametrów i algorytmów wykorzystanych w aplikacji"
time.sleep(3)










