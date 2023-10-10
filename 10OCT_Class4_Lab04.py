# STRING FUNCTIONS
# Strings are immutable, whenever we perform a string functions. a new string will be created only reference will be changed but the previous content will be available in python memeory.

name="sanketh"
print(name)
result=name.capitalize()
print(result)

print(id(name))
print(id(result))

print(name.upper())
print(name.lower())

#SWAPCASE
name2= "SaNKetH"
print(name2.swapcase())

#TITLE CASE
print(name2.title())
s="hello world welcome"
print(s.title())

#Replace STRING
print(s.replace("world","Sanketh"))

#STRING Length - space is counted in length
print("String Length=",len(s))

#Find()  - Returns the index of substring in the string
index=s.find("world")
print(index)

#Count - Returns the number of times the character is repeated
print(s.count("l"))

#NONE - used to initialize a variable when we are not initializing it or dono the data it contain. ("In Python we don't have NULL")
val=None
print(val)
str=None
print(str)
str="Hello"
print(str)

#-------------------------LISTS
# List is a collection of items

Shopping_list=["iphone 15","Audi","airpods","MAC Book Air"]
print("Length of Shopping_List = ",len(Shopping_list))