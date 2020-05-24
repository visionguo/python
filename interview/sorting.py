#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/03/02 10:43
# @Author  : Abel

void BubbleSore(int *array,int n)
{
    int i = 0;
    int j = 0;
    int temp = 0;

    for(i = 0; i < n; ++i){
        for(j = 1; j < n - i; ++j){
            if(array[j - 1] > array[j]){
                temp = array[j - 1];
                array[j - 1] = array[j];
                array[j] = temp;
            }
        }
    }
}