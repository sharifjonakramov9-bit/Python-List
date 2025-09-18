from rich.console import Console
console = Console()

def main():
    numbers = ["Ali", "Vali", "Hasan", "Ali", "Ali", "Ali"]
    console.print(f"Eski ro'yxat: {numbers}", style = "yellow")
    
    ind = numbers.count("Ali")
    
    console.print(f"Ali ism {ind} marta qatnashgan.", style="blue")

main()
