from json import*
import requests

donnees=requests.get("https://www.data.gouv.fr/fr/datasets/r/1c5f9575-9545-43a4-bc8e-dc105f593a9a")
tabJSON = loads(donnees.text)


def bac(choix):
    #tout les bacs
    if choix=="nombre d'admis au baccalaureat":
        donnee_choisie='nombre_d_admis_au_baccalaureat'
    elif choix=="pourcentage d'admis au baccalaureat":
        donnee_choisie='pourcentage_d_admis_au_baccalaureat'
    #bac général
    elif choix=="nombre d'admis au baccalaureat général":
        donnee_choisie='nombre_d_admis_au_baccalaureat_general'
    elif choix=="pourcentage d'admis au baccalaureat general":
        donnee_choisie='pourcentage_d_admis_au_baccalaureat_general'
    #bac technologique
    elif choix=="nombre d'admis au baccalaureat technologique":
        donnee_choisie='nombre_d_admis_au_baccalaureat_technologique'
    elif choix=="pourcentage d'admis au baccalaureat technologique":
        donnee_choisie='pourcentage_d_admis_au_baccalaureat_technologique'
    #bac profesionnel  
    elif choix=="nombre d'admis au baccalaureat general professionnel":
        donnee_choisie='nombre_d_admis_au_baccalaureat_professionnel'
    elif choix=="pourcentage d'admis au baccalaureat professionel":
        donnee_choisie='pourcentage_d_admis_au_baccalaureat_professionnel'
    return donnee_choisie


def toutadmis(annee,donnee):
    for objetJSON in tabJSON:
        if objetJSON['fields'] ['annee']==annee and objetJSON['fields']['origine_sociale']=="Ensemble":
            print(objetJSON['fields'][donnee])

def tri(valeur,annee):
    n=min(annee)
    c=n
    m=len(valeur)
    tempvaleur=[]
    tempannee=[]
    for i in range(m):
        for j in range(0,m):
            if annee[j]==c:
                tempvaleur.append(valeur[j])
                tempannee.append(annee[j])
        c=c+1
    return tempvaleur,tempannee

def supprvaleur(annee1,annee2,valeur,annee):
    m=annee1-min(annee)
    n=max(annee)-annee2
    for i in range(m):
        annee.pop(0)
        valeur.pop(0)
    for i in range(n):
        valeur.pop()
        annee.pop()
    return valeur,annee

def toutadmis_2(annee1,annee2,donnee,origineS):
    valeurs=[]
    annees=[]
    for objetJSON in tabJSON:
        if objetJSON['fields']['origine_sociale']==origineS:
            m=objetJSON['fields'][bac(donnee)]
            valeurs.append(m)
            c=objetJSON['fields']['annee']
            annees.append(c)
    valeur_triees,annees_triees=tri(valeurs,annees)
    valeur_triees,annees_triees=supprvaleur(annee1,annee2,valeur_triees,annees_triees)
    return valeur_triees,annees_triees