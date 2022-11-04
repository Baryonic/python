import math
import random
#from module_name import something


i1= 1
f1= 1.1
s1= "stRiNg 1"
str1="nevermind"
dataTypes={"numeric type","sequence type","boolean","sets","mapping type"}
imaginary1 = 1+1j
print(type(imaginary1))
multilinestring=""" line 1
line2
line 333 """
print(multilinestring)
print(type(multilinestring))
boolean1=True
tru=False
print(str(5<10)+str(not boolean1)+str(tru))
option=int(input("choose option (int):"))
print("calculating",float(i1-f1),float(i1)-f1)
print('x' in s1,'s' in s1, 'x' not in s1)
print("id(i1):",id(i1))
num1 = 5
num2 = 5
num3 = 1
print(num1 is num2, num3 is i1)
print(walrus:="walrus",walrus,type(walrus))
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||5")
if(option==3):
    print("option: 3")
elif(option==2):
    print("option: 2")
else:
    print("not option 3 or 2")
print("tema 6")
print(math.sqrt(4),math.fabs(-5),math.floor(4.6),math.pow(2,12),math.trunc(7.9999))
print(math.factorial(7))
angle1deg=float(input("angle in degrees?"))
print(rad1:=math.radians(angle1deg),"in radians")
print(math.sin(rad1),math.cos(rad1),math.tan(rad1))
print(math.pi,math.tau,math.e,-math.inf)
print("randoms")
random.seed(1234)#to initialize the random number generator
print(random.random(),random.randrange(0,122,11),random.randint(61,67))
sequence=[1,2,3]
sequ=("wan","two","tree")
#fix this shit #print(random.choice(sequ),random.shuffle(sequ))
print(math.fabs(200.9))
print("random {} data {} using .format".format(str1,s1))
print("random {1} data {0} using .format".format(str1,s1))
print(f"num1 and num2 = {num1+num2}")
print(str1[0],str1[-1])
print(str1[::2])
str1=(str1+s1)*2
print(str1.join([str1,"te echo de menos"]))
print(str1.capitalize())
print(str1.count('r'))
print(str1.find('x')) #throws -1 if not found
print(str1.index('s')) #throws error if not found
print(str1.isalnum(),str1.isalpha(),str1.islower(),str1.isupper())
print(str1.lower(),str1.replace('e','r'),str1.strip(),str1.upper())
#all string methods return new values, they do not change the original string
print(len(str1))
print(list(range(0,30,3)))
line=""
for x in str1:
    line=line+(x*2)
for x in range(3):
    print(line+"eeeeeeeeee")
d=0
while(d<len(str1)):
    #print(str1[d])
    d=d+1
for h in str1:
    if h=='t':
        break
else:   
    print(h)
print("||||||||||||||||||||||||||||||||||||||||||||||lists")
list1=[]
list2=[False,'e',"hello",34,3.4]
print(list2)
list3=list2*3+list1
print(list3,list3[1]*77)
for x in range(0,len(list2),option):
    del list3[x]
print(list3)
del(list1)
list4=[12,34,56,7,987,24]   
print("hello?","hello" in list3,min(list4),max(list4))
list3.append(list4)
list3=list3+list4
list3.insert(4,"insert")
print("pop",list3.pop())
list3.remove('e')
list3.reverse()
print(list3.index("insert"))#returns first element matching
print(list3.count("hello"))
for x in range(0,70,7):
    list3.insert(x,x)
print(list3*6)
list5=[x for x in range(0,70,7)if x%7==0]
print(list5)
list6=[x for x in str1]
print(list6)
print("||||||||||||||||||||||||||||||||||||||||||||||lists")
dict1={1:"hello",2:"world",3:True,"tru":False}
print(dict1)
dict1[4]="dicitonary"
print(dict1)
#del(dict1[4])
print(dict1.keys())
print(dict1.values())
#dict1.clear()    this empties the dictionary 
print(dict1.get(4),dict1.get(46))
print(dict1.items(),type(dict1.items()))
dict1.update({12:"12",13:"13","list7":["1","3","7"]})
print(dict1)
dict1["list7"].append("13")
dict1["list7"].remove("3")
print(dict1)
print("_________________________")
for i in dict1:
    print(i)
print("_________________________")
for i in dict1.values():
    print(i)
print("_________________________")
print("---------------------------------SETS")
#sets cannot contain lists
data1=set() #defining an empty set
data2={1,4,2,6,8,3,5,7,11,13,17}
data3={1,2,3,4,5,6,7,8,9,11,88,99}
data4={10,12,14,16,18,20,22,24,26,28,8,6,4,2}
num4=0
for number in data2:#loop ot access set elements
    num4=num4+number
    print(number)
print(num4)
print(data2|data3|data4)#union
print(data2.union(data3).union(data4))#union
print(data2&data3&data4)#intersection
print(data2.intersection(data3).intersection(data4))#intersection
print(data2-data4)#difference
print(data2.difference(data4))
print(len(data2),max(data2),min(data2),sorted(data4))
print(sum(data4))
data1.add(1)#does not add sets,neither does the '+' opperand
print(data1.copy())#copy of the set, XD?
print(data1.isdisjoint(data4),data1.issubset(data2),data2.issuperset(data1))
print("true?")
print(data4.pop())#pops last element, takes no argument
print(data4.remove(22))
data4.discard(24)#removes an element if it is a member
data4.update(data2|data3)#updates itself with the union of the other
print(data4)
print("--------------------------------------------FUNCTIONS")
def function1():
    print("function 1 called")
function1()
def function2():
    return "function 2 returned"
print(function2())
def function3(numm=5): #will use 5 as a value for 'numm' if not given any
    return numm**numm
print(function3(6)," function3(6) returned") #here it uses '3' as a value for 'numm'
print(function3()," function3() returned") #here it uses '(5)' as a value for 'numm'

addd=lambda nm1,nm2: nm1+nm2#'def(nm1,nm2):'  would also work
print(addd(11,55))







