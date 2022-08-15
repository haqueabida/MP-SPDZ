import os


import numpy as np



numrows= 32 #change this to add entries
#datamod=numrows*2
datamod = 48

setsize0 = 32
setsize1 = 32

path=os.getcwd()
path=path+'/Player-Data/Input-P0-0' #file gets created in Player-Data folder
f=open(path, 'w')


vals0 = np.random.permutation(datamod)[0:setsize0]
vals0 = 1+vals0
vals0.sort()

strvals = [str(i) for i in vals0]

f.write(' '.join(strvals))


print("Player events written successfully")


# close the file
f.close()





path=os.getcwd()
path=path+'/Player-Data/Input-P1-0' #file gets created in Player-Data folder
f=open(path, 'w')


vals1 = np.random.permutation(datamod)[0:setsize1]
vals1 = vals1+1
vals1.sort()

strvals = [str(i) for i in vals1[::-1]]

f.write(' '.join(strvals))



# close the file
f.close()
