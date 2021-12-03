import urllib.request







#print('Beginning file download ...')
import csv
import zipfile

url = 'https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv'
urllib.request.urlretrieve(url, 'API_SP.POP.TOTL_DS2_fr_csv_v2_3167589.zip')

zip = zipfile.ZipFile('API_SP.POP.TOTL_DS2_fr_csv_v2_3167589.zip')
zip.extract('API_SP.POP.TOTL_DS2_en_csv_v2_3358390.csv', 'DonneesTest')
zip.close()

def recherche(code,sequence):
    """Cette fonction permet de savoir si une chaine de caractère se trouve dans une autre
    elle renvoit donc True ou False"""
    lcode = len(code)
    lsequ = len(sequence)
    for i in range(len(sequence)-len(code)+1):
        if lsequ<lcode:
            pass
        elif code == sequence[i:i+len(code)]:
            return True
            break
    return False


def Pays(Type):
    with open("DonneesTest\API_SP.POP.TOTL_DS2_en_csv_v2_3358390.csv", 'r') as file:
        reader = csv.reader(file,delimiter=",")
        n=4
        Country = []
        for row in reader:
            if n ==0: #On ne souhaite pas avoir accès au 4 premières lignes
                if row[0] == "Not classified" or row[0] == "West Bank and Gaza": #Ces 2 lignes ont des valeurs qui sont vide dans le fichier
                    pass
                elif recherche(Type,row[0].lower()):
                    if Type == row[0][0:len(Type)].lower() : #On place en première place de la liste le pays étant le plus succeptible de vouloir être recherché
                        Country.insert(0,row)
                    else:
                        Country.append(row)
            else:
                n=n-1
        return Country #Retourne la liste de données de chaque pays semblable au paramêtre Type



