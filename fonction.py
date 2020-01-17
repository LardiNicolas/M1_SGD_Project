from pymongo import MongoClient
from bson.objectid import ObjectId
user = "mongodb://nl435089:nl435089@mongo/?authSource=nl435089@authMechanisme=SCRAM-SHA-1"

#On récupère la connexion à mongoDB
c=MongoClient(user)
db=c.nl435089 #id : nl435089 mdp : nl435089  Pour Flavien
db.collection_name()

#Affiche tous les jeux disponibles sur le catalogue pour chaque catégorie :
def jeuxCatégorie():
    c = db.bibliotheque.aggregate([{"$unwind":"$categorie"},{"$sort":{"nom":1}},{"$group":{"_id":"$categorie","jeux":{"$push":{"nom":"$nom"}}}},{"$sort":{"_id":1}}])
    for doc in c :
        #Pour chaque catégorie on récupère les jeux et on les affiche
        print("Categorie "+ doc["_id"]+" :")
        for j in doc["jeux"]:
            print("\t" + j["nom"])
        print()

#Affichage des informations d'un utilisateur en ayant comme paramètre son pseudo
def informationUser(pseudo):
    c = db.CatalogueJeu.aggregate([{"$unwind" : "$avis"},{"$match" : {"avis.pseudo" : pseudo}},
                                   {"$group" : {"_id" : "$avis"}}])
    commentaire = False
    for doc in c:
        #Pour chacun des avis, on affiche les informations.
        print("\t" + "Note : " + str(doc["_id"]["notation"]))
        print("\t\t" + str(doc["_id"]["commentaire"]))
        print("")
        com = True
    if not commentaire :
        #Si aucun commentaire
        print("L'utilisateur " + pseudo + " n'a jamais laissé de commentaire.")

#Fait varier tous les prix en fonction d'un pourcentage donné, si pourcentage < 100 alors les prix baisseront sinon si pourcentage > 100 ils augmenteront
def VariationPrixGlobal(pourcentage):
    c = db.CatalogueJeu.find({"prix" : { "$exists" : True}});
    for doc in c:
        variation = ((pourcentage)*doc["prix"])/100
        db.CatalogueJeu.update({"nom":doc["nom"]},{"$set":{"prix":variation}})
        doc["prix"] = variation
        print("Le prix du jeu " + doc["nom"] + " a varié de " + str(pourcentage) + " pourcent. Le prix est maintenant de : " + str(doc["prix"]) + "euro.")

#Suppression des descriptions :
def SuppressionDescription():
    #On récupère tous les jeux, et on supprime l'attribut dans le document
    db.CatalogueJeu.update_many({"description" : {"$exists" : True}},{"$unset" : {"description" : ""}})
    print("Descriptions effacées")


