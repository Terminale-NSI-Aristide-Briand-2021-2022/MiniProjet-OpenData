from donnees import*
import matplotlib.pyplot as plt

class Graphique:
    def __init__(self,an1,an2,don,ori,Nm,st):
        """
        constructeur d'un objet de classe Graphique:
        
        parmetre: deux annees an1 et an2, la donnee recherchee, l'origine (sociale), le nom de
                  l'image du graphique et le style de graphique
        resultat: attribution des differentes valeurs aux differants attributs 'self' de
                  l'objet
        """
        self.annee1=an1
        self.annee2=an2
        self.donnee=don
        self.origine=ori
        self.name=Nm
        self.style=st
   
    def attribut(self,a,b,c,d,e):
        """
        Methode qui actualise les donnees de l'objet de classe Graphique exepte le style
        
        parametre: les attributs self de l'objet et 5 autres variables
        resultat: attribution des variables aux attributs self de l'objet sauf pour self.style
        """
        self.origine=a
        self.annee1=int(b)
        self.annee2=int(c)
        self.donnee=d
        self.name=e
        
    def Barre(self):
        """
        Methode qui appel la méthode graph_BAC() avec self.style="Barre"
        
        parametre: les attributs self de l'objet
        resultat: attribution du str "Barre" a l'attribut self.style
                  et appel la méthode graph_BAC() de paramètre self
        """
        self.style="barre"
        self.graph_BAC()
        
    def Courbe(self):
        """
        Methode qui appel la méthode graph_BAC() avec self.style="Courbe"
        
        parametre: les attributs self de l'objet
        resultat: attribution du str "Courbe" a l'attribut self.style
                  et appel la méthode graph_BAC() de paramètre self
        """
        self.style="courbe"
        self.graph_BAC()
        
    def graph_BAC(self):
        """
        Methode qui construit un graphique à l'aide des parametre self et de matplotlib
        
        parametre: les attributs self
        resultat: construction d'un garphique en pourcentage soit en courbe soit en barre selon self.style
                  répondant aux demandes entrees dans l'IHM et qui dont une image sera sauvegarder dans le dossier
                  Graphiques
        """
        if self.annee1>self.annee2:
            self.annee1,self.annee2=self.annee2,self.annee1
            pourcent=toutadmis_2(self.annee1,self.annee2,self.donnee,self.origine)
        else:
            pourcent=toutadmis_2(self.annee1,self.annee2,self.donnee,self.origine)
        plt.figure()
        x=pourcent[1]
        y=pourcent[0]
        plt.xticks(x,rotation = '90')
        plt.ylim(0,100)
        if self.style=="barre":
            plt.bar(x,y)
            for i in range(len(x)):
                plt.text(x[i]-(1/4),y[i]/2,y[i],rotation=90)
        else:
            plt.plot(x,y,'r',linewidth=2)
            plt.grid()
        plt.title("Représentation graphique en {} de réussite\nen {} dans la catégorie \n{} entre {} et {}".format(self.style,self.donnee,self.origine,self.annee1,self.annee2),
                  fontdict={'fontsize': 'medium', 'fontweight': 'bold'})
        plt.savefig('Graphiques/{}.png'.format(self.name))
        plt.show()
        
graph = Graphique(None,None,None,None,None,None)