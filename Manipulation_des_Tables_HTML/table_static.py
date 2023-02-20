# selenium 4 Manipulation de Table Static
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)
# on va recuperer les nomres des lignes du table
nombre_des_lignes= len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(nombre_des_lignes)               #afficher les lignes - combien les lignes dans ce tableau

#on va recuperer les nombres des colonnes du table
nombre_des_colonnes= len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
print(nombre_des_colonnes)

# recupere entete du tableau -- zagolovok tavlicy - pervaya liniya
valeur_entete = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
for i in range(1,len(valeur_entete)+1):
    data_entete= driver.find_element(By.XPATH, "//table[@name='BookTable']//th["+str(i)+"]").text
    print(data_entete,end="    ")           #pechataet v stroku - pervuyu liniyu tablicy

#on va lire une cellule specifique de la table
valeur_cellule = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[3]/td[1]")      #vzyat vse znacheniya: "//table[@name='BookTable']//td"

print(valeur_cellule.text)                      #afficher le donnes d<une cellule

#recuperer toutes les donnees du tableau
                                            #deux boucles for pour recoupere des donnees
time.sleep(3)
for ligne in range(2,nombre_des_lignes+1):      #esli ne postavit +1 - ne dast poslednyuyu stroku
    for colonne in range(2,nombre_des_colonnes+1):  #esli ne postavit +1 - ne dast posledij stolbec konec cellule
        data_cellule = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(ligne)+"]/td["+str(colonne)+"]").text
        print(data_cellule)
print()
driver.close()
