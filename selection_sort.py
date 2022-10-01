import random
import time


def generate_random_height(digit):
    heights = []
    for i in range(digit):
        random_height = random.randint(150, 190)
        heights.append(random_height)
    return heights


def selection_sort(heights, sleep_time):
    for i in range(len(heights)-1):
        print(
            f"------------------------------- round {i} -------------------------------\n")
        time.sleep(sleep_time)
        for j in range(i + 1, 0, -1):
            if(heights[j-1] <= heights[j]):  # 如果前面的比後面的小，就不用交換
                print("== sorted == \n")
                break
            elif(heights[j-1] > heights[j]):  # 如果前面的比後面的大，就交換
                print("======== switch =========")
                print(heights, f"第 {j} 個 -> {heights[j]}\n")
                print(" ", "     "*(j-1), "|\n ",  "     "*(j-1), "V")
                temp = heights[j]
                heights[j] = heights[j-1]
                heights[j-1] = temp
                print(heights, "\n")
            time.sleep(sleep_time)
    return heights


def main():
    digit = int(input("您要創造多少個身高？"))
    heights = generate_random_height(digit)
    print(f"\n原始資料 {heights} \n")
    sleep_time = int(input("一回合要展示幾秒？"))
    sorted_heights = selection_sort(heights, sleep_time)
    print(f"sorted heights: {sorted_heights}")


main()
