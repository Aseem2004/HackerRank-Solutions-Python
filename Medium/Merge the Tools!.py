def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        uniq_string=[]
        for j in substring:
            if j not in uniq_string:
                uniq_string.append(j)
        
        print(''.join(uniq_string))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)