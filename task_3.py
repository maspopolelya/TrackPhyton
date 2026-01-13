def count_letters(text):# TODO  Напишите функцию count_letters
    symbol_count = {}
    for symbol in  text.lower():
        if symbol.isalpha():
            if symbol in symbol_count: symbol_count[symbol] += 1
            else: symbol_count[symbol] = 1

    return symbol_count

def calculate_frequency(text):# TODO Напишите функцию calculate_frequency
    sum_symb = 0
    for symbol in count_letters(text).values():
        sum_symb += symbol
    new_dict = count_letters(text)
    for key in new_dict:
        new_dict[key] /= sum_symb
        from decimal import Decimal
        new_dict[key] = Decimal(new_dict[key])
        new_dict[key] = new_dict[key].quantize(Decimal("0.01"))

    return new_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

print('\n'.join("{}: {}".format(k, v) for k, v in calculate_frequency(main_str).items()))
