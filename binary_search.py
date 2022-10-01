import math
import time


def generate_heights():
    heights = []
    for i in range(1024):
        heights.append(i)
    return heights


def binary_search(heights, target):

    middle_index = int(len(heights) / 2)  # 取得中間的 index
    pivot = heights[middle_index]  # 取中間的值
    counter = 1

    if(pivot == target):
        return pivot, counter
    temp_array = heights  # initialize temp array

    print(temp_array)
    print("Pivot -> ", pivot)
    print("Counter -> ", counter)
    print("log2(n) -> ", int(math.log(len(heights), 2)))
    print("========================")
    time.sleep(5)

    while(pivot != target):  # 如果中間的值不是我們要找的值，就繼續找
        if(pivot > target):  # 如果中間的值比我們要找的值大，就往左邊找
            temp_array = temp_array[:middle_index]
        elif (pivot < target):  # 如果中間的值比我們要找的值小，就往右邊找
            temp_array = temp_array[middle_index:]

        if(counter > math.log(len(heights), 2)):  # 如果找了超過 log2(n) 次，就回傳 -1
            return -1, counter
        middle_index = int(len(temp_array) / 2)
        pivot = temp_array[middle_index]
        counter += 1

        print(temp_array)
        print("Pivot -> ", pivot)
        print("Counter -> ", counter)
        print("log2(n) -> ", int(math.log(len(heights), 2)))
        print("========================")
        time.sleep(5)
    return pivot, counter


def main():
    heights = generate_heights()
    target = int(input("請輸入要查詢的身高: "))
    # 回傳 index (沒找到就回傳 -1) 和 counter (找了幾次)
    index, counter = binary_search(heights, target)
    if(index == -1):
        print("查無此身高")
    else:
        print(f"身高 {index} 是第 {index} 個人")
    print(f"找了幾次: {counter}")


main()
