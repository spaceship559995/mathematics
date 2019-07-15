from random import random, shuffle

def chosen_balls(total, pick):
    nums = list(range(1, total+1))
    picked_nums = []
    for i in range(pick):
        shuffle(nums)
        picked_index = int(random() * (len(nums) - i))
        picked_num = nums.pop(picked_index)
        picked_nums.append(picked_num)
    return picked_nums


def choose_balls(total, pick):
    nums = list(range(1, total+1))
    picked_nums = []
    for i in range(pick):
        shuffle(nums)
        picked_index = int(random() * (len(nums) - i))
        picked_num = nums.pop(picked_index)
        picked_nums.append(picked_num)
    return picked_nums

while True:
    money = 0
    rank1 = 0
    rank2 = 0
    rank3 = 0
    rank4 = 0
    rank5 = 0
    point = 0
    b_point = 0
    num = int(int(input('얼마치를 사시겠습니까?'))/1000)
    x = chosen_balls(45, 7)
    a = x[:6]
    bonus = x[6]
    for i in range(num):
        b = choose_balls(45, 6)
        print(a, 'bonus = ', bonus, '\n')
        print(b, '\n' * 2)
        point = 0
        b_point = 0
        for fac in b:
            if fac in a:
                point += 1
            elif fac == bonus:
                b_point =1
        if point == 6:
            money += 2000000000
            rank1 += 1
        elif point == 5:
            if b_point == 1:
                money += 65000000
                rank2 += 1
            else:
                money += 1500000
                rank3 += 1
        elif point == 4:
            money += 50000
            rank4 += 1
        elif point == 3:
            money += 5000
            rank5 += 1
    print('1등 = ', rank1, '\n','2등 = ', rank2, '\n', '3등 = ',rank3, '\n', '4등 = ', rank4, '\n', '5등 = ', rank5, '\n', '낸 금액 = ', num*1000, '\n', '받은 상금 = ', money, '\n')
