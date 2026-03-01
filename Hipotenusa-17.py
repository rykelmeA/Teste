while True:
    try:
        co = float(input('Cateto oposto:'))
        ca = float(input('Cateto adjacente:'))
        h = (co**2+ca**2)**0.5
        print(f'A hipotenusa e de {h:.2f}cm')
    except ValueError:
        print('digite números')
        