import secondary

def hello():
    print("Hello")

def main():
    hello()
    x = secondary.foo(1)
    print(x)

if __name__== "__main__":
    main()
