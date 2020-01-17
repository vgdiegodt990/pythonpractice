# This porgram says hello and asks for name
print('Hello world!')
print('What is your name?') #ask for their name 

myName = input()
print('It is good to meet you, ' + myName)

print('The length of your name is: ' + str(len(myName)))
# print(len(myName))

print('What is your age?') #ask for their age 
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

print('You will be ' + str(int(myAge) + 23) + ' in a long time.')