from rich.console import Console
from random import randint
console = Console()

def main():
    x = [randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100)]
    console.print(f"Asl ro'yxat: {x}", style="blue")

    y = x[-3:]
    console.print(f"Oxirgi 3 element: {y}", style="green")

main()
