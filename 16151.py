import math
import random
print "Current Invesment = "
current_invesment = int(raw_input())
print "Average return in decimals = "
average_return= float(raw_input())
print "st dev return in decimals = "
st_dev_return = float(raw_input())
print "Time to Retirement = "
time_to_retirement = int(raw_input())
print "Amount to invest anualy = "
amount_to_invest_anu = int(raw_input())
prob = 0
array = []
array1 = []
array2 = []


print "##########################################################################################################################"
def space(l):
		return l+(25-len(l))*" "

portfolio_size = [50,100,200,400]
arr = []
print space("Prob_Distribution Table")
for i in range (4):
		arr.append(float(portfolio_size[i])/750)
#print arr
cumu_prob = []
total_prob = []
cumu1 = 0
cumu = 0
for i in range(4):
	cumu += arr[i]
	cumu_prob.append(cumu)
	total_prob.append([int(cumu1*1),int((cumu*100)-1)])
	#print cumu*100
	cumu1 = int(cumu*100) +1

#print cumu_prob
#print total_prob


print space("Size_Portfolio"),space("Probability"),space("Cumulative_prob"),space("Range")
for i in range(4):
	print space(str(portfolio_size[i])),space(str(arr[i])),space(str(cumu_prob[i])),space(str(total_prob[i]))


print "##########################################################################################################################"
print space("Irr and End_value Table")

def norm_inv(prob,average_return,st_dev_return):

	pi = 3.14159
	x = 2*pi*average_return
	x = math.sqrt(x)
	y = (prob-average_return)/(2*(st_dev_return*st_dev_return))
	y = math.exp(-y)
	z = x*y
	return z*10
	#print z*99

def ending_value(current_invesment,irr,amount_to_invest_anu):
	end_value = current_invesment*(1+irr)+amount_to_invest_anu
	return end_value
def space(l):
		return l+(25-len(l))*" "

for i in range (20):
	array.append(i+1)
	prob = random.random()
	irr = norm_inv(prob,average_return,st_dev_return)
	array1.append(irr)
	end_value = ending_value(current_invesment,irr,amount_to_invest_anu)
	array2.append(end_value)
	

#print array
#print array1
#print array2



print space("year"),space("Return"),space("Ending_value")
for i in range(20):
	print space(str(array[i])),space(str(array1[i])),space(str(array2[i]))


print "##########################################################################################################################"
print space("Simulations")
ending_value = array2[-1]
#print ending_value
aray = []
for i in range(1000):
	aray.append(i+1)
	prob = random.random()
	irr = (1+norm_inv(prob,average_return,st_dev_return))
	sim = ending_value*irr+amount_to_invest_anu
	array2.append(sim)

print space("Simulation_itr"),space("end_value")

for i in range(1000):
	print space(str(aray[i])),space(str(array2[i]))

sum = 0
for i in range(1000):
	sum = sum+array2[i]
print "Mean =",sum/1000

array2.sort()
median = array2[500]
print "Median = ",median

mean = sum/1000
vari = 0
for i in range(1000):
	var = array2[i]-mean
	vari = vari + var

#print "Varience =",vari/1000
print "####################################### ACTURIAL METHOD ####################################################################"

current_invesment = 100000
average_return= 0.1120
st_dev_return = 0.18
time_to_retirement = 20
amount_to_invest_anu = 20000
prob = 0
array = []
array1 = []
array2 = []

print space("Mortality Table")
age = 60
print space("Age"),space("ProbofDeathin1year")
for i in range(20):
	age = age + 1
	array.append(age)
	prob = random.random()
	array1.append(prob)
	print space(str(array[i])), 
	print space(str(array1[i]))

print "#############################################################################################################################"

print space("Year"),space("ProbOfDeathIn20Year")
prob = 1
year = 0
array3 = []
for i in range(20):
	prob = prob * array1[i]
	year = year + 1
	array3.append(year)
	array2.append(prob)
	print space(str(array3[i])),
	print space(str(array2[i]))

print "#############################################################################################################################"

print space("TimeLine"),space("Age"),space("ProbOfDeathin1Year"),space("ProbOfDeathin20Year"),space("Expected OutPut")
arr = []
arr1 = []
arr2 = []
for i in range(20):
	Time = array3[i]-0.5
	arr.append(str(Time))
	print space(str(arr[i])),
	print space(str(array[i])),
	print space(str(array1[i])),
	print space(str(array2[i])),
	exp_op = array1[i]*200000
	arr2.append(exp_op)
	print space(str(exp_op))

pvOfPayouts_irr = 0.18
pr = 1
imp = []
add = 0
for i in range(20):
	pr = pr+2
	dr = math.pow(1.18,int(pr))
	pvl = arr2[i]/dr
	add = add + pvl

print "P.V. of PayOuts at 18% = ",add
	













