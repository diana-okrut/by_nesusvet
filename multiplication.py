def main(numbers):
    answer = []
    multiplication = 1
    for i in numbers:
        multiplication *= i
    if multiplication != 0:
        for i in numbers:
            answer.append(int(multiplication / i))
    elif numbers.count(0) > 1:
        answer = [0] * len(numbers)
    else:


    return answer
