
def userInput():
    
    n = int(input("Enter number of elements: "))

    a = list(map(int,input("Enter the numbers in '' and space separated: ").strip().split()))[:n]

    return a

def varianceCal(b):

    sum  = 0.0
    sumC = 0.0
    i = 0

    b = userInput()

    while i < len(b):
        
        sum += b[i]
        sumC += b[i] * b[i]
        i +=1

    result = (sumC - (sum * sum) / len(b)) / (len(b)-1)

    print("The variance of the values is: {}".format(result))

varianceCal(userInput)