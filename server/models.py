from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if not name or name.strip() == "":
            raise ValueError("Author must have a name.")
        return name

    @validates('phone_number')
    def validate_phone_number(self, key, number):
        if not number or len(number) != 10 or not number.isdigit():
            raise ValueError("Phone number must be exactly 10 digits.")
        return number

    
class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, title):
        clickbait_phrases = ["Won't Believe", "Secret", "Top", "Guess"]
        if not title or title.strip() == "":
            raise ValueError("Post must have a title.")
        if not any(phrase in title for phrase in clickbait_phrases):
            raise ValueError("Title must be clickbait-y (contain 'Won't Believe', 'Secret', 'Top', or 'Guess').")
        return title

    @validates('content')
    def validate_content(self, key, content):
        if not content or len(content) < 250:
            raise ValueError("Post content must be at least 250 characters long.")
        return content

    @validates('summary')
    def validate_summary(self, key, summary):
        if summary and len(summary) > 250:
            raise ValueError("Summary must be 250 characters or less.")
        return summary

    @validates('category')
    def validate_category(self, key, category):
        if category not in ["Fiction", "Non-Fiction"]:
            raise ValueError("Category must be either Fiction or Non-Fiction.")
        return category


    
