# функція яка допоможе генерувати набір унікальних випадкових чисел
import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return []
    
    result = random.sample(range(min, max + 1), quantity)
    
    result.sort()
    return result

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
