import random
import time


def generate_random_height(digit):
    heights = []
    for i in range(digit):
        random_height = random.randint(150, 190)
        heights.append(random_height)
    return heights


def quick_sort(heights):
    if len(heights) <= 1:
        return heights
    pivot = heights[0]
    left = []
    right = []
    for i in range(1, len(heights)):
        if heights[i] < pivot:
            left.append(heights[i])
        else:
            right.append(heights[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


def main():
    digit = int(input("您要創造多少個身高？"))
    heights = generate_random_height(digit)
    print(f"\n原始資料 {heights} \n")
    sorted_heights = quick_sort(heights)
    print(f"sorted heights: {sorted_heights}")


main()
