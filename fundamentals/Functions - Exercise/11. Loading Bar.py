received_number = input()

def check():
    if received_number == '100':
        return f'100% Complete!\n[%%%%%%%%%%]'
    for_first_symbol = int(received_number) // 10
    for_second_symbol = 10 - for_first_symbol
    return f"{received_number}% [{'%' * for_first_symbol}{'.' * for_second_symbol}]\nStill loading..."

print(check())
