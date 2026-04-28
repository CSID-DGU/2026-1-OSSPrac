def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        divisor += 1
    return factors

number = int(input("소인수분해할 수를 입력하세요: "))
print(f"{number}의 소인수분해 결과:", prime_factors(number))
