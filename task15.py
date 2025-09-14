from rich.console import Console
from random import randint
console = Console()

def main():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    num3 = randint(1, 100)
    num4 = randint(1, 100)
    num5 = randint(1, 100)
    num6 = randint(1, 100)
    num7 = randint(1, 100)
    num8 = randint(1, 100)
    result = [randint(1, 100), "a",
randint(1, 100), "b",
randint(1, 100), "x",
randint(1, 100), "y",
randint(1, 100), "z",
randint(1, 100),
randint(1, 100),
randint(1, 100)]
    console.print(result, style = "yellow")


    start = (input("Qaysidan boshlab chiqarilsin? (1...13(agar hechnima qo'ymasangiz boshidan boshlab olib ketiladi)) "))
    end = (input("Qaysiga to'xtatilinsin? (1...13(agar hechnima qo'ymasangiz oxirgacha olib ketiladi)) "))
    start = int(start) - 1 if start.strip() else 0 # shunaqa qilsa ham bo'lardi
    end = int(end) - 1 if end.strip() else len(result)
    
    return result[start:end]

console.print(main(), style = "blue")
# 15 shartini 11 ga ham qilibman shuning uchun copy qilib qo'ydim chunki uje juda charchadim
