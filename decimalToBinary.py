def DtoB(num):
    ans=0
    pw=1
    while num:
        remainder = num % 2
        if remainder==0: pw*10
        ans = remainder * pw + ans
        num = num//2
        pw=pw*10
    return ans

print(DtoB(8))