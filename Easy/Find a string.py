def count_substring(string, sub_string):
    substrings = {}
    for i in range(0, len(string) - len(sub_string) + 1):
        sub = string[i: len(sub_string) + i]
        if sub not in substrings:
          substrings[sub] = 1
        else:
           substrings[sub] = substrings[sub] + 1 
    if sub_string not in substrings:
        return 0
    else:
        return substrings[sub_string]
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)