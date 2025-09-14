from rich.console import Console
console = Console()

def main():
    x = int(input("Son kiriting: "))
    c = int(input("Son kiriting: "))
    o = int(input("Son kiriting: "))
    z = int(input("Son kiriting: "))
    y = int(input("Son kiriting: "))
    
    result = [x, c, o, z, y]
    console.print(f"Siz kiritgan sonlar {result}", style = "magenta")
    
    for i in range(len(result)):
        
        if i % 2 !=0:
            console.print("True", style = "green")
        
        else:
            console.print("False", style = "red")

main()

