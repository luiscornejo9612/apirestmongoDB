from pymongo import MongoClient

# Configurar la conexión a la base de datos MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['films']
collection = db['film']