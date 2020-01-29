# importing the request library
import requests
import json

# api-endpoint
URL = "https://jsonplaceholder.typicode.com/todos/1"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location} #This is parameters which are passed to url ? wale params
#like http://maps.googleapis.com/maps/api/geocode/json?address=delhi+technological+university

#Get Request
r=requests.get(url=URL)
print(r.json())
data=(r.json())

print(data['id'])
print(data['userId'])
print(data['title'])
state=str(data['completed']) #Converted bool i.e boolean object into string
print("The state is " + state)



#data=r.json()
#value=json.loads(data)
#print r;
#print json.dumps(data)




