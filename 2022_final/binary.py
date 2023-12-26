def binary_representation(lst):
    if len(lst) == 0:
        print(0)
    else:
        ans = 0
        for i in range(len(lst)):
            ans += lst[len(lst)-i-1]*(2**i)
        print(ans)
        
def main():
    binary_representation([1,0,1])
    binary_representation([1, 0, 1,1,0,0])
    
if __name__ == "__main__":
    main()