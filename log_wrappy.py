def loggly(func):
    def wrapper(*args, **kwargs):
        with open ("test_log.txt", "w") as logfile:
            logfile.write(f"calling {func.__name__} with {args} and {kwargs} arguments")
            result = func(*args, **kwargs)
            logfile.write(f"calling·{func.__name__} resulted: {result}\n")
            return result
    return wrapper

@loggly
def factorial(n):
    if n < 1: 
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    factorial(4)
