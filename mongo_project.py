import pymongo 
import os
from os import path
if path.exists("env.py"):
    import env

MONGODB_URI = os.getenv('MONGODB_URI')

DBS_NAME="MyTestDB"
COLLECTION_NAME="MyFirstMD"

def mongo_connect(url): 
    
    try:
        conn = pymongo.MongoClient(url)
        print("MONGO is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("NO MONGO: %s") %e

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print(~"You have selected to add a record")
        elif option =="2":
            print("You have selected to find a record by name")
        elif option =="3":
            print("You have selected to edit a record")
        elif option =="4":
            print("You have selected delete a record")
        elif option =="5":
            print("Exit")
            conn.close()
            break
        else:
            print("Invalid option")
        print("")
        #blank line

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()