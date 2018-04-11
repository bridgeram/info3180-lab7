from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired, TextArea
from wtforms.validators import InputRequired

class UploadForm(FlaskForm):
    description = TextArea('desc', validators=[InputRequired()])
    photo = FileField('Image', validators=[FileRequired('Please upload your file here'), FileAllowed(['jpg', 'png'], 'Images only!')])