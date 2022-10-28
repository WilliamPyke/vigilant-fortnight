from counters.count import add, sub, mul
import secondary

def hello():
    name = input("What is your name: ")
    print("Hello", name)

def main():
    hello()
    x = secondary.foo(1)
    print(x)
    print(add(3, 4))
    print(sub(3, 4))
    print(multiply(3, 4))

if __name__== "__main__":
    main()
