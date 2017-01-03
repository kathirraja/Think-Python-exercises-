def eval_loop():
    while True:
        exp = str(raw_input(''))
        if exp == 'done':
            break
        print eval(exp)
    return eval(exp)

print eval_loop()
