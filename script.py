import pickle

r_dict = dict()

fileobj = open('highscore.txt','wb')
pickle.dump(r_dict,fileobj)
fileobj.close()