#!/usr/bin/env python
# coding=utf-8

from flask import Flask
app = Flask(__name__)

from LibraryManage import logic


@app.route('/')
def home_page():
    home_data = logic.get_home()
    return home_data

@app.route('/books')
def books():
    books_data = logic.get_books()
    return  books_data

@app.route('/book/<string:book_id>')
def book(book_id):
    book_data = logic.get_book(book_id)
    return book_data

@app.route('/students')
def students():
    students_data = logic.get_students()
    return students_data

@app.route('/student/<string:student_id>')
def student(student_id):
    student_data = logic.get_student(student_id)
    return student_data
