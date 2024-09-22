import time
from threading import Thread
from datetime import datetime
from time import sleep
from pprint import pprint

def write_words(word_count,file_name):
    with open(file_name,'w',encoding = 'utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
print(f'Работа потоков длилась {time_end - time_start}')
time_start = datetime.now()
thr_first = Thread(target=write_words,args=(10, 'example5.txt'))
thr_second = Thread(target=write_words,args=(30, 'example6.txt'))
thr_third = Thread(target=write_words,args=(200, 'example7.txt'))
thr_four = Thread(target=write_words,args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()
time_end = datetime.now()

print((f'Работа потоков длилась {time_end - time_start}'))
