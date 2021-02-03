numbers = [5,3,86,8,43,5]

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
    for idx in range(len(num_list)):
        smallest_num = max(num_list)
        for num in num_list[idx:]:
            if num < smallest_num:
                smallest_num = num
        num_list[idx] = smallest_num
    return num_list


def insertion_sort(num_list):
    sorted_list = []
    for num in num_list:
        print(sorted_list)
        if sorted_list == []:
            sorted_list.append(num)
        else:
            flag = True
            minimize = 10000
            for idx, value in enumerate(sorted_list):
                if num > value:
                    flag = False
                    # if idx < len(sorted_list)-1:
                    #     second_half = sorted_list[idx:]
                    #     sorted_list = sorted_list[:idx-1].append(num)
                    #     sorted_list.extend(second_half)
                    # else:
                    #     sorted_list.append(num)
            if flag:
                temp = sorted_list[:]
                sorted_list = [num]
                sorted_list.extend(temp)
    return sorted_list



# print(bubble_sort(numbers))
# print(selection_sort(numbers))
print(insertion_sort(numbers))