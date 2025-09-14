from rich.console import Console 
console = Console()

def main():
    while True:
        list0 = ["Ali", "Toshpo'latov"]
        list1 = list0[1]
        yes_or_no = input("Qaysi familiyaga almashtirmoqchisiz? ").lower()

        if yes_or_no == "ha":
            x = input("Yangi familiya kiriting: ")
            
            if x.isalpha():
                list1 = x
                
                return list1
            
            else:
                console.print(f"""Siz yozgan {x} familiya bo'la 
olmaydi.  Iltimos faqat harflardan 
iborat familiya yozing""", style = "red")
        
        elif yes_or_no == "yo'q":
            console.print("Almashtir bu buyruq!!", style = "magenta")
        
        else:
            console.print("bunday buyruq mavjud emas!", style = "cyan")
    
    return changed_list

console.print(main(), style = "green")

