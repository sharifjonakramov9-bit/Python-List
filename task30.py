from rich.console import Console

console = Console()

def main():
    numbers = []
    
    for i in range(5):
        x = i + 1 
        num = input(f"{x} Matn kiriting: ")

        numbers.append(num)

        y = [z for z in numbers if z.lower() == z.lower()[::-1]]

        console.print(f"Hamma so'zlar: {numbers}", style = "magenta")
        console.print(f"Plandrinoma so'zlar: {y}")

main()
