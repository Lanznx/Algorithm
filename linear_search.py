import random


def generate_random_height():
    heights = []
    for i in range(1000):  # 產出 1000 個介於 150 ~ 190 的身高
        random_height = random.randint(150, 190)
        heights.append(random_height)
    return heights


def sum_of_list(heights):
    sum = 0
    for h in heights:  # 把大家的身高 h 一個一個加去 sum
        sum += h
    average = sum / len(heights)  # 計算平均身高
    return average


def linear_search(heights, target):
    for i in range(len(heights)):  # 一個一個比對
        if heights[i] == target:  # 如果有找到就回傳 index
            return i
    return -1


def main():
    heights = generate_random_height()
    print(f"大家的身高（前三十個）：{heights}")

    average = sum_of_list(heights)
    print("平均身高: ", average)

    target = int(input("請輸入要查詢的身高: "))
    index = linear_search(heights, target)
    if index == -1:
        print("查無此身高")
    else:
        print(f"身高 {target} 是第 {index} 個人")


main()
