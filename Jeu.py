class Jeu:
    def __init__(self,id,n,db,dev,ed,no,des,a,cat):
        self.identifiant = id
        self.nom = n
        self.database = db
        self.developpeurs = dev
        self.editeur = ed
        self.note = no
        self.description = des
        self.avis = a
        self.categorie = cat

    def getIdentifiant(self):
        return self.identifiant

    def getNom(self):
        return self.nom

    def getDatabase(self):
        return self.database

    def getDeveloppeurs(self):
        return self.developpeurs

    def getEditeur(self):
        return self.editeur

    def getNote(self):
        return self.note

    def getDescription(self):
        return self.description

    def getCategorie(self):
        return self.categorie

    def setIdentifiant(self,id):
        self.identifiant = id

    def setNom(self,n):
        self.nom = n

    def setDatabase(self,db):
        self.database = db

    def setDeveloppeurs(self,dev):
        self.developpeurs = dev

    def setEditeur(self,ed):
        self.editeur = ed

    def setNote(self,no):
        self.note = no

    def setDescription(self,des):
        self.description = des

    def setCategorie(self,cat):
        self.categorie = cat

    def Affichage(self):
        print(
            "Nom du jeu : ",self.getNom(),
            "Categorie : ",self.getCategorie(),
            "Developpeur : ",self.getDeveloppeurs(),
            "Editeur : ",self.getEditeur()
        )
    

    
