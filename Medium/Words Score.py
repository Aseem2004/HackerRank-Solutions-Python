def is_vowel(letter):
    return letter in ['a','e','i','o','u','y']

def score(words):
    s=0
    words=list(words)
    for word in words:
        vowels=0
        for letter in word:
            if is_vowel(letter):
                vowels+=1
        if vowels%2==0:
            s+=2
        elif vowels%2!=0:
            s+=1
    return s

n=int(input())
words=input().split()
print(score(words))
