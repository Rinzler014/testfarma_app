from pymongo import MongoClient

def get_db_handle(db_name):
    
    client = MongoClient("mongodb+srv://TESTFARMATST:3czzys7FtN6XysKr@testfarmatst.crr3uq1.mongodb.net/?retryWrites=true&w=majority")
    
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        
        db = client[db_name]
        
        return db
        
    except Exception as e:
        
        print(e)
        
        return None
    

# db = get_db_handle("testfarma")

# collection = db["medic_data"]

# documents = collection.find()

# new_id = 1

# for document in documents:
    
#     print(new_id)
#     # Actualizar el valor del ID en el documento
#     collection.update_one({'_id': document['_id']}, {'$set': {'id': new_id}})
    
#     # Incrementar el contador del nuevo ID
#     new_id += 1

# print("¡La actualización de los IDs ha sido completada!")


