import urllib
from urllib import request
import json

def function():
    #This will open the url
    webUrl=request.urlopen("https://jsonplaceholder.typicode.com/posts")
    #webUrl.getcode results HTTP status code
    print("HTML Response: " + str(webUrl.getcode()))
    #data ha json object
    data=webUrl.read()
  #  print(data)


    # Use the json module to load the string into dictionary
    #jsonVar=json.loads(data)

    file=open("/Users/amitsingh/Desktop/pythonPractice/dummy.json",'r')
    data=file.read()
    #print(data)

    jsondata=json.loads(data)
    print("__________________________________________________")
    print(jsondata)
    print("__________________________________________________")
    print("Value of isbn key is " + str(jsondata["isbn"]))
    print("Value of editor key is " + str(jsondata["editor"]))
    print("Value of editor key is " + str(jsondata["editor"]["lastname"]))
    print("______________________________________________________________________")

    ################# Lets loop over an index and print the details ##############

    for (key,value) in jsondata.items():
      print("key:"+key)
      print("value:"+str(value))








  #  with file as jsonblocks:
      #jsonblocksvalue=json.load(jsonblocks)
     # print(jsonblocks)
    # Use the json module to load the string into dictionary


function()
