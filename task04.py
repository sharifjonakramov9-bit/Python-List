from rich.console import Console
console = Console()

def main():
    while True:
        x = input("Ism kiriting: ")
        y = input("Ism kiriting: ")
        z = input("Ism kiriting: ")
        
        if x.isalpha() and y.isalpha() and z.isalpha():
            result = [x, y, z]
            
            return result

        else:
            console.print("Faqat Isim kiriting!", style = "red")
            
            continue

    return result

console.print(main(), style='blue')
