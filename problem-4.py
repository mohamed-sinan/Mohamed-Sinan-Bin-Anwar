n = [1,2,8,9,12,46,76,82,15,20,30]
def multiples(r):
    target = [1,2,3,4,5,6,7,8,9]
    answer = {}
    for i in target:
        answer[i]=0
        for j in range(len(r)):
            if r[j]%i == 0:
                answer[i]+=1

    return answer

input_answer= multiples(n)
print(input_answer)

