//On considère qu'on utilise la collection 'jeux'

//1: dump toute la bd
db.jeux.find();

//2: affiche la catégorie du jeu "Petanque Championship 2040"
db.jeux.find({ "nom": "Petanque Championship 2040" },
    { "Categorie": 1 });

//3: Affiche les noms les jeux dont le rpix est inferieur ou égal à 15
db.jeux.find({ "prix": { $lte: 15 } },
    { "nom": 1 });

//4: Affiche le nombre de catégories différentes
db.jeux.distinct("catégorie");

//5: Affiche le nombre de jeux MOBA dont le prix est superieur à 10
db.jeux.count({ "categorie": "MOBA", "prix": { gt: 10 } });

//6: Affiche le nombre d'avis par jeu
db.jeux.aggregate([
    { $unwind: "$avis" },
    {
        $group: {
            "_id": "$avis",
            "total": { $sum: 1 }
        }
    },
    { $sort: { "total": 1 } }
]);

//7: Calcul du prix total par Categorie
var map = function () {
    var px = { px: this.prix, count: 1 };
    emit(this.categorie, px)
};

var reduce = function (Collection, val) {
    rVal = { px: 0, count: 0 };
    for (var cpt = 0; cpt < val.length; cpt++) {
        rVal.count += val[cpt].count;
        rVal.px += val[cpt].px;
    };
    return rVal;
};

db.jeux.mapReduce(map, reduce, { out: { inline: 1 } })

//8: Ajout d'un commentaire au jeu "SCEP"
db.jeux.update({ "nom": "SCEP" },
    {
        $addToSet: {
            "avis":
            {
                "user": { "pseudo": "Flav" },
                "commentaire": "J'ai beaucoup aimé le film et ce jeu restranscrit parfaitement son histoire!",
                "notation": 8
            }
        }
    });

//9: Mise a jour de la catégorie portant l'acronyme MOBA avec le nom complet
db.jeux.updateMany({ "catégorie": "MOBA" },
    { $set: { "categorie": "Multiplayer online battle arena" } });


//10:renvoie les avis donnant plus de la moyenne
db.jeux.aggregate([
    { $unwind: "$avis" },
    { $match: { "avis.note": { $gt: 5 } } },
    {
        $group: {
            "_id": "$user.pseudo",
            "total": { $sum: 1 }
        }
    }
]);

//11 : Auteur ayant sorti le plus de jeux
db.jeux.aggregate([
    {$unwind:"$auteur"},
    {$group:{"_id":"$auteur.nom",
            "total":{$sum:1}}},
    {$sort:{"total":-1}},
    {$limit:1}
]);

//12: Moyenne générale des notes de la collection
var map = function () {
    var val = { note: 0, count: 0 };

    for (var i = 0; i < this.avis.length; i++) {
        val.note += this.avis[i].note;
        val.count += 1;
    }

    emit(val)
};

var reduce = function (val) {
    rVal = { note: 0, count: 0 };
    for (var cpt = 0; cpt < val.length; cpt++) {
        rVal.note += val[cpt].note;
        rVal.count += val[cpt].count;
    };
    rVal.avg = rVal.note / rVal.count;
    return rVal;
}

db.jeux.mapReduce(map, reduce, { out: { inline: 1 } });