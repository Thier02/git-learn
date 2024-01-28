

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def main():
    print(add(10, 2))
    print(sub(10, 2))
    print(multiply(10, 2))

if __name__ == '__main__':
    main()

