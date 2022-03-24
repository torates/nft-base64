import os
import json
import base64
from textwrap import indent

imgpaths = []
base64arr = []
finalJson = {}

def getImgs():
    for i in os.listdir():
        if i.endswith("png"):
            print(i + "added") #for debugging only
            imgpaths.append(i)
        else:
            print("not an img")
            continue
    print("Finished succesfully, please run encodeBase64")

def encodeBase64():
    for i in imgpaths:
        with open(i, "rb") as img_file:
            base64arr.append(base64.b64encode(img_file.read()).decode('utf-8'))

    print("images encoded succesfully, please create your json")

def jsonCreate():
    for i in base64arr:
        finalJson[str(base64arr.index(i) + 1)] = i
    with open("data.json", 'w') as output:
        json.dump(finalJson, output, indent=4)
    
