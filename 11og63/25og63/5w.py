def main():
  x = int(input('Enter :'))
  y = int(input('Enter :'))
  print('The sum of',x,' and ',y,' is')
  show_sum(x,y)
def show_sum(num1, num2):
  result = num1 + num2
  print(result)
main()