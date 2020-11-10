import os



def getShiftedString(s, leftShifts, rightShifts, a=None):
    # Write your code here
    k=len(s)
    i=1;j=0;
    if leftShifts > 0:
        for i in k:
            for j in i:
              a[j]=s[i]
              print(a[j])
            j=j+1
        i=i+1


            




if __name__ == '__main__':
    ptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    leftShifts = int(input().strip())

    rightShifts = int(input().strip())

    result = getShiftedString(s, leftShifts, rightShifts)

    fptr.write(result + '\n')

    fptr.close()