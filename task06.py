from rich.console import Console
console = Console()

def shaharlar():
    list1 = ["Toshkent", "Samaraqand", "Qashqadaryo", "Surxandaryo", "Navoi"]
    
    return list1[2]

console.print(shaharlar(), style = "green")
