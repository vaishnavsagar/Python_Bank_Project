import json
di = {"name" : input("What is your name"),
      "age" : input("What is your age")
      }

with open('database.json', 'w') as db :
    json.dump(di, db)
