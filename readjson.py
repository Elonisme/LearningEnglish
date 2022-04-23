# -*- coding =utf-8 -*-
# @Time : 2022-04-23 15:08
# @Author : Elon
# @File : readjson.py
# @Software : PyCharm

import pandas as pd

df = pd.read_json(r'.\data\adicted-data.json')

# print(type(df))
# print(df.keys())

dict = df['dict']
# print(type(dict))
# print(dict.keys())

# print("----------learning-------")
learning = dict['learning']
# print(type(learning))
# print(learning.keys())

word_list = []
form_list = []
mean_list = []
sentence_list = []

# print('{:^20}{:^20}{:^20}{:^20}'.format("单词","词性","示意","引句"))
for word in learning:
    mean = dict['learning'][word]['target']

    if 'form' in dict['learning'][word]:
        form = dict['learning'][word]['form']
    else:
        form = " "

    if 'sentence' in  dict['learning'][word]:
        sentence = dict['learning'][word]['sentence']
        sentence = sentence.replace('<b>','<')
        sentence = sentence.replace('</b>','>')
    else:
        sentence = " "
    word_list.append(word)
    form_list.append(form)
    mean_list.append(mean)
    sentence_list.append(sentence)

    # print('{:^20}{:^20}{:^20}{:^20}'.format(word, form, mean, sentence))

dataframe = pd.DataFrame({'单词' :word_list,'词性' :form_list,'示意' :mean_list , '引句' :sentence_list})
dataframe.to_csv(".//data//learningword(gbk).csv",index=True,sep=',',encoding="gbk")
dataframe.to_csv(".//data//learningword(utf_8).csv",index=True,sep=',',encoding="utf_8")

# print("----------mastered-------")
# mastered = dict['mastered']
# # print(type(mastered))
# # print(mastered.keys())
#
# print('{:^20}{:^20}{:^20}{:^20}'.format("单词","词性","示意","引句"))
# for word in mastered:
#     mean = dict['mastered'][word]['target']
#     if 'form' in dict['mastered'][word]:
#         form = dict['mastered'][word]['form']
#
#     if 'sentence' in  dict['mastered'][word]:
#         sentence = dict['mastered'][word]['sentence']
#         sentence = sentence.replace('<b>','<')
#         sentence = sentence.replace('</b>','>')
#     else:
#         sentence = " "
#
#     print('{:^20}{:^20}{:^20}{:^20}'.format(word, form, mean, sentence))