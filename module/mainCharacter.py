import random
import os 
from rich import print

class mainCharacter: 
   
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.race = self.defineRace()
        self.classe = self.defineClass()
        self.defineStatus()

    def defineRace(name): 
        os.system('cls' if os.name == 'nt' else 'clear')
        raceN = -1
        while True:
            try:
                print("[red]Escolha sua Raça: [/red]")
                print("1 - Humano \n2 - Elfo\n3 - Anão ")
                raceN = int(input("Selecione sua Raça > "))
                if raceN < 1 or raceN > 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("[yellow]Opção inválida, escolha um número entre [/yellow]1 e 3. \n")
                else: 
                    break
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[yellow]Entrada inválida, por favor insira um número entre [/yellow] 1 e 3.\n")

        match raceN:
            case 1:
                return "Humano"       
            case 2: 
                return "Elfo"
            case 3: 
                return "Anão"
                
    def defineClass(name): 
        os.system('cls')
        classN = -1
        while True:
            try:
                print("[red]Classes: [/red]")
                print("1 - Barbaro \n2 - Ladino\n3 - Mago")
                classN = int(input("Selecione sua Classe > "))
                if classN < 1 or classN > 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("[yellow]Opção inválida, escolha um número entre [/yellow]1 e 3. \n")
                else:
                    break

            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[yellow]Opção inválida, escolha um número entre [/yellow]1 e 3. \n")
        
        match classN:
            case 1:
                return "Barbaro"
            case 2: 
                return "Ladino"
            case 3: 
                return "Mago"
    
    def defineStatus(self): 
        os.system('cls')
        numbersForStatus = []
        for i in range(5):
            numbersForStatus.append(random.randint(3,12))
        print("[red]Defina seus atributos: [/red]")
        print(f"    Seus números são {numbersForStatus}\n")

        status ={1 :'Força',
                 2 :'Destreza',
                 3 :'Sabedoria',
                 4 :'Constituição',
                 5 :'Sorte'
                }
        hasChoosed = []
        for i in range(5):         
            
            x = -1
            print(f"Você ainda deve escolher atributos para:")
            print(status)
            while x not in status.keys() or x in hasChoosed:
                try:
                    print(f'Para o valor: [red]{numbersForStatus[i]}[/red]')
                    x = int(input(f"    Escolha um atributo >  "))
                except ValueError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("[yellow]Opção inválida, escolha um número entre [/yellow]1 e 5. \n")
                    print(status)
                    continue
                if x in hasChoosed:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("[yellow]Atributo já escolhido, escolha outro.[/yellow]\n")
                    print(status)
                elif x not in status.keys():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("[yellow]Opção inválida, escolha um número entre [/yellow]1 e 5. \n")
                    print(status)
            hasChoosed.append(x)
            del status[x]

            match x:
                case 1:
                    self.stg = numbersForStatus[i]
                case 2: 
                    self.dex = numbersForStatus[i]
                case 3: 
                    self.wis = numbersForStatus[i]
                case 4: 
                    self.cons = numbersForStatus[i]
                case 5: 
                    self.luck = numbersForStatus[i]


    def showStatus(self):
    
        os.system('cls')
        os.system('cls')
        print('[red]Informações: [/red]')
        print(f"[blue]     Nome:[/blue] {self.name}\n[blue]     Level:[/blue] {self.level}\n[blue]     Raça:[/blue] {self.race}\n[blue]     Classe:[/blue] {self.classe}\n")
        print('[red]Atributos: [/red]')
        print(f"     [blue]Força:[/blue] {self.stg}\n     [blue]Destreza:[/blue] {self.dex}\n     [blue]Sabedoria:[/blue] {self.wis}\n     [blue]Constituição:[/blue] {self.cons}\n     [blue]Sorte:[/blue] {self.luck}\n")
        print('[red]Equipamentos: [/red]')

i= mainCharacter('Vinic')
i.showStatus()
