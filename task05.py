from rich.console import Console
console = Console()

def main():
    names = ['Ali', 'Vali', 'Hasan']
    ages = [15, 19, 8]

    result = [[names[i], ages[i]] for i in range(len(names))]
    
    return result

console.print(main(), style='blue')

