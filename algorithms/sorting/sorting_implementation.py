# numbers = [5,3,86,8,86,43,3,5]
numbers = [5,9,3,10,45,2,0]
# numbers = [5,6,7,8,9]

def bubble_sort(num_list):
    sorting = True
    while sorting:
        sorting = False
        for index in range(len(num_list) - 1):
            if num_list[index] > num_list[index+1]:
                temp = num_list[index + 1]
                num_list[index + 1] = num_list[index]
                num_list[index] = temp
                sorting = True
    return num_list


def selection_sort(num_list):
    smallest_num = max(num_list)
    for idx in range(len(num_list)):
        for num in num_list[idx:]:
            if num < smallest_num:
                smallest_num = num
        num_list[idx] = smallest_num
    return num_list


def insertion_sort(num_list):
    count = 0
    for index, num in enumerate(num_list):
        count += 1
        sorted_list = num_list[:index]
        if index == 0 or num > max(sorted_list):
            continue
        elif num < min(sorted_list):
            temp = num_list.pop(index)
            num_list.insert(0, temp)
        else:
            for idx, value in enumerate(sorted_list):
                count += 1
                if num > sorted_list[idx] and num < sorted_list[idx+1]:
                    temp = num_list.pop(index)
                    num_list.insert(idx+1, num)
                elif num == value:
                    temp = num_list.pop(index)
                    num_list.insert(idx+1, num)
    return (f'{num_list} \n Number of comparisons: {count}')


# print(bubble_sort(numbers))
# print(selection_sort(numbers))
print(insertion_sort(numbers))