if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
arrList = list(arr)
arrList.sort(reverse=True)

for i in range(len(arrList)):
    if arrList[i] != arrList[i+1]:
        print(arrList[i+1])
        break
