#!/usr/bin/env python
# coding=utf-8

from views import app       #从views这个模块import出 app这个应用

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
