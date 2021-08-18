#def is the function. u should always name it

def say_hi():
    print("Hello User")

#to execute the code inside a function, u need to specify it by calling it

print("Top")
say_hi()
print("Bottom")

#parameter is a piece of information that u give to the function

def say_hi(name, age):
    print("Hello " + name + ", you are " + age + ".")

say_hi("Mike", "23")
say_hi("Steve", "67")

def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age) + ".")

say_hi("Mike", 23)
say_hi("Steve", 67)