# Исключить из списка А1..AN максимальный элемент.

a = ['A','1','.','.','A','N']
ind = a.index(max(a))
max_el = a[ind]
spi_1 = a[0:ind]+a[ind+1:]
if max_el not in spi_1:
    print(spi_1)
else:
    for i in spi_1:
        if i==max_el:
            spi_1.remove(i)
    print(spi_1)