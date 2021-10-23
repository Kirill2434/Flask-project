from datetime import datetime, timedelta
from openpyxl import load_workbook
from flask import Blueprint, request

excel_validation_bp = Blueprint('validation', __name__, url_prefix='/validation')




@excel_validation_bp.route("/get_file", methods=["POST"])

def making_dict():
    file = request.files['file']
    wb = load_workbook(file)
    sheet = wb.get_sheet_by_name('График ЗП')
    month = sheet.cell(row=4, column=2).value

    data = sheet.iter_rows(min_row=4, max_row=4, min_col=5, max_col=35, values_only=True)
    hours = sheet.iter_rows(min_row=5, max_row=5, min_col=5,  max_col=35, values_only=True)
    dictionary = dict(zip(*data, *hours))
    Float_dictinary = str(dictionary)
    print(month)
    print(Float_dictinary)
    return {"ok": True}

@excel_validation_bp.route("/get_file_check", methods=["POST"])
def load_def_fail():
    file = request.files['file2']
    wb = load_workbook(file)
    sheet = wb.active
    month = sheet.cell(row=10, column=33).value
    surname = sheet.cell(row=21, column=2).value

    data_1 = sheet.iter_rows(min_row=14, max_row=14, min_col=4, max_col=18, values_only=True)
    data_2 = sheet.iter_rows(min_row=18, max_row=18, min_col=4, max_col=19, values_only=True)
    hours_1 = sheet.iter_rows(min_row=22, max_row=22, min_col=4, max_col=18, values_only=True)
    hours_2 = sheet.iter_rows(min_row=24, max_row=24, min_col=4, max_col=19, values_only=True)
    dictionary = dict(zip(*data_1, *hours_1))
    dictionary_2 = dict(zip(*data_2, *hours_2))
    dictionary.update(dictionary_2)


    print(month)
    print(surname)
    print(dictionary)
    return {"ok": True}





