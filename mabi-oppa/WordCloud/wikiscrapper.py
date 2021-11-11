from bs4 import BeautifulSoup
import requests

headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}

url = "https://wiki.mabinogiworld.com/view/NPCs"
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
names = soup.find_all("a")
n=[]
for name in names:
    n.append(name.get_text())

unwanted = ["Tir","World","NPCs",'Patreon', "https", "Wiki", "NPC", "Castle" , "Camp", "Generation",  "Barri", "Dungeon", "Ciar", "Rabbie", "Basic", "Town", "Disclaimer", "Wiki", "World","About", "Mabinogi"]
unwantnr = ["Generation 1","Generation 2","Generation 3","Generation 4","Generation 5","Generation 6","Generation 7",
            "Generation 8","Generation 9","Generation 10","Generation 11","Generation 12"]
new_n = n[80:475]
text = " ".join([e for e in new_n if e not in unwanted if e not in unwantnr])
