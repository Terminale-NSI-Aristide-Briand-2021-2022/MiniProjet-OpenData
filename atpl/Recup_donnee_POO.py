import json
import requests

reponse = requests.get('https://www.data.gouv.fr/fr/datasets/r/8646ddd2-aa1f-4773-9e47-1a53c8f0ab38')

tabJSON = json.loads(reponse.text)

liste_objet = []


class Activites_Touristiques:
    
    def __init__(self,code,act):
        self.code_postal = code
        self.type_activite = act
        
    def estPresent(self,code):
        """
        Paramètre : code --> chaîne de caractère
                    sequence --> chaîne de caractère
        Résultat : True si le code est présent dans la sequence sinon False
        """
        sequence = self.type_activite
        for i in range(len(sequence)-len(code)+1):
            if code==sequence[i:i+len(code)]:
                return True
        return False
        
    def commence(self,code):
        """
        Paramètre : code --> chaîne de caractère de longueur 2
                    sequence --> chaîne de caractère
        Résultat : True si la sequence commence par le code sinon False
        """
        sequence = self.code_postal
        if sequence[0] == code[0] and sequence[1] == code[1]:
            return True
        else:
            return False


#________________________________________________________________________________________________


def instances_ActivitesTouristiques():
    for objetJSON in tabJSON:
        try:
            liste_objet.append(Activites_Touristiques(objetJSON['fields']['codepostal'],objetJSON['fields']['type']))
        except:
            pass

instances_ActivitesTouristiques()


#________________________________________________________________________________________________


def NombreTotal_par_Activite(Lo = liste_objet):
    """
    Paramètre : Lo --> liste contenant toutes les instances de la classe Activites_Touristiques
    Résultat : Nombre total pour chaque activité dans tout les Pays-de-la-Loire
    """
    nb_JeuxPourEnfants = 0
    nb_AirePiqueNique = 0
    nb_Piscine = 0
    nb_CentreEquestre = 0
    nb_Cinema = 0
    nb_ActiviteSportivesLudiques = 0
    
    for element in range(len(Lo)):
            
        if Lo[element].estPresent("Jeux pour enfants") == True:
            nb_JeuxPourEnfants = nb_JeuxPourEnfants+1
            
        if Lo[element].estPresent("Aire de pique-nique") == True:
            nb_AirePiqueNique = nb_AirePiqueNique+1
            
        if Lo[element].estPresent("Piscine") == True:
            nb_Piscine = nb_Piscine+1
            
        if Lo[element].estPresent("Centre équestre") == True:
            nb_CentreEquestre = nb_CentreEquestre+1
            
        if Lo[element].estPresent("Cinéma") == True:
            nb_Cinema = nb_Cinema+1
            
        if Lo[element].estPresent("Activités sportives et ludiques") == True:
            nb_ActiviteSportivesLudiques = nb_ActiviteSportivesLudiques+1
                
    return nb_JeuxPourEnfants,nb_AirePiqueNique,nb_Piscine,nb_CentreEquestre,nb_Cinema,nb_ActiviteSportivesLudiques


nombreTotal = 0

for i in range(6):
    nombreTotal = nombreTotal+NombreTotal_par_Activite()[i]


#________________________________________________________________________________________________


def pourcentage(emplacement_act,total = nombreTotal):
    """
    Paramètre : Total --> nombre total de la catégorie
                nombre_a_calculer --> nombre dont on veut calculer le pourcentage
    Résultat : Pourcentage du nombre_a_calculer par rapport au Total
    """
    nombre_a_calculer = NombreTotal_par_Activite()[emplacement_act]
    c = nombre_a_calculer*100/total
    if c-int(c) > 0.5:
        c = int(c)+1
    else:
        c = int(c)
    return c


#________________________________________________________________________________________________


def NombreActivite_par_CodePostal(choix,Lo = liste_objet):
    """
    Paramètre : choix --> activité sélectionnée par l'utilisateur dans la liste déroulante
                Lo --> liste contenant toutes les instances de la classe Activites_Touristiques
    Résultat : Nombre de l'activité sélectionnée dans chaque département
    """
    nb_LoireAtlantique = 0
    nb_MaineEtLoire = 0
    nb_Mayenne = 0
    nb_Sarthe = 0
    Activite = choix
    
    for element in range(len(Lo)):
        if Lo[element].estPresent(Activite) == True:
            
            if Lo[element].commence("44") == True:
                nb_LoireAtlantique = nb_LoireAtlantique+1
            
            if Lo[element].commence("49") == True:
                nb_MaineEtLoire = nb_MaineEtLoire+1
                
            if Lo[element].commence("53") == True:
                nb_Mayenne = nb_Mayenne+1
                
            if Lo[element].commence("72") == True:
                nb_Sarthe = nb_Sarthe+1
                    
    return nb_LoireAtlantique,nb_MaineEtLoire,nb_Mayenne,nb_Sarthe
