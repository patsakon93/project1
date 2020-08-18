str1 = "English = 78 Science = 83 math = 68 History = 65"
num = 0 
sun = 0
sd = str1.split()
for i in sd:
    if i.isnumeric():
        num = num + int(i)
        sun = sun +1
print('bum is',num)
print(num/sun)

      