from rich.console import Console
console = Console()

def main():
    numbers = ["Ali", "Vali", "Hasan", "Ali", "Ali", "Ali"]
    console.print(f"Eski ro'yxat: {numbers}", style = "yellow")
    
    x = numbers.copy()
    
    console.print(f"Yangi ro'yxat: {x}", style="blue")

main()
