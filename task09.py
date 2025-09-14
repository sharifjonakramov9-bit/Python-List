from rich.console import Console
console = Console()

def main():
    x = ["Ali", "Vali", "Hasan"]
    y = [18, 10, 20]
    while True:
        result = [[x[i], y[i]] for i in range(len(x))]
        console.print(result, style = "blue")
        idk = input("nimani almashtirmoqchisiz? (ism/yosh/chiqish) ").lower()

        if idk == "ism":
            a = int(input("Qaysi ismni almashtirmoqchisiz?(1/2/3) ")) 

            if a == 1:
                chenge_name1 = input("Yangi ism kiriting: ").lower()
                x[0] = chenge_name1
            
            elif a == 2:
                chenge_name2 = input("Yangi ism kiriting: ").lower()
                x[1] = chenge_name2
            
            elif a == 3:
                chenge_name3 = input("Yangi ism kiriting: ").lower()
                x[2] = chenge_name3
            
            else:
                console.print("Bunaqa ism qatori mavjud emas!", style = "red")
            
        elif idk == "yosh":
            b = int(input("Qaysi yoshni almashtirmoqchisiz?(1/2/3) "))
            
            if b == 1:
                chenge_age1 = int(input("Yangi yoshni tanlang: "))
                y[0] = chenge_age1
            
            elif b == 2:
                chenge_age2 = int(input("Yangi yoshni tanlang: "))
                y[1] = chenge_age2
            
            elif b == 3:
                chenge_age3 = int(input("Yangi yoshni tanlang: "))
                y[2] = chenge_age3

            else:
                console.print("Bunday yosh qatori mavjud emas!", style = "red")

        elif idk == "chiqish":
            
            return result  
            
        
        else:
            console.print("Faqat ism yoki yosh almashtira olasiz!", style = "red")
    

print(main())
