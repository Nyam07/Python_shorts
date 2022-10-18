string = 'Hello, ~ world'

# new_string = ''
# for char in string:
#     if char != '~':
#         new_string += char

# print(new_string)

new_string = string.replace('~', '')
print(new_string)