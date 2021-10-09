from flask import Blueprint, request

excel_validation_bp = Blueprint('validation', __name__, url_prefix='/validation')

@excel_validation_bp.route("/get_file", methods=["POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
    return {"ok": True}
