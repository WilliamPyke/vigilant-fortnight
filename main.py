from counters.count import add, sub, mul
import secondary

def hello():
    print("Hello")

def main():
    hello()
    x = secondary.foo(1)
    print(x)
    print(add(3, 4))
    print(sub(3, 4))
    print(mul(3, 4))

if __name__== "__main__":
    main()
