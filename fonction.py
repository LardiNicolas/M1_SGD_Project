from pymongo import MongoClient
from bson.objectid import ObjectId
uri="mongodb://fr108211:fr108211@mongo/?authSource=fr108211&authMechanism=SCRAM-SHA-1"

#On recupère la connexion à mongoDB
c=MongoClient(uri)
db=c.fr108211
db

#Affiche tous les jeux disponibles sur le catalogue pour chaque categorie :
def jeuxCategorie():
    c = db.jeux.aggregate([{"$unwind":"$categorie"},{"$sort":{"nom":1}},{"$group":{"_id":"$categorie","jeux":{"$push":{"nom":"$nom"}}}},{"$sort":{"_id":1}}])
    for doc in c :
        #Pour chaque categorie on recupère les jeux et on les affiche
        print("Categorie "+ doc["_id"]+" :")
        for j in doc["jeux"]:
            print("\t" + j["nom"])
        print()

#Affichage des avis publiés par un utilisateur
def informationUser(pseudo):
    c = db.jeux.aggregate([{"$unwind" : "$avis"},{"$match" : {"avis.user.pseudo" : pseudo}},
                            {"$group" : {"_id" : "$avis"}}])
    commentaire = False

    for doc in c:
        #Pour chacun des avis, on affiche les informations.
        print("\t" + "Note : " + str(doc["_id"]["note"]))
        print("\t\t" + str(doc["_id"]["commentaire"])+"\n")
        commentaire = True
    if not commentaire :
        #Si aucun commentaire
        print("L'utilisateur " + pseudo + " n'a jamais laisse de commentaire ou n'existe pas.")


#Fait varier tous les prix en fonction d'un pourcentage donné pour simuler des soldes
def VariationPrixGlobal(pourcentage):
    c = db.jeux.find({"prix" : { "$exists" : True}});
    for doc in c:
        variation = ((pourcentage)*doc["prix"])/100
        db.jeux.update({"nom":doc["nom"]},{"$set":{"prix":variation}})
        doc["prix"] = variation
        print("Le prix du jeu " + doc["nom"] + " a varie de " + str(pourcentage) + " pourcent. Le prix est maintenant de : " + str(doc["prix"]) + "euro.")

#Suppression des descriptions :
def SuppressionDescription():
    #On recupère tous les jeux, et on supprime l'attribut dans le document
    db.jeux.update_many({"description" : {"$exists" : True}},{"$unset" : {"description" : ""}})
    print("Descriptions effacees")


#jeuxCategorie()
informationUser(input("Entrez le nom d'un utilisateur pour avoir ses commentaires: \n"))
#VariationPrixGlobal(90)
#SuppressionDescription()