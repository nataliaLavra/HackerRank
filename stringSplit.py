def split_and_join(line):
    newLine = line.split(" ")
    newLine = "-".join(newLine)
    return newLine

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
