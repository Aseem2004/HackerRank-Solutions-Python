if __name__ == '__main__':
    n = int(input())
    student_marks = {}  
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum_scores = 0 
    
    for s in student_marks[query_name]: 
        sum_scores = s + sum_scores
        
    result = sum_scores / 3 
    
    result =  "{:.2f}".format(result)
    print(result)
