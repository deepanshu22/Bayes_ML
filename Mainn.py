import numpy as np
from train_bayes import Input_train
from test_bayes import Input_test

file = open("tae.data","r")
train_file=open("train.data","w")
test_file=open("test.data","w")

data_arr=[]
fin_data=[]
for i in file:
	data_arr.append(i.strip('\n').split(','))

count_1=0
count_3=0
for i in data_arr:
	if i[5]=='1' or i[5]=='3':
		fin_data.append(i)

np.random.shuffle(fin_data)

fin_data=np.array(fin_data)
fin_data=np.split(fin_data,5)
for i in range(5):
	train_set=[]
	test_set=[]
	for j in range(5):
		if(j==i):
			test_set.extend(fin_data[j])
		else:
			train_set.extend(fin_data[j])
	lowfid,highfid,a,b=Input_train(train_set)
	accuracy=Input_test(lowfid,highfid,test_set,a,b)
	print accuracy

#print ""
#press=raw_input()
#if(press=='1'):
#	 train = int(len(fin_data)*.5)
#	 test = len(fin_data)-train
#	 train_set=[]
	# test_set=[]
	# count=0
	# for i in (fin_data):
	# 	if(count<train):
	# 		train_set.append(i)
	# 		train_file.write(str(i))
	# 		train_file.write('\n')
	# 	else:
	# 		test_set.append(i)
	# 		test_file.write(str(i))
	# 		test_file.write('\n')
	# 	count=count+1

	# lowfid,highfid,a,b=Input_train(train_set)

	# accuracy=Input_test(lowfid,highfid,test_set,a,b)
	# print accuracy
