from openpyxl import load_workbook
from flask import Blueprint, Flask, request
from main import excel_validation_bp, BasicTypeGraphic, CheckedTypeGraphic, db


@excel_validation_bp.route("/get_file", methods=["POST"])
def making_dict():
    file = request.files['file']
    wb = load_workbook(file)
    sheet = wb.get_sheet_by_name('График ЗП')
    mounth = sheet.cell(row=4, column=2).value

    data = sheet.iter_rows(min_row=4, max_row=4, min_col=5, max_col=35, values_only=True)
    hours = sheet.iter_rows(min_row=5, max_row=5, min_col=5,  max_col=35, values_only=True)
    dictionary = dict(zip(*data, *hours))
    Float_dictinary = str(dictionary)
    main_base = BasicTypeGraphic(main_date=data, hours=hours)
    db.session.add(main_base)
    db.session.commit()
    print(mounth)
    print(Float_dictinary)
    return {"ok": True}

@excel_validation_bp.route("/get_file_check", methods=["POST"])


def get_hours_list():
    file = request.files['file2']
    wb = load_workbook(file)
    sheet = wb.active
    hours_list = []
    for row in range(22, 632, 4):
        hours_dict = {}
        date_1 = sheet.iter_rows(min_row=14, max_row=14, min_col=4, max_col=18, values_only=True)
        date_2 = sheet.iter_rows(min_row=18, max_row=18, min_col=4, max_col=19, values_only=True)
        hours_1 = sheet.iter_rows(min_row=row, max_row=row, min_col=4, max_col=18, values_only=True)
        hours_2 = sheet.iter_rows(min_row=row + 2, max_row=row + 2, min_col=4, max_col=19, values_only=True)
        dictionary = dict(zip(*date_1, *hours_1))
        dictionary_2 = dict(zip(*date_2, *hours_2))
        hours_dict['dictionary'] = dictionary
        hours_dict['dictionary_2'] = dictionary_2
        hours_list.append(hours_dict)
    return hours_list
    hours_list = get_hours_list()
    for hours_dict in hours_list:
        upd_dict_1 = upd_to_float_dict(hours_dict['dictionary'])
        upd_dict_2 = upd_to_float_dict(hours_dict['dictionary_2'])
        result_dict = {}
        result_dict.update(upd_dict_1)
        result_dict.update(upd_dict_2)
        surname_d = {}
        for row_s in range(21, 629, 4):
            surname = sheet.cell(row=row_s + 4, column=2).value
            surname_d[surname] = result_dict
    print(surname_d)
    check_base = CheckedTypeGraphic(main_date=data, hours=hours)
    db.session.add(check_base)
    db.session.commit()
def upd_to_float_dict(dictionary):

    upd_dict = {}
    for key, value in dictionary.items():
        new_value = None

        if value == 'X':
            continue

        if value == "'" or value == "":
            new_value = 0

        if new_value != 0:
            new_value = ''
            for i in value:
                if i == ',':
                    i = '.'
                new_value = new_value + i
        upd_dict[key] = float(new_value)
    return upd_dict

    return {"ok": True}





