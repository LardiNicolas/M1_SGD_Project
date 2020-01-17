class Avis:
    def __init__(self,id,d,j,n,ps):
        self.identifiant = id
        self.description = d
        self.jeu = j
        self.note = n
        self.pseudo = ps

    def getId(self):
        return self.identifiant

    def getDescription(self):
        return self.description

    def getJeu(self):
        return self.jeu

    def getNote(self):
        return self.note

    def getPseudo(self):
        return self = pseudo

    def setId(self,id):
        self.identifiant = id

    def setNomUser(self,ps):
        self.pseudo = ps

    def setDescription(self,d):
        self.description = d

    def setJeu(self,j):
        self.jeu = j

    def setNote(self,n):
        self.note = n

    def Affichage(self):
        print(
            "Identifiant : ",self.getId(),
            "Jeu : ",self.getJeu(),
            "Note : ",self.getNote(),
            "Commentaire : ",self.getDescription()
        )
