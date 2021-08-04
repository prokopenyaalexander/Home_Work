def zero_exception(a, b):
    try:
        result = a / b
    except ZeroDivisionError as err:
        print(f'divisor is zero - {err}!!!')
    except Exception as err:
        print(f'SOMETHING WRONG - {err}!!!')
