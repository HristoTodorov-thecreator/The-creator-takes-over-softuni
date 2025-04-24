import re
count_barcodes = int(input())


for m in range(count_barcodes):

    barcode_check = input()

    pattern = r'(@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+)'

    x = re.findall(pattern,barcode_check)

    if x:
        bar = ''.join(x)
        product_group = ''.join([x for x in bar if x.isdigit()])
        if not product_group:
            product_group = '00'
        print(f'Product group: {product_group}')




    if not x:
        print(f'Invalid barcode')