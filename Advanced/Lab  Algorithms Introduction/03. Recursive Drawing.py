
def drawing(n):
    if n <=0:
        return

    print(f'*' * n)

    drawing(n-1)

    print(f'#' * n)




n = int(input())
drawing(n)