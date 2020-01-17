class User:

    def __init__(self,ps,db,mdp,nbAvis):
        self.pseudo = ps
        self.database = db
        self.password = mdp
        self.nb_Avis = nbAvis

    def getPseudo(self):
        return self.pseudo

    def getDatabase(self):
        return self.database

    def getPassword(self):
        return self.password

    def getNbAvis(self):
        return self.nb_Avis

    def setPseudo(self,ps):
        self.nom = ps

    def setDatabase(self,db):
        self.database = db

    def setPassword(self,mdp):
        self.password = mdp

    def setNbAvis(self,nbAvis):
        self.nb_Avis = nbAvis

    def Affichage(self):
        print(
            "Utilisateur : ",self.getNom(),
            "Nombre d'avis : ",self.getNbAvis()
        )