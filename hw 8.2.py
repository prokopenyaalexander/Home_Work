x = (lambda **kwargs: {k*2: v for k, v in kwargs.items()})(abc=5, de=1)
print(x)
