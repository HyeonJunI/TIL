import math

# 분자와 분모를 입력받음
numerator1, denominator1 = map(int, input().split())
numerator2, denominator2 = map(int, input().split())

# 두 분수의 분모의 최소공배수를 계산
lcm = (denominator1 * denominator2) // math.gcd(denominator1, denominator2)

# 두 분수의 분자를 최소공배수를 기준으로 비례하게 만듦
numerator1 *= lcm // denominator1
numerator2 *= lcm // denominator2

# 두 분수의 분자를 더함
numerator_sum = numerator1 + numerator2

# 최종 결과 분자와 분모를 기약분수로 만듦
gcd = math.gcd(numerator_sum, lcm)
numerator_sum //= gcd
lcm //= gcd

# 결과 출력
print(numerator_sum, lcm)
