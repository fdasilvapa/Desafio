class Characters:
    # Método construtor do personagem
    def __init__(self, name, description, image_link, program, animator):
        self.name = name
        self.description = description
        self.image_link = image_link
        self.program = program
        self.animator = animator

    # Método que imprime as informações armazenadas nos inputs do loop
    def display(self):
        print("_" * 25)
        print(f"Nome: {self.name}")
        print(f"Descrição: {self.description}")
        print(f"Link da imagem: {self.image_link}")
        print(f"Programa: {self.program}")
        print(f"Animador responsável: {self.animator}")


# Lista que armazena os personagens
characters = []

# Contador para especificar qual é o personagem atual
cont = 1

# Loop para preenchimento das informações
while True:
    nameC = input(f"Nome do personagem {cont} (digite 'sair' para encerrar): ")
    if nameC.lower() == 'sair':
        break
    descriptionC = input("Descrição: ")
    image_linkC = input("Link da imagem: ")
    programC = input("Programa utilizado: ")
    animatorC = input("Animador responsável: ")

    # Atualizando contador
    cont += 1
    # Armazenando em uma variável essas informações
    character = Characters(nameC, descriptionC, image_linkC, programC, animatorC)
    # Adicionando essa variável com todos os atributos à lista
    characters.append(character)

    # Organização apenas
    print("_" * 40)

print("\nPersonagens criados:")

# Iteração na lista para usar o método de imprimir
for character in characters:
    character.display()
