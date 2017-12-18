import random, sys
prod = 0
minnum = 5
maxnum = 10
interval = 5
target = 100
cnt = 0

while prod != target:
    myrandnum = random.randint(minnum, maxnum)
    myrandnummult = random.randint(minnum, maxnum)
    prod = myrandnum * myrandnummult
    print('The random number generated is '+ str(myrandnum) + ' and multiplied by '+ str(myrandnummult) + ' equals ' + str(prod))
    cnt = cnt + 1

print('The program generated ' + str(cnt) + ' random numbers upon reaching ' + str(target))


