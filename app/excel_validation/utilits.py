
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


def upd_to_float_dict_2(dictionary1):
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


# Сравниваем  словари
def comp_dicts(base_dict, check_dict):
    for key, val in base_dict.items():
        if val == check_dict[key]:
            print('Ok', val, check_dict[key])
        else:
            print('Не совпало элементов:', val, check_dict[key])
    return base_dict == check_dict