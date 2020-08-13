import numpy
import math
import matplotlib.pyplot as plt
import csv

count=[0]*9
sum=0.0
rate=[0.0]*9
benford=[0.0]*9

#読み込み
f = open('JB.csv',encoding="utf-8_sig")
reader = csv.reader(f)
for line in reader :
    #data = line2.split(",")
    try:
        topnum = line[3][0]
        i=int(topnum)
        count[i-1]+=1
        sum+=1.0
    except ValueError :
        continue
f.close()
print(count)

#書き込み
#f2 = open('output_SP500.csv', 'w', newline="")
#writer = csv.writer(f2)
#writer.writerow(["number","rate","benford" ])
#f2.close()
for i in range(1,10):
    rate[i-1]=count[i-1]/sum
    benford[i-1]=math.log(i+1,10)-math.log(i,10)    
    #writer.writerow([i, rate[i-1], benford[i-1]])
print (rate)
plt.title("Benford's law")
plt.xlabel("Number")
plt.ylabel("Appearance Probability")
plt.grid(True)
plt.plot(range(1,10),benford)
plt.plot(range(1,10),rate)
plt.show()