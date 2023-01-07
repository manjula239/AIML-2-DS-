#Strings
name=100
namesq='xyz'

print(type(name))
print(type(namesq))
name="A Manju"

#access string content
print(name[1])
print(name[2:6])

# modify string content
name[0]='A'

name2=name+'Hyd'
print(name2)
name=name+'xyz'
print(name)
name=name.upper()
name="mr"
name=name.capitalize()
print(name)
name='Manjula Devi'
#==================================================================
# name = concatenate(name,'10')
#
#===============================================================
name=name.replace('Manjula Devi','Devi Manjula')
print(name)
name=10

print(name)
isinstance(name,str) #true
isinstance(name,int) #false