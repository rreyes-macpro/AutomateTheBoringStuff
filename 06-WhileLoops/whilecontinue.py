#while continue sample
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3: #when the variable reached this value,
        # it will skip and will not print
        continue
    print('spam is ' + str(spam))
