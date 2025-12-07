vol_symb = 4
vol_line = 25 * vol_symb
vol_page = 50 * vol_line

vol_book = 100 * vol_page # TODO Найдите количество книг, которое можно разместить на дискете

memory_ = 1024 ** 2 * 1.44
quantity_ = int(memory_ / vol_book)

print("Количество книг, помещающихся на дискету:", quantity_)
