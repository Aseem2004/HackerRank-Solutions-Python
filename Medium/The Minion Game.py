def minion_game(string):
    # your code goes here
    vowels = ["A", "E", "I", "O", "U"]
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    consonants_list = [1 if char in consonants else 0 for char in string]
    vowel_list = [1 if char in vowels else 0 for char in string]
    char_value = list(range(len(string), 0, -1))

    stuart = sum([a * b for a, b in zip(consonants_list , char_value)])
    kevin =  sum([a * b for a, b in zip(vowel_list , char_value)])

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)