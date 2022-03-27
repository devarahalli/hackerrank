if __name__ == '__main__':
    x = int(input('Enter the value for x = '))
    y = int(input('Enter the value for y = '))
    z = int(input('Enter the value for z = '))
    n = int(input('Enter the value for n = '))

    r = [(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n ]
    print (r)