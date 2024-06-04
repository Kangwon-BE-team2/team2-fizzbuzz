def fizzbuzz(n):
  for i in range(1, 101):
    if i % 3 == 0:
      print('Fizz')
    elif(i % 5 == 0) :
      print("Buzz") 
     elif i % 3 == 0 and i % 5 ==0:   
      print('fizzbuzz')
    else:
      print(i)
def main():
  for i in range(1,101):
    print(fizzbuzz(i))