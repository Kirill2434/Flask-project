
from openpyxl import workbook, load_workbook
from flask import Blueprint, request

excel_validation_bp = Blueprint('validation', __name__, url_prefix='/validation')

@excel_validation_bp.route("/get_file", methods=["POST"])

def upload_file():
    file = request.files['file']
    wb = load_workbook(file)
    sheet = wb.get_sheet_by_name('График ЗП')
    for file in sheet['A1':'D2']:
        for cell in file:
            print(cell.value)
    #wb = load_workbook('./prototype.xlsx')
    #print(wb.get_sheet_names())
    return {"ok": True}



