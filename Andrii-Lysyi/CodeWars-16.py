def solution(number):
    mul = []
      for x in range(number):
        if int(x)%3 == 0 or int(x)%5 ==0:
            mul.append(int(x))
      return(sum(mul))