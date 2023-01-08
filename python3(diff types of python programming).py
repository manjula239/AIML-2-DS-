#Traditional functional programming
TDS=[10,20,30,40,50]
i=0 #Initialize
for x in TDS:
    TDS[i]=x+10
    i=i+1 #increment
print(TDS)    

#covert above traditional functional programming to better in python
age=[1,2,3,4]
#i=0
#enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
for i,e in enumerate(age):
    age[i]=e+10
print(age)    

#convert above traditional functional programming to most efficient in python by using
#map is more effective, scalable and parallel process mechanism
#use map object insted of for loop
age=[1,2,3,4]
weight=[5,10,15]
def incr(e,f):
    return e+f+10

total=list(map(incr,age,weight))
print(total)

#let us write even shorter code using lambda
#lambda is anonymous function/in-line function
#note that lambda is used only when you don't want to re-use the function 
age=[1,2,3,4]
#i=0
age=list(map(lambda e:e+10,age)) #labda is replacing incr function here.
print(age)