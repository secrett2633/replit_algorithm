def checkPrimeNum(check_number):
    #에라토스테네스의 체로 소수인지 확인
    for i in range(2, int(check_number**0.5)+1): 
        if int(check_number) % i == 0: 
            return False
    return True


print(checkPrimeNum(5))