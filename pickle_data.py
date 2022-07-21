import pickle

file = "ref_name.pkl"
fileobj = open(file, 'rb')
mydata = pickle.load(fileobj)
print(mydata)