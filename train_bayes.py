import numpy as np


def Input_train(train_set):
	lowfid=[]
	highfid=[]
	first=[0]*3
	first_prob=[0]*3
	second=[0]*26
	second_prob=[0]*26
	third=[0]*27
	third_prob=[0]*27
	fourth=[0]*3
	fourth_prob=[0]*3
	fifth=[0]*67
	fifth_prob=[0]*67
	count_1=0
	count_3=0
	for i in train_set:
		if(i[5]=='1'):
			first[int(i[0])]+=1
			second[int(i[1])]+=1
			third[int(i[2])]+=1
			fourth[int(i[3])]+=1
			fifth[int(i[4])]+=1
			count_1+=1

	lowfid.append(first)
	lowfid.append(second)
	lowfid.append(third)
	lowfid.append(fourth)
	lowfid.append(fifth)


	first_1=[0]*3
	second_2=[0]*26
	third_3=[0]*27
	fourth_4=[0]*3
	fifth_5=[0]*67

	for j in train_set:
		if(j[5]=='3'):
			first_1[int(j[0])]+=1
			second_2[int(j[1])]+=1
			third_3[int(j[2])]+=1
			fourth_4[int(j[3])]+=1
			fifth_5[int(j[4])]+=1
			count_3+=1

	highfid.append(first_1)
	highfid.append(second_2)
	highfid.append(third_3)
	highfid.append(fourth_4)
	highfid.append(fifth_5)



	#print count_1,count_3
	prob_low=count_1/float(count_1+count_3)
	prob_high=count_3/float(count_1+count_3)
	for i in range(len(lowfid)):
		for j in range(1,len(lowfid[i])):
			#print lowfid[i][j]
			temp=lowfid[i][j]+1
			temp2=float(count_1+(len(lowfid[i])-1))
			prob= temp/temp2
			lowfid[i][j]=prob

	for i in range(len(highfid)):
		for j in range(1,len(highfid[i])):
			temp=highfid[i][j]+1
			temp2=float(count_1+(len(highfid[i])-1))
			prob= temp/temp2
			highfid[i][j]=prob

	return (lowfid,highfid,prob_low,prob_high)

