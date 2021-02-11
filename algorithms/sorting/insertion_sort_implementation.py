numbers = [5,9,3,10,45,2,0]


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


print(insertion_sort(numbers))