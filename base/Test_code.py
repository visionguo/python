#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# def get_formatted_name(first,final):
#     full_name = first +' ' +final
#     return full_name.title()

# print("Enter 'q' to quit.")
# while True:
#     first = raw_input("\nEnter the first_name:")
#     if first == 'q':
#         break
#     final = raw_input("\nEnter the final_name:")
#     if final == 'q':
#         break
#     formatted_name = get_formatted_name(first,final)
#     print("\tNeatly formatted name: " +formatted_name + '!')

#单元测试和测试用例
#单元测试用于核实函数的某个方面没有问题
#测试用例是一组单元测试

#可通过的测试
# import unittest     #导入模块unittest
# #from name_function import get_formatted_name   #导入测试的函数get_formatted_name
#
# class NamesTestCase(unittest.TestCase):     #创建NamesTestCase的类，包含一系列针对get_formatted_name()的单元测试
#     def test_first_final_name(self):
#         formatted_name = get_formatted_name('vision','guo')     #调用函数并将值存储
#         self.assertEqual(formatted_name,'Vision Guo')           #断言方法用来核实得到的结果是否与期望的结果一致
#
# unittest.main()

# .                     #有一个测试通过了
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s  #指出python运行了一个测试，和消耗时间
#
# OK                    #该测试用例中的所有单元测试都通过了

#不能通过的测试
# def get_formatted_name(first,middle,final):
#     full_name = first +' ' +middle +' ' +final
#     return full_name.title()
#
# import unittest
#
# class NamesTestCase(unittest.TestCase):
#     def test_first_final_name(self):
#         formatted_name = get_formatted_name('vision','guo')
#         self.assertEqual(formatted_name,'Vision Guo')
#
# unittest.main()

#测试未通过时怎么办
# def get_formatted_name(first,final,middle=''):
#     if middle:
#         full_name = first + ' ' + midlle + ' ' + final
#     else:
#         full_name = first + ' ' + final
#     return full_name.title()
#
# import unittest
#
# class NamesTestCase(unittest.TestCase):
#     def test_first_final_name(self):
#         formatted_name = get_formatted_name('vision','guo')
#         self.assertEqual(formatted_name,'Vision Guo')
#
# unittest.main()

#添加新测试
# def get_formatted_name(first,final,middle=''):
#     if middle:
#         full_name = first + ' ' + middle + ' ' + final
#     else:
#         full_name = first + ' ' + final
#     return full_name.title()
# import unittest
# #from name_function import get_formatted_name
#
# class NameTestCase(unittest.TestCase):
#     def test_first_final_name(self):
#         formatted_name = get_formatted_name('allen','su')
#         self.assertEqual(formatted_name,'Allen Su')
#     def test_first_middle_final_name(self):
#         formatted_name =get_formatted_name('lin','jun','jie')
#         self.assertEqual(formatted_name,'Lin Jie Jun')
# unittest.main()

#测试类
# class AnonymousSurvey():            #收集匿名调查问卷的答案
#     def __init__(self,question):    #存储一个问题，并为存储答案做准备
#         self.question = question
#         self.responses = []         #空列表，用于存储答案
#     def show_question(self):        #显示调查问卷
#         print(question)
#
#     def store_response(self,new_response):  #存储单份调查答卷
#         self.responses.append(new_response)
#
#     def show_results(self):         #显示收集到的所有答卷
#         print("Survey results:")
#         for response in responses:
#             print('-' + response)
#
# from survey import AnonymousSurvey
# responses = []
# question = "what language did you first learn to spark?"    #定义一个问题，并创建一个表示调查的AnonymousSurvey对象
# my_survey = AnonymousSurvey(question)
#
# my_survey.show_question()
# print("Enter 'q' to quit")
# while True:
#     response =raw_input("Language:")
#     if response == 'q':
#         break
#     my_survey.store_response(response)
#
# print("\nThank you to everyone who participated in this survey!")
# my_survey.show_results()

#测试AnonymousSurvey类
# import unittest                         #导入unittest模块
# #from survey import AnonymousSurvey     #导入要测试的类AnonymousSurvey
# class AnonymousSurvey():            #收集匿名调查问卷的答案
#     def __init__(self,question):    #存储一个问题，并为存储答案做准备
#         self.question = question
#         self.responses = []         #空列表，用于存储答案
#     def show_question(self):        #显示调查问卷
#         print(question)
#
#     def store_response(self,new_response):  #存储单份调查答卷
#         self.responses.append(new_response)
#
#     def show_results(self):         #显示收集到的所有答卷
#         print("Survey results:")
#         for response in responses:
#             print('-' + response)
#
# class TestAnonmyousSurvey(unittest.TestCase):   #将要测试用例命名为TestAnonmyousSurvey，也继承了unittest.TestCase
#     """针对AnonmyousSurvey类的测试"""
#     def test_store_single_response(self):
#         """测试单个答案会被妥善地存储"""
#         question ="What language did you first learn to speak?"
#         my_survey=AnonymousSurvey(question)
#         my_survey.store_response('chinese')     #创建实例my_survey使用方法store_response()存储单个答案chinese
#         self.assertIn('chinese',my_survey.responses)
#     def test_store_three_responses(self):
#         """测试三个答案会被妥善地存储"""
#         question="What language do you like?"
#         my_survey =AnonymousSurvey(question)
#         responses=['python','go','shell']
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response,my_survey.responses)
#
# unittest.main()

#方法setUp()
import unittest                         #导入unittest模块
#from survey import AnonymousSurvey     #导入要测试的类AnonymousSurvey
class AnonymousSurvey():            #收集匿名调查问卷的答案
    def __init__(self,question):    #存储一个问题，并为存储答案做准备
        self.question = question
        self.responses = []         #空列表，用于存储答案
    def show_question(self):        #显示调查问卷
        print(question)

    def store_response(self,new_response):  #存储单份调查答卷
        self.responses.append(new_response)

    def show_results(self):         #显示收集到的所有答卷
        print("Survey results:")
        for response in responses:
            print('-' + response)

responses = []
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question ="What language do you like?"
        self.my_survey=AnonymousSurvey(question)            #创建一个调查对象
        self.responses= ['English','Spanish','Mandarin']    #创建一个答案列表
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):       #测试三个答案会被妥善地存储
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()
#运行测试用例时，每完成一个单元测试，Python都打印一个字符:测试通过时打印一个句点;测试引发错误时打印一个E ;测试导致断言失败时打印一个F 。