def capitalize_words(input_string):
    # Use the title() method to capitalize the first letter of each word
    return input_string.title()

# Test the function
input_string = "hello world how are you"
result = capitalize_words(input_string)
print(result)  # Output: "Hello World How Are You"
