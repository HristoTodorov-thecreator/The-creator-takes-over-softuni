numbers = input().split(', ')

make_int = [int(number) for number in numbers]

start = 10



while make_int:

    comprehension_for_int = [second for second in make_int if second <= start]

    make_int = [third for third in make_int if third > start]






    print(f"Group of {start}'s: {comprehension_for_int}")
    start += 10

