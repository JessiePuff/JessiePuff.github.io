import pymongo


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):

        # Connection Variables
        USER = 'aacuser'
        PASS = 'messieJessie'
        HOST = 'localhost'
        PORT = 27017
        DB = 'AAC'
        COL = 'animals'


        # Correct connection string with authSource=admin
        self.client = pymongo.MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]


        #Improve Create Method

        # CREATE: Insert a document into the collection
    def create(self, data):
        
        if data is None:
            print("Create Error: No data provided")
            return False

        if not isinstance(data, dict):
            print("Create Error: Data must be a dictionary")
            return False

        try:

            result = self.collection.insert_one(data)

            if result.acknowledged:
                print("Document inserted successfully")
                return True

            return False

        except Exception as e:
            print("Create Error:", e)
            return False

    # Improve Read Method
    # READ: Query documents from the collection
    # ENHANCEMENT
    # READ: Query documents from the collection
    # ENHANCED DATABASE VERSION
    def read(self, query=None):

        if query is None:
            query = {}

        if not isinstance(query, dict):
            print("Read Error: Query must be a dictionary")
            return []

        try:
            cursor = self.collection.find(query)
            
            results = list(cursor)

            print(f"Retrieved {len(results)} document(s)")
            
            return results

        except Exception as e:
            print("Error reading documents:", e)
            return []

    # UPDATE: Modify document(s) in the collection
    #Improve Update Method
    # ENHANCEMENT
    
    def update(self, query, new_values):
        """
        Update document(s) in the collection.
        :param query: Filter for documents to update.
        :param new_values: Dictionary of fields to update.
        :return: Number of documents modified.
        """

        if not isinstance(query, dict) or not isinstance(new_values, dict):
            print("Update Error: Query and values must be dictionaries")
            return 0

        if not query:
            print("Update Error: Query cannot be empty")
            return 0

        if not new_values:
            print("Update Error: No update values provided")
            return 0

        try:
            result = self.collection.update_many(
                query,
                {"$set": new_values}
            )

            print(f"Updated {result.modified_count} document(s)")
            return result.modified_count

        except Exception as e:
            print("Error updating documents:", e)
            return 0
    
    # DELETE: Remove document(s) from the collection
    def delete(self, query):
        """
        Delete document(s) from the collection.
        :param query: Filter for documents to delete.
        :return: Number of documents deleted.
        """
        if not isinstance(query, dict):
            print("Delete Error: Query must be a dictionary")
            return 0

        if not query:
            print("Delete Error: Query cannot be empty")
            return 0
        
        try:
            result = self.collection.delete_many(query)
            print(f"Deleted {result.deleted_count} document(s)")
            return result.deleted_count
        
        except Exception as e:
            print("Error deleting documents:", e)
            return 0

        
        

