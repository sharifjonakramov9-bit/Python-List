from rich.console import Console
console = Console()

def main():
    numbers = [1, 2, 3, 4, 4, 5, 6, 7]
    console.print(f"Eski ro'yxat: {numbers}", style = "yellow")
    
    numbers.pop(0)
    
    console.print(f"Yangilangan ro'yxat: {numbers}", style="blue")

main()
