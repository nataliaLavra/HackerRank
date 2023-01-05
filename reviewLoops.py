# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    word = str(input())
    even = ''
    odd = ''
    for i in range(len(word)):
        if i % 2 == 0:
            even+=word[i]
        else:
            odd+=word[i]
    print('{} {}'.format(even,odd))
