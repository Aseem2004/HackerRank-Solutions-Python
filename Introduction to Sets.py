def average(array):
    user_set = set(array)
    length = len(user_set)
    array_sum = sum(user_set)
    result = array_sum/length
    return result
   

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)