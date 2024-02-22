
import random
import pandas as pd
from datetime import datetime, timedelta
from tkinter import *
from tkinter.ttk import Combobox

# Opening files, converting to arrays, preparing to generation

m_names = [str(i).replace("\n", "") for i in (open('names.txt', 'r', encoding='utf-8').readlines())]
m_surnames = [str(i).replace("\n", "") for i in open('surnames.txt', 'r', encoding='utf-8').readlines()]
m_patronymics = [str(i).replace("\n", "") for i in open('patronymics.txt', 'r', encoding='utf-8').readlines()]

w_names = [str(i).replace("\n", "") for i in open('names_w.txt', 'r', encoding='utf-8').readlines()]
w_surnames = [str(i).replace("\n", "") for i in open('surnames_w.txt', 'r', encoding='utf-8').readlines()]
w_patronymics = [str(i).replace("\n", "") for i in open('patronymics_w.txt', 'r', encoding='utf-8').readlines()]

doctors = [str(i).replace("\n", "") for i in open('doctors.txt', 'r', encoding='utf-8').readlines()]
analyzes = [str(i).replace("\n", "") for i in open('analyzes.txt', 'r', encoding='utf-8').readlines()]
symptoms = [str(i).replace("\n", "") for i in open('symptoms.txt', 'r', encoding='utf-8').readlines()]

years_pasp = []
for i in range(100):
    if i < 24 and i >= 10:
        years_pasp.append(str(i))
    if i < 10:
        years_pasp.append('0'+str(i))
    if i > 79:
        years_pasp.append(str(i))
        
used_pasp = []
used_snils = []

iso_format = "{Year}-{Month}-{Day}T{Hour}:{Minute}+{Offset}"

year_range = ["2020", "2021", "2022", "2023"]
month_range = ["01","02","03","04","05","06","07","08","09","10","11","12"]
day_range = [str(i).zfill(2) for i in range(1,29)]
hour_range = [str(i).zfill(2) for i in range(8,21)]
min_range = [str(i).zfill(2) for i in range(0,60)]
offset = ["03:00"]

def gen_snils():
    snils_format = '{Num1}-{Num2}-{Num3} {Num4}'
    argz = {'Num1': str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)), 
            'Num2': str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)), 
            'Num3': str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)), 
            'Num4': str(random.randint(0, 9)) + str(random.randint(0, 9))}
    return snils_format.format(**argz)


def num_of_card(pay_system, bank):
    card_format = '{fig} {fig2} {fig3} {fig4}'
    
    if pay_system == 'Мир':
        if bank == 'Сбербанк':
            figures = '2202'
        elif bank == 'Тинькофф':
            figures = '2200'
        elif bank == 'ВТБ':
            figures = '2204'
        else:
            figures = '2206'
    elif pay_system == 'MasterCard':
        if bank == 'Сбербанк':
            figures = '5469'
        elif bank == 'Тинькофф':
            figures = '5489'
        elif bank == 'ВТБ':
            figures = '5443'
        else:
            figures = '5406'
    else:
        if bank == 'Сбербанк':
            figures = '4276'
        elif bank == 'Тинькофф':
            figures = '4277'
        elif bank == 'ВТБ':
            figures = '4272'
        else:
            figures = '4279'
    
    argz = {'fig': figures, 
            'fig2': str(random.randint(1000, 9999)), 
            'fig3': str(random.randint(1000, 9999)), 
            'fig4': str(random.randint(1000, 9999))}
    
    return card_format.format(**argz)


def gen_name(gender):
    if gender == 'M':
        return random.choice(m_surnames) + " " + random.choice(m_names) + " " + random.choice(m_patronymics)
    else:
        return random.choice(w_surnames) + " " + random.choice(w_names) + " " + random.choice(w_patronymics)


def gen_time():
    argz = {"Year": random.choice(year_range),
            "Month": random.choice(month_range),
            "Day" : random.choice(day_range),
            "Hour": random.choice(hour_range),
            "Minute": random.choice(min_range),
            "Offset": random.choice(offset)
            }
    return iso_format.format(**argz)


def gen_pasp(nat):
    if nat == 'Rus':
        return str(random.randint(0, 8)) + str(random.randint(0, 9)) + str(random.choices(years_pasp)[0]) + ' ' + str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+str(random.randint(0, 9))
    elif nat == 'Bel':
        return str(random.choices(['AB', 'BM', 'HB', 'KH', 'MC', 'KБ', 'ПП'])[0]) + str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))
    elif nat == 'Kz':
        return 'N' + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))


