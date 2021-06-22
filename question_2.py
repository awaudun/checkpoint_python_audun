

def to_camel_case(text):
    return text.title().replace(" ", "")

print(to_camel_case("hello world")) # -> ‘HelloWorld’
print(to_camel_case("My stRriNg")) # -> ‘MyString’
print(to_camel_case("tHis Is A tesT string")) # -> ‘ThisIsATestString’