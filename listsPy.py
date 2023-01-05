if __name__ == '__main__':
    N = int(input())
    listC = []
    for _ in range(N):
        nCommand, *line = input().split()
        nums = list(map(int,line))
        
        if nCommand == 'insert':
            listC.insert(nums[0],nums[1])
        elif nCommand == 'print':
            print(listC)
        elif nCommand == 'remove':
            listC.remove(nums[0])
        elif nCommand == 'append':
            listC.append(nums[0])
        elif nCommand == 'sort':
            listC.sort()
        elif nCommand == 'pop':
            listC.pop()
        elif nCommand == 'reverse':
            listC.reverse()
