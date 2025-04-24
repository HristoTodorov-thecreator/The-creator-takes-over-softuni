

def math_operations(*args,**kwargs):
    keys = list(kwargs.keys())

    for i in range(len(args)):
        key = keys[i % 4]

        if key == 'a':
            kwargs[key] += args[i]

        if key == 's':
            kwargs[key] -= args[i]

        if key == 'd':
            if args[i] != 0:
                kwargs[key] /= args[i]


        if key == 'm':
            kwargs[key] *= args[i]

    kwargs = sorted(kwargs.items(),key=lambda x: (-x[1],x[0]))


    return '\n'.join(f'{k}: {v:.1f}'for k,v in kwargs)





print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))