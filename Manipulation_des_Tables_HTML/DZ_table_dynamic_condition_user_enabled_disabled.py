# selenium 4 Manipulation de Table dinamic
"""DZ
Site – orange login, a gauche – Admin – UsersManagement-Users
Table dynamique
récupérer les nombres des utilisateurs
récupérer les nombres d utilisateurs status – enabled
récupérer les nombres d utilisateurs status – disabled
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#My_wait=WebDriverWait(driver,20)
#MyWait=WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[Exception])

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#time.sleep(4)

title_of_page = driver.title
print(title_of_page)
time.sleep(4)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH,"//button").click()                # Zaloginilis'
time.sleep(5)

driver.find_element(By.XPATH,"//nav/div[2]/ul/li[1]/a").click()    #click sur Admin-a gauche
time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()   #click sur UserMamagement
time.sleep(4)
driver.find_element(By.XPATH," //a[normalize-space()='Users']").click()                        #click sur User dropdown
time.sleep(5)


# on va recuperer les nomres des lignes du table
nombre_des_lignes= len(driver.find_elements(By.XPATH,"//div[@role='row']"))           #//div[@role='table']
print(nombre_des_lignes)               #afficher les lignes - combien les lignes dans ce tableau

"""#on va recuperer les nombres des colonnes du table
nombre_des_colonnes= len(driver.find_elements(By.XPATH,"//div[@role='table']//th"))
print(nombre_des_colonnes)"""

# recupere entete du tableau -- zagolovok tavlicy - pervaya liniya
"""compteur_enabled = 0
valeur_enabled = driver.find_elements(By.XPATH, "//div[@class='oxd-table-header']")
for i in range(1,len(valeur_enabled)+1):
    data= driver.find_element(By.XPATH, "(//div[@role='cell'])[17]["+str(i)+"]").text
    if data=="Enabled":
        compteur_enabled = compteur_enabled + 1
        print(compteur_enabled)"""
    #print(data)           #pechataet v stroku - pervuyu liniyu tablicy
compteur_enabled=0
valeur_enabled = driver.find_elements(By.XPATH, "(// div[contains(text(), 'Enabled')])")    #(//div[contains(text(),'Enabled')])
for enabled in range(2,nombre_des_lignes+1):
    if enabled == 'Enabled':
        #prix = driver.find_element(By.XPATH, "(// div[contains(text(), 'Enabled')])" + str(ligne)).text
        #compteur_enabled=compteur_enabled+1
        print(enabled)
#print(valeur_enabled)

"""otsyuda NE rabotaet
for ligne in range(2,nombre_des_lignes+1):      #esli ne postavit +1 - ne dast poslednyuyu stroku

                                                #bybiraem iz tablicy -konkretnyi avtor kakie knigi u nego i prix
    status= driver.find_element(By.XPATH, "//div[@class='oxd-table-header']//tr["+str(ligne)+"]/td[2]").text

    if status == 'Enabled':
        status = driver.find_element(By.XPATH, "div[@class='oxd-table-header']//tr[" + str(ligne) + "]/td[4]").text
        #nom_livre = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(ligne) + "]/td[1]").text
        print(status, "*")"""
"""
#on va lire une cellule specifique de la table
valeur_cellule = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[3]/td[1]")      #vzyat vse znacheniya: "//table[@name='BookTable']//td"

print(valeur_cellule.text)                      #afficher le donnes d<une cellule

#recuperer toutes les donnees du tableau
                                            #deux boucles for pour recoupere des donnees
time.sleep(3)
for ligne in range(2,nombre_des_lignes+1):      #esli ne postavit +1 - ne dast poslednyuyu stroku

                                                #bybiraem iz tablicy -konkretnyi avtor kakie knigi u nego i prix
    auteur= driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(ligne)+"]/td[2]").text

    if auteur == 'Amit':
        prix = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(ligne) + "]/td[4]").text
        nom_livre = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(ligne) + "]/td[1]").text
        print(auteur, "*",nom_livre,"*",prix)

"""
driver.close()
