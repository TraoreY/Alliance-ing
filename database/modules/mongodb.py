from pymongo import MongoClient
# se connecter à MongoDB, modifier le << MONGODB URL >> pour refléter votre propre chaîne de connexion
client = MongoClient("mongodb+srv://root:root@database.juhpb.mongodb.net/database?retryWrites=true&w=majority")
# Client.databasename
db = client.database

# Add, get, delete and update for actualites
def add_Actualites(namepost, uriimg, descriptionpost):
    #Etape 2: Créer des exemples de données
    post = {
            'namepost': namepost,
            'uriimg': uriimg,
            'descriptionpost': descriptionpost
        }
    #Etape 3: Insérer l'objet métier directement dans MongoDB via isnert_one
    result = db.actualites.insert_one(post)
    #Etape 4: Imprimer sur la console l'ObjectID du nouveau document
    return f'Enregistré dans en tant que : ', {result.inserted_id}

#Get all actualites
def get_Actualites_All():    
    result = list(db.actualites.find({}))

    return result

#Get One actualites
def get_Actualites_One(namepost):
    result = db.actualites.find_one({'namepost':namepost})

    return result

#Delete an actualites
def delete_Actualites(namepost):
    result = db.actualites.delete_one({'namepost':namepost})

    return result



#Update an actualites

# filter = {'name':'name'}
# newvalues = {"$set": {'name':'name', 'uriimg':'uriimg', 'descriptionformation':'descriptionformation'}}

def update_Actualites(filter, newvalues):
    result = db.actualites.update_one(filter, newvalues)

    return result

# Add, get, delete and update for Formations
def add_Formation(nameformation, uriimg, descriptionformation):
    #Etape 2: Créer des exemples de données
    post = {
            'nameformation': nameformation,
            'uriimg': uriimg,
            'descriptionformation': descriptionformation
        }
    #Etape 3: Insérer l'objet métier directement dans MongoDB via isnert_one
    result = db.formations.insert_one(post)
    #Etape 4: Imprimer sur la console l'ObjectID du nouveau document
    return f'Enregistré dans en tant que : ', {result.inserted_id}

#Get all Formation
def get_Formation_All():    
    result = list(db.formations.find({}))

    return result

#Get One Formation
def get_Formation_One(namepost):
    result = db.formations.find_one({'namepost':namepost})

    return result

#Delete an Formation
def delete_Formation(namepost):
    result = db.formations.delete_one({'namepost':namepost})

    return result


#Update an Formation

# filter = {'name':'name'}
# newvalues = {"$set": {'name':'name', 'uriimg':'uriimg', 'descriptionformation':'descriptionformation'}}

def update_Formation(filter, newvalues):
    result = db.formations.update_one(filter, newvalues)

    return result


# data = get_Actualites_All()  

# print(data)  

# add_Actualites('dgd', 'gg', 'dgjdhjgfdhjfgjhfg')
# add_Actualites('zezeze', 'ccsds', 'xwccwwcxw')
# add_Actualites('ezrtyt', 'oujijk', 'dsddsggdgstgfs')