def solution(numer1, denom1, numer2, denom2):
    from fractions import Fraction
    a = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    answer = [a.numerator, a.denominator]
    return answer