# Домашнее задание по теме "Блокировки и обработка ошибок"

import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            random_number = random.randint(50, 500)
            self.balance = self.balance + random_number
            time.sleep(0.001)
            print(f"Пополнение: {random_number}. Баланс: {self.balance}.")
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()


    def take(self):
        for i in range(100):
            random_number = random.randint(50, 500)
            print(f"Запрос на {random_number}.")
            if random_number > self.balance:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            else:
                self.balance = self.balance - random_number
                time.sleep(0.001)
                print(f"Снятие: {random_number}. Баланс: {self.balance}.")



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')








