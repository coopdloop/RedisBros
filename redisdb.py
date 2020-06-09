import redis
import json

host = "dev1"
port = "6379"
pw = None
#datafile = r'citylots.json'

#data = json.loads(datafile)

#print(data)
'''data = {

    "sun" : "cream",
    "salsa" : "spicy",
    "valorant" : "yeeeee"
}

r.mset(data)
'''
#print(r.keys())


#for key in r.keys():
    #print("KEY : {} // VALUE : {}".format(key, r[key]))


def searchforsomething(value):
    r = redis.Redis(host=host, port=port, password=pw)
    for key in r.keys():
        #print(type(r[key]))
        if value == r[key].decode('utf-8'):
            print("Found!!!!")
            print("KEY : {} // VALUE : {}".format(key, r[key]))
            return key


#searchforsomething("spicy")
#r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

#print(r.get("Bahamas"))

#print(dir(r))

#for i in r.keys():
#    print(i)

#r.delete("Bahamas")

#print(r.keys())

#print(r.dbsize())