
import json
import requests

q= 'hilarious'
rating ='g'
key = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
limit = 2
url_string = f"https://api.giphy.com/v1/gifs/search?q={q}&rating={rating}&api_key={key}&limit={limit}"

response = requests.get(url_string)
print(response.status_code)


# If the status code is 200 return the result as a JSON object.
outfile = "/Users/macbookpro/Desktop/DI-Bootcamp/Week5/Day4/ExerciseXpGold/outputFile.json"

if response.status_code == 200:
    data = response.json()
    with open(outfile,"w") as f1:
        json.dump(data,f1,indent = 3)   

# Only return gifs which have a height bigger then 100.



# Return the length of the object you received in the previous question.
# Only return the first 10 gifs. Hint: In the Giphy Documentation, check out the relevant Request Parameters.









                     