import pickle

d1 = {}

d1['name'] = 'kuldeep'
d1['school'] = 'sjsu'
d1['city'] = 'san jose'
d1['id'] = 252666


print "before pickling \n",d1 

#PICKLING
#f1 = open("pickled_data", "w")
f1 = open("pickled_data", "wb")
pickle.dump(d1, f1)
f1.close()

#UNPICKLING
f1 =open("pickled_data", "rb")
d1 = pickle.load(f1)
f1.close()

print "after pickling \n", d1
