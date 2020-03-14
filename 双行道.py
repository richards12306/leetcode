length = input('input:')
doubleroad=[]
leftroad = input('input:')
rightroad = input('input:')
doubleroad=[leftroad,rightroad]
leftroad=[]
rightroad=[]
stack = []
 
for j in doubleroad[0]:
	leftroad.append([j,0])
for j in doubleroad[1]:
	rightroad.append([j,0])
doubleroad=[leftroad,rightroad]

