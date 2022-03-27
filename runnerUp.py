if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = [ i for i in arr]
    m = max(x)
    c = x.count(m)
    x.sort()
    print (x[len(x)-c-1])


