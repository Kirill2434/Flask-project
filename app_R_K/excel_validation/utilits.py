def upd_to_float_dict_1(dict_d):
    upd_dict_1 = {}
    for key, value in dict_d.items():
        new_value = None

        if value == "'" or value == "":
            new_value = 0

        if new_value != 0:
            new_value = ''
            for i in str(value):
                if i == ',':
                    i = '.'
                new_value = new_value + i
        upd_dict_1[str(key)] = float(new_value)

    return upd_dict_1


def upd_to_float_dict_2(dictionary1) -> object:
    upd_dict = {}
    for key, value in dictionary1.items():
        new_value = None

        if value == 'X':
            continue

        if value == "'" or value == "":
            new_value = 0

        if new_value != 0:
            new_value = ''
            for i in str(value):
                if i == ',':
                    i = '.'
                new_value = new_value + i
        upd_dict[str(key)] = float(new_value)
    return upd_dict


def comparison_of_dictionaries(base_dict, checking_dict):

    mistakes_dict = {'Ошибки': []}
    for key, value in checking_dict.items():
        base_hours_value = base_dict.get(key)
        if value != base_hours_value:
            mistakes_dict['Ошибки'].append(value)

    print(f"Обнаружено: {int(len(mistakes_dict['Ошибки']))} несовпадений")

    return 'Проверка выполнена'
