st = input('Enter a string : ')
print('This is what I found about that string :')
if st.isalnum() :
    print('The string is alphanumeric.')
if st.isalpha() :
    print('The string contains only alphabetic characters.')
if st.islower() :
    print('The letters in the string are all lowercase.')
if st.isnumeric() :
    print('The string contains only digits.')
if st.isupper() :
    print('The letters in the string are all uppercase.')
    