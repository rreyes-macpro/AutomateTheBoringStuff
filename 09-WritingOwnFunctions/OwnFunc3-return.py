def plusOne(number):
    try:
        return number + 1
    except TypeError:
        print('Please type numbers only!')

print('Type a number :')
number = input()
number = int(number) #global scope variable
#print(number)
latestnum = plusOne(number)
print('The method/function yields '+ str(latestnum))
      

