from rich.console import Console

console = Console()

def main():
    numbers = []
    
    for i in range(10):
        x = i + 1 
        num = int(input(f"{x} son kiriting: "))

        numbers.append(num)

        c = 0
        d = None

        for n in numbers:
            if numbers.count(n) > c:
                c = numbers.count(n)
                d = n

        console.print(f"Hamma sonlar: {numbers}", style = "magenta")
        console.print(f"Takrorlangan son(eng ko'p): {d}")

main()
