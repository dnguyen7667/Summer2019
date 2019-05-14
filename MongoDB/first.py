# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
# Run mongodb server
#   mongod --config /usr/local/etc/mongod.conf
import pymongo

# MongoDB will create the database if it does not exist,
# and make a connection to it
my_client = pymongo.MongoClient('mongodb://localhost:27017/')

# List of system databases
print(my_client.list_database_names())

# Get database
my_db = my_client['mydatabase']

# Creates collection 'customers' if it doesn't already exists and returns it
customer_collection = my_db['customers']

# Insert document into 'customer' collection
inserted_document = customer_collection.insert_one(
    {'name': 'John', 'address': 'Highway 37'})

# Insert document into 'customer' collection with specified id
inserted_document = customer_collection.insert_one(
    {'_id': 1, 'name': 'Greg', 'address': '54321 Made Up'})
print('Inserted document with specified id: ' +
      str(inserted_document.inserted_id))

# Prints the latest document object id that has been inserted
print('Inserted document: ' + str(inserted_document.inserted_id))

# Insert multiple documents
inserted_documents = customer_collection.insert_many([
    {'name': 'Sarah', 'address': '2134 Valley Lane'},
    {'name': 'Smith', 'address': '5124 Highway St.'}
])
print('Inserted documents..')
for document_id in inserted_documents.inserted_ids:
    print('\t' + str(document_id))

# print each document's data (all columns) in 'customer' collection
for document in customer_collection.find():
    print(document)

# print specified document's data in 'customer' collection
#   excluding the 'address'
print('Specified data')
for document in customer_collection.find({}, {'address': 0}):
    print('\t' + str(document))

# Make a update to a document
query = {'address': 'Highway 37'}
new_values = {'$set': {'name': 'George'}}
if customer_collection.update_one(query, new_values):
    print('Values updated successfully')
else:
    print('Could not update values')

# Print collection after update
for document in customer_collection.find():
    print(document)

# Return list of collection in database
all_collections = my_db.list_collection_names()
print(all_collections)

# Sees if a collection by the name customers exists
if 'customers' in all_collections:
    print("The collection exists.")

# Drop 'customer' collection
if customer_collection.drop():
    print('Dropped an existing collection')
else:
    print('Collection cannot be dropped since it doesn\'t exist')
