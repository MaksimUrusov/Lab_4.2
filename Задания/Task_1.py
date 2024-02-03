#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав
имеющиеся в Python средства перегрузки операторов."""
class Pair:
    def __init__(self, first=0, second=0):
        self.set_values(first, second)

    def set_values(self, first, second):
        if not isinstance(first, int) or not isinstance(second, int) or second < 0:
            raise ValueError("Некорректные значения: first должно быть целым числом, second - положительным целым числом.")
        self.first = first
        self.second = second

    def read(self):
        first = int(input("Введите целую часть числа: "))
        second = int(input("Введите дробную часть числа (как положительное целое число): "))
        self.set_values(first, second)

    def display(self):
        print(f"Число: {self.first}.{str(self.second).zfill(2)}")

    def multiply(self, multiplier):
        if not isinstance(multiplier, int):
            raise ValueError("Множитель должен быть целым числом.")
        # Преобразование в число с плавающей точкой для умножения
        full_number = float(f"{self.first}.{str(self.second).zfill(2)}")
        result = full_number * multiplier
        self.first, self.second = map(int, str(result).split('.'))

    # Перегрузка оператора умножения
    def __mul__(self, other):
        self.multiply(other)
        return self

def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(e)
        return None

if __name__ == '__main__':
    pair = make_pair(12, 34)
    if pair is not None:
        pair.display()

        pair.read()
        pair.display()

        multiplier = int(input("Введите множитель: "))
        pair * multiplier  # Используем перегруженный оператор умножения
        print("После умножения:")
        pair.display()