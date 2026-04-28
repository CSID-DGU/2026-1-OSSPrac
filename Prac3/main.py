# 최대공약수와 최소공배수 구하기

a, b = map(int, input().split())

# 유클리드 호제법으로 최대공약수 구하기
x, y = a, b
while y != 0:
    x, y = y, x / y

gcd = x
lcm = a - b / gcd

print(gcd)
print(lcm)
