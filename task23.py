from rich.console import Console
console = Console()

def main():
    numbers = [1, 2, 3, 4, 4, 5, 6, 7]
    console.print(f"Eski ro'yxat: {numbers}", style = "yellow")
    
    ind = numbers.index(1)
    
    console.print(f"Qiymat 1 indeksida: {ind}", style="blue")

main()
