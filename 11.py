n = int(input('Введите целое число '))
def simple(n):
    flag = True
    for i in range(1,n+1):
        if i!=1 and i!=n and n%i == 0:
            return False
    return True
if __name__ == "__main__":
    print(simple(n))









