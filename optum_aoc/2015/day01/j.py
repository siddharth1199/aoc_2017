filepath='input.txt'

def find_floor(file):
    count=0
    char_basement=''
    with open(file) as opened_file:
        for content in opened_file:
            for i in range(len(content)):
                if content[i] == '(':
                    count += 1
                if content[i] == ')':
                    count -=1
    return count

def find_pos(file):
    count=0
    position_basement=0
    with open(file) as opened_file:
        for content in opened_file:
            for i in range(len(content)):
                if content[i] == '(':
                    count += 1
                if content[i] == ')':
                    count -=1
                if count == -1:
                    position_basement=i+1
                    break
    return position_basement

def main():
    print("What floor do the instructions take Santa: ", +find_floor(filepath))
    print("Position of the character that causes Santa to first enter the basement:", +find_pos(filepath))

if __name__ == "__main__":
    main()