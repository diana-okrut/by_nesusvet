def main(numbers):
    answer = []
    multiplication = 1
    for i in numbers:
        if i != 0:
            multiplication *= i
    if numbers.count(0) > 1:
        answer = [0] * len(numbers)
    elif numbers.count(0) == 1:
        mem = numbers.index(0)
        answer = [0] * len(numbers)
        answer[mem] = multiplication
    else:
        for i in numbers:
            answer.append(int(multiplication / i))

    return answer
