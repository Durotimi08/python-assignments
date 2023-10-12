temp = input("what is the temperature(C)? \n" )

if int(temp) < 80: 
    print("The weather is cold and windy") 
elif int(temp) >= 80:
    print("The weather is sunny")


val = input("Input the value you would like to check \n")
if int(val) % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")