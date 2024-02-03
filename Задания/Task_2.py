#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования [].
Максимально возможный размер списка задать константой. В отдельном поле size должно
храниться максимальное для данного объекта количество элементов списка; реализовать метод
size(), возвращающий установленную длину. Если количество элементов списка изменяется во
время работы, определить в классе поле count. Первоначальные значения size и count
устанавливаются конструктором.
В тех задачах, где возможно, реализовать конструктор инициализации строкой.
-------------------------------------------------------------------------------------------------------------------
Используя класс Bill , реализовать класс ListPayer. Класс содержит список плательщиков за
телефонные услуги, дату создания списка, номер списка. Поля одного элемента списка —
это: плательщик (класс Bill), признак оплаты, дата платежа, сумма платежа. Реализовать
методы добавления плательщиков в список и удаления их из него; метод поиска
плательщика по номеру телефона и по фамилии, по дате платежа. Метод вычисления
полной стоимости платежей всего списка. Реализовать операцию объединения и операцию
пересечения списков. Реализовать операцию генерации конкретного объекта Group
(группа), содержащего список плательщиков, из объекта типа ListPayer. Должна быть
возможность выбирать группу плательщиков по признаку оплаты, по атрибутам, по дате
платежа, по номеру телефона."""
from datetime import datetime

class Bill:
    """
    Класс счета (плательщика). Содержит информацию о плательщике, номере телефона,
    дате платежа, сумме и статусе оплаты.
    """
    def __init__(self, payer, phone_number, payment_date, amount, is_paid=False):
        # Инициализация счета
        self.payer = payer  # Фамилия плательщика
        self.phone_number = phone_number  # Номер телефона
        self.payment_date = datetime.strptime(payment_date, '%Y-%m-%d')  # Дата платежа
        self.amount = amount  # Сумма платежа
        self.is_paid = is_paid  # Признак оплаты

    def __repr__(self):
        # Возвращение строкового представления счета
        return f"{self.payer}, {self.phone_number}, {self.payment_date.strftime('%Y-%m-%d')}, {self.amount}, {'Оплачено' if self.is_paid else 'Не оплачено'}"

class ListPayer:
    """
    Класс списка плательщиков. Содержит список счетов (объектов класса Bill),
    дату создания списка и его номер.
    """
    MAX_SIZE = 100  # Максимальный размер списка

    def __init__(self, list_number, creation_date):
        # Инициализация списка плательщиков
        self.bills = []  # Список счетов
        self.list_number = list_number  # Номер списка
        self.creation_date = datetime.strptime(creation_date, '%Y-%m-%d')  # Дата создания списка
        self.size = ListPayer.MAX_SIZE  # Максимальный размер списка
        self.count = 0  # Текущее количество элементов в списке

    def add_payer(self, bill):
        # Добавление плательщика в список
        if self.count < self.size:
            self.bills.append(bill)
            self.count += 1
        else:
            print("Достигнут максимальный размер списка. Добавление невозможно.")

    def remove_payer(self, phone_number):
        # Удаление плательщика из списка по номеру телефона
        self.bills = [bill for bill in self.bills if bill.phone_number != phone_number]
        self.count = len(self.bills)

    def find_by_phone(self, phone_number):
        # Поиск плательщика по номеру телефона
        return [bill for bill in self.bills if bill.phone_number == phone_number]

    def find_by_payer(self, payer):
        # Поиск плательщика по фамилии
        return [bill for bill in self.bills if bill.payer == payer]

    def find_by_date(self, payment_date):
        # Поиск плательщика по дате платежа
        date = datetime.strptime(payment_date, '%Y-%m-%d')
        return [bill for bill in self.bills if bill.payment_date == date]

    def total_amount(self):
        # Вычисление общей суммы платежей
        return sum(bill.amount for bill in self.bills)

    def __getitem__(self, index):
        # Получение плательщика по индексу
        return self.bills[index]

    def __len__(self):
        # Возвращение текущего количества элементов в списке
        return len(self.bills)

    def __repr__(self):
        # Возвращение строкового представления списка плательщиков
        return f"Номер списка: {self.list_number}, Дата создания: {self.creation_date.strftime('%Y-%m-%d')}, Счета: {self.bills}"

# Демонстрация использования классов
if __name__ == '__main__':
    list_payers = ListPayer('001', '2023-01-01')
    list_payers.add_payer(Bill('Иванов Иван', '123456789', '2023-02-01', 100, True))
    list_payers.add_payer(Bill('Петров Петр', '987654321', '2023-02-02', 150, False))

    print("Общая сумма платежей:", list_payers.total_amount())
    print("Поиск по номеру телефона '123456789':", list_payers.find_by_phone('123456789'))
    print("Поиск по фамилии 'Петров Петр':", list_payers.find_by_payer('Петров Петр'))
    print("Поиск по дате платежа '2023-02-01':", list_payers.find_by_date('2023-02-01'))

    print("Все плательщики:", list_payers)