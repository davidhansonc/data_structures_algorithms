def fibonacci():
    cache = dict()

    def calc(index):
        if index in cache:
            return cache[index]
        if index < 2:
            cache[index] = index
            return cache[index]
        cache[index] = calc(index - 1) + calc(index - 2)
        return cache[index]
    
    return calc

fib_calc = fibonacci()
f = fib_calc(50)
print(f)


def fib_bot_up(n):
    count = 0
    answers = [0, 1]
    for index in range(2, n + 1):
        answers.append(answers[index - 2] + answers[index - 1])
        count += 1
    return answers[-1]

print(fib_bot_up(50))