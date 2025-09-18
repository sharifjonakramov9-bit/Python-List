from rich.console import Console
console = Console()

def main():
    numbers = ["Ali", "Vali", "Hasan", "Ali", "Ali", "Ali"]
    console.print(f"Eski ro'yxat: {numbers}", style = "yellow")
    
    numbers.clear()
    
    console.print(f"Yangi ro'yxat: {numbers}", style="blue")

main()
