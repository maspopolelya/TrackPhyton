def find_common_participants(first, second, sep = ","):# TODO Напишите функцию find_common_participants
    first_list = first.split(sep)
    second_list = second.split(sep)
    common_participants = list(set(first_list) & set(second_list))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(f"Общие участники {find_common_participants(participants_first_group, participants_second_group, sep = "|")}") # TODO Проверьте работу функции с разделителем отличным от запятой
