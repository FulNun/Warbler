from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, Optional


class UserAddForm(FlaskForm):
    """Form for adding users."""
    username = StringField("Username", validators=[InputRequired(), Length(max=20)])
    password = PasswordField("Password", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=50)])
    image_url = StringField("(Optional) Image URL", validators=[Optional()])


class LoginForm(FlaskForm):
    """Login form."""
    username = StringField("Username", validators=[InputRequired(), Length(max=20)])
    password = PasswordField("Password", validators=[InputRequired()])


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""
    text = StringField("Text", validators=[InputRequired(), Length(max=140)])


class UserProfileForm(FlaskForm):
    """Form for editing user profile."""
    username = StringField("Username", validators=[InputRequired(), Length(max=20)])
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=50)])
    image_url = StringField("Image URL", validators=[InputRequired(), Length(max=200)])
    header_image_url = StringField("Header Image URL", validators=[InputRequired(), Length(max=200)])
    bio = StringField("Bio", validators=[Length(max=140)])
    location = StringField("Location", validators=[Length(max=30)])
    password = PasswordField("Password", validators=[InputRequired()])
