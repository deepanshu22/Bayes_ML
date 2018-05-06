import numpy as np

def Input_test(lowfid,highfid,test_set,prob_low,prob_high):
	prob_cal1=1
	prob_cal2=1
	bayes_test=[]
	testarr=[]
	check=10
	for i in test_set:
		#print lowfid[0][int(i[0])]
		prob_cal1*=prob_low*lowfid[0][int(i[0])]*lowfid[1][int(i[1])] *lowfid[2][int(i[2])]*lowfid[3][int(i[3])]*lowfid[4][int(i[4])]
		prob_cal2*=prob_high*highfid[0][int(i[0])]*highfid[1][int(i[1])]*highfid[2][int(i[2])]*highfid[3][int(i[3])]*highfid[4][int(i[4])]
		if prob_cal1<prob_cal2:
			bayes_test.append('3')
		else:
			bayes_test.append('1')
		testarr.append(i[5])


	flag=3
	fp=0.0
	tp=0.0
	tn=0.0
	fn=0.0
	for x in range(0,len(test_set)):
		if(bayes_test[x]=='3' and test_set[x][5]=='3'):
			tp+=1
			check+=1
		if(bayes_test[x]=='1' and test_set[x][5]=='1'):
			tn+=1
			check+=1
		if(bayes_test[x]=='1' and test_set[x][5]=='3'):
			fn+=1
			check+=1
		if(bayes_test[x]=='3' and test_set[x][5]=='1'):
			fp+=1
			check+=1

	tpr=tp/(tp+fn)
	check+=1
	fpr=fp/(tn+fp)
	check+=1
	print tp,fn,fp,tn
	print "True postive :",tpr,"False postive ",fpr
	for i in range(len(bayes_test)):
		if(bayes_test[i]==testarr[i]):
			flag+=1
	
	accuracy=100*(flag/float(len(bayes_test)))
	return accuracy