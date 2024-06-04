def fizzbuzz(n):
    if n % 3 == 0:
      print('Fizz')
    elif(n % 5 == 0) :
      print("Buzz") 
     elif n % 3 == 0 and n % 5 ==0:   
      print('fizzbuzz')
    else:
      print(n)
def main():
  for i in range(1,101):
    print(fizzbuzz(i))
