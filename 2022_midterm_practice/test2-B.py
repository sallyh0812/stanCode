def main():
    i = 5
    a = i//2
    b=stancode(i%2+2)
    if b:
        print("Answer 3:"+str(a))
    else:
        print('Answer 4:'+str(a))
        
def stancode(i):
    print("Answer 1:"+str(int(i+3.99)))
    i += 1
    a = i+stanCode(i)
    return a%2!=0

def stanCode(i):
    i /= 2
    print('Answer 2:'+str(i))
    return i


if __name__ == '__main__':
    main()