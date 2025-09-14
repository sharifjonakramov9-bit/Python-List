from rich.console import Console
console = Console()

def main():
    while True:    
        x = int(input("Son01 kiriting: "))
        c = int(input("Son02 kiriting: "))
        o = int(input("Son03 kiriting: "))
        z = int(input("Son04 kiriting: "))
        y = int(input("Son05 kiriting: "))

        result = [x, c, o, z, y]
        console.print(f"Siz kiritgan sonlar {result}", style = "magenta")
        chance = input("Berilgan ro'yxatni teskari qilib chuqush xoxlaysizmi? (ha/yo'q) ").lower()
    
        if chance == "ha":
            changed = result[::-1]
            console.print(f"Ro'yxat mufoyaqatli o'zgartirildi! {changed}", style = "green")

        elif chance == "yo'q":
            console.print(f"Royxat o'zgartirilmadi! {result}", style = "blue")
            break

        else:
            console.print("bunaqa buyruq yo'q!", style = "red")

print(main())
