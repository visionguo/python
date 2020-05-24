#!/usr/bin/env python
#coding=utf-8

def get_home():
    """获取图书馆主页资料，一般是读取数据库或者缓存系统"""
    return 'data of home page'

def get_books():
    """获取图书馆所有书籍列表，一般是读取缓存系统"""
    return 'list of books basic info'

def get_book(book_id):
    """获取某一本书的详细信息，一般是读取数据库，如果书籍比较热门的话，一般可读取缓存系统"""
    return 'detailed info of book : {}'.format(book_id)

def get_students():
    """获取学生列表，一般是读取数据库"""
    return 'list of students basic info'

def get_student(student_id):
    """获取某一个学生的详细信息，一般是读取数据库"""
    return 'detailed info of student: {}'.format(student_id)