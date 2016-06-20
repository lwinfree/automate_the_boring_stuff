
def collatz(number):

        if number%2==0:
            return(number//2)
                      

        elif number%2==1:
            return(3*number+1)
            
print('guess a number')
try:
    num=int(input())
except ValueError:
    print('type an integer')
num=int(input())

newNum=collatz(num)

while collatz(newNum) != 1:

            print(collatz(num))
            collatz(newNum)
            newNum=collatz(newNum)
            print(collatz(newNum))

