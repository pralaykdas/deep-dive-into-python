def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f"$ {result}")
    return wrapper

@currency
def compute(amount, tax):
    return amount + tax

compute(100, 20)
