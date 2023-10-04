def solution(n,b):
    k = len(n);
    x = 0;
    y = 0;
    z = int(n,b);

    loop = [];
    loop.append(z);

    while True:
        sortedN = sorted(n);
        sortedN = ''.join(sortedN);
        x = int(sortedN[::-1],b);
        y = int(sortedN,b);
        z = x-y;
        #print("x: {} y: {} z:{}".format(x,y,z));
        n = baseString(z,b, k);

        #Check for constant value
        if (loop[-1] == z): return 1;

        #Check for looping value
        loop.append(z);
        firstOccurence = -1;
        secondOccurence = -1;

        for i in range(len(loop)):
            if (loop[i] == z):
                if (firstOccurence == -1): firstOccurence = i
                else: secondOccurence = i
                if secondOccurence != -1: return secondOccurence - firstOccurence

    return -1

def baseString(z,b,k):
    if (z == 0): return "0"
    temp = 0
    while z:
        temp*=10
        temp+=(int(z%b))
        z //=b

    #print (temp)

    temp = temp.__str__()
    while (len(temp) < k):
        temp = "0" + temp
    return temp.__str__()

print(solution("1121",10))
print(solution("210022",3))
print(solution("762",8))
print(solution("33120",4))
