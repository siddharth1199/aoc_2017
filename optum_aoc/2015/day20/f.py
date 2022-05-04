import math

def solve_part1(num_presents):
    house_num = 1
    num_present_per_house = 0
    
    while num_present_per_house < num_presents:
        num_present_per_house = 0 
        half_way = math.ceil(math.sqrt(house_num))
        for elf in range(1, half_way):
            if house_num % elf== 0:
                num_present_per_house += (elf * 10 + house_num / elf * 10)
        if half_way ** 2 == house_num:
            num_present_per_house += half_way * 10
        house_num += 1
        
    return house_num - 1
    
def main():
    num_presents = 33100000
    lowest_house_num = solve_part1(num_presents)
    print(lowest_house_num)

if __name__ == '__main__':
    main()