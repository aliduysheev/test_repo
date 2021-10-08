# d
# dict_ = {k1:v1 for k1, v1 in dictict_= {'TImur':{'h':90, 'm':95, 'l': 91}, 'Vlad': {'m':93, 'v':95, 'l':98}}_.items() for k2,v2 in v1.item() if max(v1.values()) == v2}
# print(dict_)

# dict_ = {'first':{'a':1}, 'second': {'b:2'}}
# dict_ = {k1:v1 for k1, v1 in dict_.items() for k2,v2 in v1.items()}
# print(dict_)

# try:
#     age = int(input('введите возраст:'))
#     if not age in range(18, 65):
#         raise ValueError('Доступ запрещен далбаеб')
# except ValueError:
#     print('Your age must be between 18 and 65')
# else:
#     print('OK')
# finally:
#     print('Good Bye')

# import random
# a = (random.randrange(0, 10))
# while True:
#     num = input('Guess the number beach:')
#     print(f'random nuber is {a}')

#     if num.lower() == 'exist':
#         print('Game over suchka')
#     elif int(a) > int(num):
#         print('NUMBER HOLd OOON')
#     elif int(a) < int(num):
#         print('NUMBER IS LOWER SHEHEHEHEHEHE')
#     elif int(a) == int(num):
#         print('ПОЗДРАВЛЯЮ ДАЛБЕЕБЕБ/nType exit to quit')

# def add_nums(a,b):
#     return a + b
# result = add_nums(10, 5)
# print(result)

# result = lambda a, b: a + b
# # print(result(10, 5))
# print(type(add_nums()))

# lst = [1, 2, 4, 6, 9]
# lst_new = [str(i) for i in lst]
# for i in lst:
#     lst_new.append(str(i))
# print(lst_new)
# map(function, iterible_obj)
# def num_to_str(i):
#     return str(i)
# lst_new = list(map(lambda i: str(i), lst))
# lst_new = list(map(num_to_str, lst))
# print(lst_new)

# filter()
# filter(func, iterible_obj)
# lst = [i for i in range(1, 11)]
# lst = list(range(1, 11))
# new_lst = list(filter(lambda i: x % 3 != 0, lst))
# print(new_lst)

# # reduce()
# from functools import reduce
# lst = [20, 57, 33]
# result = reduce(lambda x, y: x / y, lst)
# print(result)

# print(pow(1, 2))

# # zip()
# employee_numbers = [2, 4, 56, 14]
# employee_numes = ['JANArrr', 'ISken', 'MAra', 'SANJIKK']
# employee_sphere = ['It', 'Finanscompany', 'Cocci', 'ASDDF']
# zipped_values = zip(employee_numbers, employee_numes, employee_sphere)
# # print(zipped_values)
# zipped_list = list(zipped_values)
# print(zipped_list)from



# list_of_readers = {'Alex': {'Financial': 'Theodor Draiser'}}
# list_of_books = {'Financial': 'Theodor Draiser', 'Rich dad, poor dad,': 'robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}
# db = {'John': 23, 'Jack': 52, 'Alex': 23, 'Tom': 34}
# def registration():
#     global list_of_books
#     book = input(f'Какую книгу вы хотите хотите получить? Выберите из {list_of_books}')
#     if book in list_of_books:
#         print()
# registration()

# dew write_csv(data):
#     with open('mobiles.csv', 'a') as csv_file:
#         writer = csv.writer(csv_file, delimter= '/')
#         writer.writerow()

# def main():
#     # html
#     # 

# https://cars.kg/offers
# import requests
# from bs4 import BeautifulSoup as BS


# from typing import ClassVar
# import schedule    
# import time

# def job():
#     print("I'm working...")

# schedule.every(3).seconds.do(job)
# # schedule.every().thursday.at('19:10').do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
# import requests
# from bs4 import BeautifulSoup as BS
# import schedule
# import csv

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BS(html, 'lxml')
#     catalog = soup.find('div', class_='product-index product-index oh')
#     phones = catalog.find_all('div', class_='item product_listbox oh')
#     for car in cars:
#         try:
#             title = 'div', class=<h1 class="page-title" itemprop="Name">Мобильные телефоны в Бишкеке, Кыргызстане</h1></div>'
            
#         except:
#             title = ''
#         try:
#             img = 'div', class="listbox_img pull-left">
#     <a href="/product/view/sotovyy-telefon-bravis-a552-joy-max-zolotoy" target="_blank"><img src="/images/product/40705/40705.jpg" alt="Сотовый телефон BRAVIS A552 Joy Max золотой"></a></div>'
#         except:
#             price= 'div', class="listbox_price text-center">
#                                             <strong>7730 сом</strong>
#                         </div>'
#         print(title, img)
   
# def main():
#     # url = 'https://cars.kg/offers'
#     # html = get_html(url)
#     # data = get_data(html)

#     for page in range(1, 28):
#         url = f'https://www.kivano.kg/mobilnye-telefony/{page}'
#         html = get_html(url)
#         data = get_data(html)


