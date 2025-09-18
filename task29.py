from rich.console import Console

console = Console()

def main():
    numbers = []
    
    for i in range(10):
        x = i + 1 
        num = input(f"{x} son kiriting: ")

        numbers.append(num)

        y = [z for z in numbers if numbers.count(z) == 1]

        console.print(f"Hamma sonlar: {numbers}", style = "magenta")
        console.print(f"Takrorlanmagan sonlar: {y}")

main()
