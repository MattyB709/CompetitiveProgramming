cases = int(input())

def split_num(index, array:list) -> bool:
    num = array[index]
    if num < 10:
        return False
    # print(f"num: {num}, index: {index}")
    array[index] = num // 10
    array.insert(index+1,num % 10)
    if array[index] > array[index + 1] or array[index + 1] > array[index + 2]:
        return False
    elif index > 0 and array[index - 1] > array[index]:
        return split_num(index - 1, array)
    else:
        return True

for _ in range(cases):
    n = int(input())
    array = list(map(int, input().split()))
    i = 0
    case_works = True
    while i < (len(array) - 1) and case_works:
        # print("index: ", i)
        # print(*array)
        if array[i] > array[i+1]:
            case_works = split_num(i, array)
        i += 1

    if case_works:
        print("YES")
    else:
        print("NO")        
