# def my_function(x):
#   return x[::-1]

# mytxt = my_function("edyoda university")

# print(mytxt)

def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

input_str = str(input("enter a word: "))

if __name__ == "__main__":
    print('Reverse String using for loop =', reverse_for_loop(input_str))
