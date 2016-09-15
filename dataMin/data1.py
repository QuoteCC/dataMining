import math
import sys

#
#Colin Corliss
#Data Mining Assignment 1
#Data Used: UCI Iris Data
#https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
#

'''
A couple of notes about this:
Irises are initially sorted into 3 types, by name, these sets are then used to perform the analysis

When comparing 2 datasets, numbers returned are set 1 - set 2 (literally difference between set 1 and 2)

Ordering is Sepal Length, Sepal Width, Petal Length, Petal Width

The predict method takes in a set of 4 floats, and compares them to the means of each of the types of flowers.  These comparisons are evaluated
for which of the 3 values is closest to 0, then the flower type which has the most similar traits is returned as an int
i.e. will result in a set of 4 numbers between 0 and 2, the number which appears the most is returned.


KEY:
Iris-virginica is 0
Iris-Setosa is 1
Iris-Versicolor is 2
(printing Iris[key] will print the name)

'''


#highly specified, could be modified to generate the lists and colors from splitting a line one time
iris = ["Iris-virginica", "Iris-setosa","Iris-versicolor"]
typedData = [ [[],[],[], []], [[],[],[],[]], [[],[],[],[]] ] #3 lists of 4 lists, 1 for each flower

#method to get what iris type it is, returns int from 0-2 or -1 if invalid
def chkType(name):
	for i in range(0,3):
		if name == iris[i]:
			return i
	return -1


def stdDeviation(indx):
        #calculate mean, subtract each number from the mean, take mean of those, then sqrt
        tmp = mean(indx)
        tmp2 = []
        tmp3 = []
        x = 0
        for i in range(0, len(tmp)):
                tmp2 =[]
                for i2 in typedData[indx][i]:
                        tmp2.append(tmp[i]- float(i2))
                tmp3.append(tmp2) #tmp3 has all of the difference calculaions

        tmp2 = []
        for i in tmp3:
                for i2 in i:
                        x += i2
                x = round(x/ len(tmp3), 2) #mean then sqrt
                #print (x)
                x = math.sqrt(abs(x))
                tmp2.append(round(x,2))        
        
        
        return tmp2

def mean(y): #takes in flower num (0-2), returns list of means for the 4 data parts
        med = []
        x = 0
        for f1 in typedData[y]:
                x = 0
                for f2 in f1:
                        x += float(f2)

                med.append(round(x/len(typedData[y][0]), 2)) 
        return med

def predict(unknown):
        #given a datapoint, tries to figure out which flower type, returns 0-2
        test = [-1,-1,-1,-1]
        grt = [0,0,0]
        f0 = compare(unknown, mean(0))
        f1 = compare(unknown, mean(1))
        f2 = compare(unknown, mean(2))
        i = 0
        
        for i in range(0,4):
                test[i] = min([f0[i],f1[i],f2[i]])
                #print (f0[i])
                #print (f1[i])
                #print (f2[i])
                #print(min([f0[i],f1[i],f2[i]], key = float))
                if test[i] == f0[i]:
                        test[i] = 0;
                elif test[i] == f1[i]:
                        test[i] = 1
                elif test[i] == f2[i]:
                        test[i] = 2
                

        for i1 in test:
                if i1 == 0:
                        grt[0] += 1
                elif i1 == 1:
                        grt[1] += 1
                elif i1 == 2:
                        grt[2] += 1

        print ("Comparator Set: " + str(test))
        return (grt.index(max(grt)))



#second predictor, utilizes how much difference by summing the compares
def predictComp(unknown):
        f0 = compare(unknown, mean(0))
        f1 = compare(unknown, mean(1))
        f2 = compare(unknown, mean(2))
        sms = [sum(f0), sum(f1), sum(f2)]
        return(sms.index(min(sms)))
              
        

def compare(set1, set2): #pass in two sets, returns how close they are as a positive float
        tmp = []
        for p,q in zip(set1, set2):
               tmp.append(round(abs(p-q), 2))
        return tmp  



#takes in number from 0 to 2, and the name of the method to be run (mean or stdDeviation)
def printThing(num, method):
        tmp = method(num)
        print (method.__name__ +" of " + iris[num] + ": " + str(tmp))



#open file, read data
file = open(sys.argv[1], "r")
data = file.read()
file.close

s = data.splitlines()
x = 0


#sort data into correct section of lists
for line in s:
	line.strip()
	tmp = line.split(',') #tmp holds one line of data split by comma
	tpe = chkType(tmp[4])
	typedData[tpe][0].append(tmp[0])
        typedData[tpe][1].append(tmp[1])
        typedData[tpe][2].append(tmp[2])
        typedData[tpe][3].append(tmp[3])
        x += 1





#the below statements print out a count of the datapoints and a given set of

#6.8,2.8,4.8,1.4,Iris-versicolor
#6.8,3.2,5.9,2.3,Iris-virginica
        
for s in range(0,3):
        print("\n")
        printThing(s, mean)
        printThing(s, stdDeviation)
        

print("\nPrediction of randomly chosen single data point, should be: Iris-virginica")        
print(iris[predict([6.8,3.2,5.9,2.3])])
print(iris[predictComp([6.8,3.2,5.9,2.3])])



