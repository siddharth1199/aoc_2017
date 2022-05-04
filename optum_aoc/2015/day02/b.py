def wrapping_paper(lines):
    total=0
    for i in range(len(lines)):
        word=lines[i].split('x')
        intlist = [int(x) for x in word]
        total= total+(2*intlist[0]*intlist[1])+(2*intlist[1]*intlist[2])+(2*intlist[2]*intlist[0])
        intlist.remove(max(intlist))
        total = total + (intlist[0]* intlist[1])
    return(total)


def ribbon(lines):
    total=0
    for i in range(len(lines)):
        word=lines[i].split('x')
        intlist = [int(x) for x in word]
        total = total+(intlist[0]* intlist[1]* intlist[2])
        intlist.remove(max(intlist))
        total = total + ((2*intlist[0])+ (2*intlist[1]))
    return(total)


def main():
    with open("input.txt") as raw_data:
        data = raw_data.read()
    lines = [x for x in data.strip().split('\n') if x]
    print("Total square feet of wrapping paper: {}".format(wrapping_paper(lines)))
    print("total feet of ribbon: {}".format(ribbon(lines)))


if __name__ == "__main__":
    main()
