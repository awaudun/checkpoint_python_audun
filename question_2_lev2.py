

def to_camel_case(text):
    return text.title().replace(" ", "")

print(to_camel_case("hello world")) # -> ‘HelloWorld’
print(to_camel_case("My stRriNg")) # -> ‘MyString’
print(to_camel_case("tHis Is A tesT string")) # -> ‘ThisIsATestString’

def to_snake_case(camel_text):
    if camel_text.find(" "):
        print("wrong format dude! Try again")
    snake = ""
    first_letter = True
    for char in camel_text:
        if first_letter:
            snake += char.lower()
            first_letter = False
        elif char.isupper():
            snake += "_"
            snake += char.lower()
        else:
            snake += char
    return snake

print(to_snake_case("MyNameIsAudunYeah"))