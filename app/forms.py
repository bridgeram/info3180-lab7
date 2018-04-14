from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('description', validators=[InputRequired()])
    photo = FileField('Image', validators=[FileRequired('Please upload your file here'), FileAllowed(['jpg', 'png'], 'Images only!')])