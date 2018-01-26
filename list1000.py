#Kiera McMurtrie
#1/24/2018
#Computer Programming

n = ['Bob', 'Jeff', 'Billy', 'Joe', 'Kate'] 
def list(n):  #Passes list
    x = input('Do you want to add a name to the list?(y/n) ')
    if x == 'y':
        xx = input('New name: ')
        n.append(xx)
        list(n)  #Repeats until inputed 'n'
    elif x == 'n':
        print(n)
    else:
        print('Invalid Input')
        list(n)

list(n)
