from rich.console import Console
console = Console()

def main():
    numbers = ["Ali", "Vali", "Hasan", "Ali", "Ali", "Ali"]
    console.print(f"Eski ro'yxat: {numbers}", style = "yellow")
    
    numbers.sort()
    
    console.print(f"Alfavit bo'yicha: {numbers} ", style="blue")

main()