def gen_dataset(MC, Visa, Mir, Sb, Tk, Vtb, Alp, size):
    df = pd.DataFrame({'ФИО':[], 'Паспортные данные':[], 'СНИЛС':[], 'Симптомы':[], 'Выбор врача':[], 
                       'Дата посещения врача':[], 'Анализы':[], 'Дата получения анализов':[], 
                       'Стоимость анализов':[], 'Карта оплаты':[]})
    for i in range(size):
        print(i)
        gender = random.choices(['M', 'F'])[0]
        nat = random.choices(['Rus', 'Bel', 'Kz'])[0]
        bank = random.choices(['Сбербанк', 'Тинькофф', 'ВТБ', 'Альфа'], weights = [Sb, Tk, Vtb, Alp])[0]
        pay_system = random.choices(['Мир', 'MasterCard', 'Visa'], weights = [Mir, MC, Visa])[0]
        analyze_cost = random.randint(1000, 9999)
        snils = gen_snils()
        passport = gen_pasp(nat)
        
        while snils in used_snils:
            snils = gen_snils()
        used_snils.append(snils)
        
        while passport in used_pasp:
            passport = gen_pasp(nat)
        used_pasp.append(passport)
        
        num = random.randint(0, 49)

        symps = str(symptoms[num])
        ans = str(analyzes[num])

        for i in range(random.randint(0, 4)):
            n = random.randint(0, 49)
            symps += ", " + str(symptoms[n])
            ans += ", " + str(analyzes[n])

        time = gen_time()
        time_new = (datetime.fromisoformat(time) + timedelta(hours=random.choices([24,48,72])[0])).isoformat()


        df.loc[len(df.index)] = [gen_name(gender), passport, snils, symps, doctors[num].replace("\n",""), 
                               time, ans, time_new, analyze_cost, num_of_card(pay_system, bank)]

    df.to_excel('Now.xlsx', index=False)



    
def clicked():
    try:
        size = int(txt.get())
    except:
        size = 1000
    if ((int(combo1.get()) + int(combo2.get()) + int(combo3.get())) != 100) or ((int(combo4.get()) + int(combo5.get()) + int(combo6.get()) + int(combo7.get())) != 100):
        messagebox.showinfo('Ошибка', 'Сумма в процентах не равна 100')    
    else:
        gen_dataset(int(combo1.get()), int(combo2.get()), int(combo3.get()), int(combo4.get()), 
                    int(combo5.get()), int(combo6.get()), int(combo7.get()), size)
        messagebox.showinfo('Готово', 'Создание таблицы завершено')
    
# Creating a window
window = Tk()
window.title("Конструктор синтетических данных")
window.geometry('500x400')

# Labels
lbl = Label(window, text="Добро пожаловать!", font='Arial 16 bold')  
lbl.place(relx=0.5, rely=0.1, anchor=CENTER)

lbl2 = Label(window, text="Перед началом работы выберите необходимые настройки:", font='Arial 12')  
lbl2.place(relx=0.5, rely=0.17, anchor=CENTER)

# Payment system processing:
lbl3 = Label(window, text="Платежная система:", font='Arial 11')
lbl3.place(relx=0.5, rely=0.25, anchor=CENTER)

t1 = Label(window, text="MasterCard, %")
t1.place(relx=0.044, rely=0.3)

t2 = Label(window, text="Visa, %")
t2.place(relx=0.44, rely=0.3)

t3 = Label(window, text="Мир, %")
t3.place(relx=0.79, rely=0.3)

combo1 = Combobox(window, width=10)  
combo1['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
combo1.current(3) 
combo1.place(relx=0.05, rely=0.37)

combo2 = Combobox(window, width=10)  
combo2['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
combo2.current(3) 
combo2.place(relx=0.4, rely=0.37)

combo3 = Combobox(window, width=10)  
combo3['values'] = (10, 20, 30, 40, 50, 60, 70, 80)  
combo3.current(1) 
combo3.place(relx=0.75, rely=0.37)

# Bank processing:
lbl4 = Label(window, text="Банк:", font='Arial 11')
lbl4.place(relx=0.5, rely=0.5, anchor=CENTER)

t4 = Label(window, text="Сбербанк, %")
t4.place(relx=0.044, rely=0.57)

t5 = Label(window, text="Тинькофф, %")
t5.place(relx=0.3, rely=0.57)

t6 = Label(window, text="ВТБ, %")
t6.place(relx=0.57, rely=0.57)

t7 = Label(window, text="Альфа-банк, %")
t7.place(relx=0.75, rely=0.57)

combo4 = Combobox(window, width=10)  
combo4['values'] = (10, 20, 30, 40, 50, 60, 70)  
combo4.current(2) 
combo4.place(relx=0.05, rely=0.65)

combo5 = Combobox(window, width=10)  
combo5['values'] = (10, 20, 30, 40, 50, 60, 70)  
combo5.current(2) 
combo5.place(relx=0.3, rely=0.65)

combo6 = Combobox(window, width=10)  
combo6['values'] = (10, 20, 30, 40, 50, 60, 70)  
combo6.current(2) 
combo6.place(relx=0.53, rely=0.65)

combo7 = Combobox(window, width=10)  
combo7['values'] = (10, 20, 30, 40, 50, 60, 70)  
combo7.current(0) 
combo7.place(relx=0.75, rely=0.65)

txt = Entry(window,width=20)  
txt.place(relx=0.2, rely=0.85)

lbl9 = Label(window, text="Введите количество строк", font='Arial 12')
lbl9.place(relx=0.3, rely=0.8, anchor=CENTER)

lbl11 = Label(window, text="Значение по умолчанию: 10000", font='Arial 8')
lbl11.place(relx=0.3, rely=0.95, anchor=CENTER)

btn = Button(window, text="Создать таблицу", command=clicked)
btn.place(relx=0.95, rely=0.95, anchor="se", width=150) 

window.mainloop()

