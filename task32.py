from rich.console import Console

console = Console()

def main():
    numbers = []
    x = []

    while True:
        num = input("So'z kiriting(to'xtash uchun stop yozin!): ")

        if num.lower() == "stop":
            break

        numbers.append(num)

        for n in numbers:
            if len(n) > 5:
                x.append(n)
           

        console.print(f"Hamma so'zlar: {numbers}", style = "magenta")
        console.print(f"Uzun so'zlar: {x}")

main()
