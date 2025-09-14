from rich.console import Console
from random import randint
console = Console()

def main():
    x = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
    console.print(f"Royxat: {x}", style = "yellow")

    if len(x) >= 5:
        console.print("Ko'p element! ", style = "green")

    else:
        console.print("Kam element", style = "red")

main()
