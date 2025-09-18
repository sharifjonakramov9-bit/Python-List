from rich.console import Console
console = Console()

def main():
    names = []
    
    while True:
        
        ism = input("Yangi ism kiriting (to'xtash uchun 'stop'): ")

        if ism.lower() == "stop":
            break
        names.append(ism)
    
    console.print(f"Siz {len(names)} ta ism kiritdingiz.", style="green")
    console.print(f"Ismlar ro'yxati: {names}", style="blue")

main()
