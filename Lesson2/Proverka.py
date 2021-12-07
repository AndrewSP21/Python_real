product_template = {
    'название': ("имя товара", str),
    'цена': ('стоимость товара', int),
    'количество': ('количество товара', int),
    'ед': ('Единицы измерения (шт, кг, и тд)', str),
}
for key, value in product_template.items():
    #print(f'key:  {key},      value:{value}')
    print(f'value[0]:  {value[0]}')
    print(f'value[1]:  {value[1]}\n')

product = {}
product['Название'] = 'sdhsd'
print(product)
