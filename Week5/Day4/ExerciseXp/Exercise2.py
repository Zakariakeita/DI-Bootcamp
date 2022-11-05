# 🌟 Exercise 2: Working With JSON
# Instructions
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
            }
        }
   }
}"""

# Access the nested “salary” key from the JSON-string above.
data = json.loads(sampleJson)
print(data['company']['employee']['payable']['salary'])
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
data['company']['employee']['birth_date'] = "1999-12-08"
# Save the dictionary as JSON to a file.
file_name = "/Users/macbookpro/Desktop/DI-Bootcamp/Week5/Day4/ExerciseXp/exercise2.json"
with open(file_name,"w") as f:
    json.dump(data,f,indent=2,sort_keys = True)
