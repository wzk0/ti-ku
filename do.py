import sys
import os

type="*.yaml"
act="ls "+type+" >> temp.txt"
os.system(act)
result=[]
with open('temp.txt','r') as f:
	for line in f:
		result.append(line.strip('\n').split(',')[0])
os.system("rm temp.txt")
l=result[:-1]
want=max(l)
final=want[:-5]
real=int(final)+1
name=str(real)+".yaml"
do="cp model.x.yaml "+name+" && nano "+name
os.system(do)
choose=input("是否(y/n)更改高层文件:")
if choose=="y":
	os.system("rm most.txt && touch most.txt")
	with open("most.txt","w") as f:
		data=f.write(str(real))
else:
	pass
