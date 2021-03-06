# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


import zipfile
import os
from sortedcontainers import SortedDict
# import locale
#
# locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')


class Word_Docs_Statistic():

    def __init__(self, file):
        self.file = file
        self.highstatistic = {}
        self.lowstatistic = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file, 'r') # создали объект zipfile.ZipFile
        for file in zfile.namelist(): # для каждого файла в zfile производим распаковку
            zfile.extract(file)
        self.file = file

    def read(self):
        if self.file.endswith('.zip'):
            self.unzip()
        with open(self.file, mode='r') as file:
            for line in file:
                self.count(line)

    def count(self, line):
        for i in line:
            if i.isalpha():
                if i.istitle():
                    if i in self.highstatistic:
                        self.highstatistic[i] += 1
                    else:
                        self.highstatistic[i] = 1
                else:
                    if i in self.lowstatistic:
                        self.lowstatistic[i] += 1
                    else:
                        self.lowstatistic[i] = 1


    def results(self):
        hitems = self.highstatistic.items()
        litems = self.lowstatistic.items()
        return hitems, litems



    def show_res(self):
        dash = '-'
        print(f'+{dash*9}+{dash*9}+')
        print('|{0:^9}|{1:^9}|'.format('буква', 'частота'))
        print(f'+{dash*9}+{dash*9}+')
        sum = 0
        for word, value in self.statistic.items():
            print(f'|{word:^9}|{value:^9}|')
            sum += value
        print(f'+{dash*9}+{dash*9}+')
        print('|{0:^9}|{1:^9}|'.format('ИТОГО', sum))
        print(f'+{dash*9}+{dash*9}+')


    def bug_correct(self, lst):
        lletters = ['ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
                    'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        hletters = ['Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
                    'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
        if lst[-1][0] == 'ё':
            for i in lletters:
                for j in range(len(lst)):
                    if i in lst[j]:
                        lst.insert(j, lst[-1])
                        lst.pop()
                        return
        elif lst[-1][0] == 'Ё':
            for i in hletters:
                for j in range(len(lst)):
                    if i in lst[j]:
                        lst.insert(j, lst[-1])
                        lst.pop()
                        return

class Word_Upper_Statistic(Word_Docs_Statistic):

    def results(self):
        hitems, litems = super().results()
        self.highstatistic = sorted(hitems)
        self.lowstatistic = sorted(litems)
        self.bug_correct(self.lowstatistic)
        self.bug_correct(self.highstatistic)
        self.statistic = self.highstatistic + self.lowstatistic
        self.statistic = dict(self.statistic)

class Word_Lower_Statistic(Word_Docs_Statistic):

    def results(self):
        hitems, litems = super().results()
        self.highstatistic = sorted(hitems)
        self.lowstatistic = sorted(litems)
        self.bug_correct(self.lowstatistic)
        self.bug_correct(self.highstatistic)
        self.statistic = self.highstatistic + self.lowstatistic
        self.statistic = list(reversed(self.statistic))
        self.statistic = dict(self.statistic)

class Word_Frequence_Statistic(Word_Docs_Statistic):

    def results(self):
        self.highstatistic.update(self.lowstatistic)
        sorted_values = sorted(self.highstatistic.values())
        self.statistic = {}
        for i in sorted_values:
            for k in self.highstatistic.keys():
                if self.highstatistic[k] == i:
                    self.statistic[k] = self.highstatistic[k]




for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for name in filenames:
        if name == 'voyna-i-mir.txt.zip':
            current_path = os.path.join(dirpath, name)

alpha_plus = Word_Frequence_Statistic(current_path)
alpha_plus.read()
alpha_plus.results()
alpha_plus.show_res()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
