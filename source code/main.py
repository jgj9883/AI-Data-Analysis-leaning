import random
random.seed(2021)
ranInt = [random.randint(-100,100) for _ in range(10)]
print(ranInt)
print('1번 = {} '.format(len(ranInt)))

print('2번 = {}, {} '.format(ranInt[0], ranInt[4]))

ranInt.append(80)

print(ranInt)

print(ranInt[ :3])


def myfunc_1(mylist):
    return [x for x in mylist if x > 0]

ranInt01  = myfunc_1(ranInt)
print(ranInt01)

def myfunc_2(mylist):
    return [x for x in mylist if x > 50]

ranInt02  = myfunc_2(ranInt)
print(ranInt02)

def myfunc_3(mylist):
    return [x/10 for x in mylist]

ranInt03  = myfunc_3(ranInt02)
print(ranInt03)