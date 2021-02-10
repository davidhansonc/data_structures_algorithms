
def merge_sort(number_list):
    full_length = len(number_list)
    if full_length > 1:
        div_length = int(full_length / 2)
        first_half = merge_sort(number_list[:div_length])
        second_half = merge_sort(number_list[div_length:])
        return sort_return(first_half, second_half)
    elif full_length == 1:
        single_item = number_list[0]
        return single_item
    

def sort_return(first_half, second_half):
    if type(first_half) is not int:
        sorted_list = []
        index_i, index_j = 0, 0
        while index_i < len(first_half) and index_j < len(second_half):
            first_num = first_half[index_i]
            second_num = second_half[index_j]
            if first_num < second_num:
                index_i += 1
                sorted_list.append(first_num)
            else:
                index_j += 1
                sorted_list.append(second_num)
        sorted_list.extend(min(first_half[index_i:], second_half[index_j:]))
        sorted_list.extend(max(first_half[index_i:], second_half[index_j:]))
        return sorted_list
    else:
        return [min(first_half, second_half), max(first_half, second_half)]


numbers = [6, 3, 4, 1, 8, 7, 2, 5]
# numbers = [6, 3, 4, 1]
# numbers = [8, 7, 2, 5]
print(merge_sort(numbers))