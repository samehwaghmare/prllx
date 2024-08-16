from firebase import firebase
import time

def readFirebase():
    firebase1 = firebase.FirebaseApplication('https://vs-code-77905-default-rtdb.firebaseio.com/', None)
    fire = firebase1.get('/nmims/fire', None)
    light = firebase1.get('/nmims/light', None)
    water = firebase1.get('/nmims/water', None)
    print(fire,light,water)
    return(fire,light,water)

def writeFirebase(count):
    firebase1 = firebase.FirebaseApplication('https://vs-code-77905-default-rtdb.firebaseio.com/', None)
    result = firebase1.put('nmims/','people',count)
    print(result)
