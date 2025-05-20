num1 = int(input("Coloque um número: "))
numlist = []

def replist():
    for i in range(1, num1 + 1):
        multi1 = i * str(i)
        comp = len(multi1)
        numlist.append(comp)
        print(numlist)
replist()