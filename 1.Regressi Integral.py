#from sklearn import svm
from sklearn.svm import SVR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Database
FileDB = 'database.txt'
Database = pd.read_csv(FileDB, sep=",", header=0)
print ("---------------------")
print (Database)
#x = data, y = target
x = Database[[u'target']]
y = Database.target
#Fit model regresi
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_rbf.fit(x, y)
#Menampilkan data prediksi
xp = np.linspace(1, 21, 1)
n = len (xp)
print ("---------------------")
print ("----Integral-----")
print ("xp(i) rbf")
for i in range (n):
    rbf = svr_rbf.predict([[xp[i]]])
    print ('{:.2f}'.format(xp[i]), rbf)
print ("---------------------")

#Plot data prediksi
rbf2 = svr_rbf.predict(x)
plt.figure()
plt.plot(x, rbf2, color = 'red')
plt.scatter(x,y, color ='blue')
plt.title ('Hasil Integral Variasi Batas atas & Batas Bawah')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['rbf', 'data'],loc=2)
plt.show()
