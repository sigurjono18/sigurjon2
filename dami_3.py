n = int(input("Enter the length of the sequence: ")) # Do not change this line

devisor = 1
tala_1 = 1
tala_2 = 2
tala_3 = 3
tala_4 = 6

if n > 3:
    print(tala_1)
    print(tala_2)
    print(tala_3)
if n == 1:
    print(tala_1)
elif n == 2:
    print(tala_1)
    print(tala_2)
elif n == 3:
    print(tala_1)
    print(tala_2)
    print(tala_3)
else:
    for x in range(n-3):
        #print(tala_4)
        tala_4 = tala_1 + tala_2 + tala_3
        tala_1 = tala_2
        tala_2 = tala_3
        tala_3 = tala_4
        print(tala_4)

#devisor += 1