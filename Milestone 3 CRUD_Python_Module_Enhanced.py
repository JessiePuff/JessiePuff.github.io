from pymongo import MongoClient
from bson.objectid import ObjectId

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
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]

    # CREATE: Insert a document into the collection
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Error inserting document:", e)
                return False
        else:
            return False

    # READ: Query documents from the collection
    # ENHANCEMENT
    def read(self, query=None):
        if query is None:
            query = {}

        try:
            cursor = self.collection.find(query)
            results = list(cursor)
            return results
        except Exception as e:
            print("Error reading documents:", e)
            return []

    # UPDATE: Modify document(s) in the collection

    # ENHANCEMENT
    def update(self, query, new_values):
        """
        Update document(s) in the collection.
        :param query: Filter for documents to update.
        :param new_values: Dictionary of fields to update.
        :return: Number of documents modified.
        """
        if not isinstance(query, dict) or not isinstance(new_values, dict):
           return 0
        try:
            result = self.collection.update_many(query, {"$set": new_values})
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
            return 0
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        
        except Exception as e:
            print("Error deleting documents:", e)
            return 0

        
        

