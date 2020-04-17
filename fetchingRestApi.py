import urllib
import json
from urllib import request

id = int(input("Enter the id for which you want to get the title"))


def function():
  weburl = request.urlopen('https://jsonplaceholder.typicode.com/posts')
  print(str(weburl.getcode()))
  statusCode = weburl.getcode()
  print(statusCode)

  if statusCode == 200:
    print("status code is 200")
    jsonfiledata = weburl.read()
    print(jsonfiledata)

    # Neeche diye gaye command se string object jo ki jsonfiledata hai wo
    # dictionary mein convert ho jayega

    '''Dekho neeche ek khela ye hai ki, jsondata mein actually jo bhi json hai, wo ek list k form mein hai
    jiske andar dictionary hai, toh ab hamein pahle list ke elements ki ginti jaan ni paregi, yaani ki kitni dictionary hai 
    fir usmein iterate kara ke ham items() method ki madad se saare element print karwa denge.'''
    jsondata = json.loads(jsonfiledata)
    count = len(jsondata)
    print(count)
    print(type(count))

    rangeval = range(count)

    for i in rangeval:

      # Iterating over a dictionary
      for (key, value) in jsondata[i].items():
        # print("key: " + key)
        # print("---------------------------------------")
        # print('value: ' + str(value))
        print(key + " : " + str(value))
        print("******************************************")


  else:
    print("status code is not 200")


'''The below function will take an id and print the book title from json data'''
def function1(id):
  print("Details for entered id is " + str(id))
  weburl = request.urlopen('https://jsonplaceholder.typicode.com/posts')
  print(str(weburl.getcode()))
  statusCode = weburl.getcode()
  print(statusCode)

  if statusCode == 200:
    print("status code is 200")
    jsonfiledata = weburl.read()
    print(jsonfiledata)

    # Neeche diye gaye command se string object jo ki jsonfiledata hai wo
    # dictionary mein convert ho jayega

    '''Dekho neeche ek khela ye hai ki, jsondata mein actually jo bhi json hai, wo ek list k form mein hai
    jiske andar dictionary hai, toh ab hamein pahle list ke elements ki ginti jaan ni paregi, yaani ki kitni dictionary hai 
    fir usmein iterate kara ke ham items() method ki madad se saare element print karwa denge.'''
    jsondata = json.loads(jsonfiledata)
    count = len(jsondata)
    print(count)
    print(type(count))

    rangeval = range(count)

    #for i in rangeval:
    print(type(id))

      # Iterating over a dictionary
    for (key, value) in jsondata[id-1].items():
        # print("key: " + key)
         #print("---------------------------------------")
         #print('value: ' + str(value))

         #print(key + " : " + str(value))
         print("******************************************")

    print("title of book with id no. "+str(id)+" is : "+jsondata[id]["title"])
  else:
    print("status code is not 200")


function()
function1(id)
