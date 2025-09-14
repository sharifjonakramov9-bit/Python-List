from random import randint
from rich.console import Console
console = Console()

def main():
    x = randint(1, 10)
    y = randint(1, 10)
    z = randint(1, 10)
    
    list1 = [x, y, z]
    
    return list1[-1]

console.print(main(), style = "red")
