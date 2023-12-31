#manipulacao de dados


def inicializar():
    biblioteca = {
    "titulo" : [],
    "autor" : [],
    "categoria": [],
    "valor": []
    }
    
    try:
        with open("minhaBiblioteca.txt", "r", encoding = "utf-8") as arquivo:#abre e fecha o arquivo automaticamente
            for linha in arquivo:
                linha = linha.strip() # se nao usar strip, printa \n
                if linha == "":
                    break #sair do loop caso linha esteja em branco, significa que nao ha mais livros. Um failsafe.
                else:
                    biblioteca["titulo"].append(linha)         
                    linha = next(arquivo).strip()
                    biblioteca["autor"].append(linha)
                    linha = next(arquivo).strip()
                    biblioteca["categoria"].append(int(linha))
                    linha = next(arquivo).strip()
                    biblioteca["valor"].append(float(linha))
    except FileNotFoundError:
        print("Arquivo txt nao foi encontrado!")
        print("Criaremos um arquivo para voce.")
        arquivo = open("minhaBiblioteca.txt", "w")
        arquivo.close()

    return biblioteca


categorias = ["Terror", "Aventura", "Sci-fi","Romance","Infantil","Drama","Gêneros Literário","Young Adult", "Outros"]

def cadastrar(biblioteca):
    while True:
        titulo = input("Digite o nome do livro: ")
        if titulo=="" or titulo.strip()=="":#1 espaço vazio ou vários continua o looping, o titulo.strip()=="" tira os espaços vazio da extremidade e se mesmo assim continua vazio continua o looping
            print("Por favor, digite algo!")
        else:
            break 
    while True:
        autor = input("Digite o nome do autor do livro: ")
        autor_sem_espacos = autor.replace(" ", "")  # trocar os espaço em branco por nada, assim removendo espaços em branco
        if autor_sem_espacos.isalpha():
            break
        else:
            print("Por favor, digite apenas letras do alfabeto!")

    print("Essas são as categorias disponíveis:")
    for indice, categoria in enumerate(categorias):#para obter o indice e a categoria
        print(f"{indice}. {categoria}")
    while True:
        categoria = input("Digite a qual categoria o livro pertence (número): ")
        if categoria.isdigit() == True:# isdigit() retorna True se a string for números de 0-9
            if len(categoria)==1:
                break
            elif len(categoria)!=1:
                print("Por favor, digite um número de 1 digito no intervalo de 0-9!")
        else:
            print('Por favor, digite um número de 0-9 correspondente a categoria do seu livro!')

    preco = float(input("Digite o preço do livro: "))

    biblioteca["titulo"].append(titulo)
    biblioteca["autor"].append(autor)
    biblioteca["categoria"].append(categoria)
    biblioteca["valor"].append(preco)

    with open("minhaBiblioteca.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{titulo}\n{autor}\n{categoria}\n{preco}\n")

def deletar(biblioteca):
    if biblioteca == {}:
        print("A biblioteca está vazia!")
    else:
        listarSimples(biblioteca)
        try:
            idParaDeletar = int(input("Digite o número do livro que deseja deletar: "))
            del biblioteca["titulo"][idParaDeletar]
            del biblioteca["autor"][idParaDeletar]
            del biblioteca["categoria"][idParaDeletar]
            del biblioteca["valor"][idParaDeletar]
            doDicionarioParaFile(biblioteca) # quero reescrever o file INTEIRO, baseado na nova biblioteca
        except IndexError:
            print("Não existe livro com esse valor.\nAção cancelada.")
        except ValueError:
            print("Escreva um número")

def doDicionarioParaFile(biblioteca):
    with open("minhaBiblioteca.txt", ("w"), encoding="utf-8") as arquivo:# abre e fecha o arquivo automaticamente
        for i in range(len(biblioteca["titulo"])):
            arquivo.write(biblioteca["titulo"][i] + "\n") 
            arquivo.write(biblioteca["autor"][i] + "\n")
            arquivo.write(str(biblioteca["categoria"][i]) + "\n")
            arquivo.write(str(biblioteca["valor"][i]) + "\n")

def listar(biblioteca):
    print(" 1-Listar Tudo\n2-Listar filtrado por categoria\n3-Listar Gastos Totais\n4- Listar gastos filtrado por categoria")
    choice = int(input("Escolha uma das opções de listar: "))
    if biblioteca == {} or biblioteca == {
        "titulo": [],
        "autor": [],
        "categoria": [],
        "valor":[]
        }: 
        print("A biblioteca está vazia!")
        
    if choice == 1:
        for i in range(len(biblioteca['titulo'])):
            print(f"""{i}. '{biblioteca['titulo'][i]}' por {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; R$: {biblioteca["valor"][i]}\n""")
    elif choice == 2:
        print("Essas são as categorias disponíveis:")
        for indice, categoria in enumerate(categorias):#para obter o indice e a categoria
            print(f"{indice}. {categoria}")
        choiceCategoria = int(input("\nQual categoria? "))
        livros_encontrados = False
        for i in range(len(biblioteca['titulo'])):#vai rodar o n° de livros na biblioteca
            if biblioteca['categoria'][i] == choiceCategoria:# se a chave e o valor for igual com a categoria e 
                print(f"""{i}. '{biblioteca['titulo'][i]}' por {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; R$: {biblioteca["valor"][i]}\n""")
                livros_encontrados = True
        if livros_encontrados == False:
            print(f'Você não possui livros dessa categoria!')
    elif choice == 3:
        custoTotal = 0
        for i in range(len(biblioteca['titulo'])):
            custoTotal += biblioteca["valor"][i]
        print(f"R${custoTotal:.2f}")
    elif choice == 4:
        custoTotal = 0
        print("Essas são as categorias disponíveis:")
        for indice, categoria in enumerate(categorias):#para obter o indice e a categoria
            print(f"{indice}. {categoria}")
        choiceCategoria = int(input("\nQual categoria? "))
        livros_encontrados = False        
        for i in range(len(biblioteca['titulo'])):
            if biblioteca['categoria'][i] == choiceCategoria:
                custoTotal += biblioteca["valor"][i]
                livros_encontrados = True
                print(f"R${custoTotal:.2f}")
        if livros_encontrados == False:
            print(f'Você não possui livros dessa categoria!')
        
def listarSimples(biblioteca):
    for i in range(len(biblioteca['titulo'])):
                print(f"""{i}. '{biblioteca['titulo'][i]}' por {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; R$: {biblioteca["valor"][i]}.""")

def atualizar(biblioteca):
        listarSimples(biblioteca)
        posicao=int(input(f"Digite o número do livro que deseja modificar de acordo com a listagem:"))
        print("1- titulo\n2- autor\n3-genero\n4-valor\n")
        item=int(input("Digite o número de qual elemento você quer editar: "))
        novo=input("Qual será o nova informação?")
        
        if item == 1:
            biblioteca["titulo"][posicao] = novo
            
        elif item ==2:
            biblioteca["autor"][posicao] = novo
            
        elif item ==3:
            biblioteca["categoria"][posicao] = int(novo)

        elif item ==4:
            biblioteca["valor"][posicao] = float(novo)
        livro_atualizado = {
        "titulo": biblioteca["titulo"][posicao],
        "autor": biblioteca["autor"][posicao],
        "categoria": biblioteca["categoria"][posicao],
        "valor": biblioteca["valor"][posicao]
        }
        print(f"{posicao}. '{livro_atualizado['titulo']}' por {livro_atualizado['autor']}\n"
              f"{categorias[livro_atualizado['categoria']]} ; R$: {livro_atualizado['valor']}\n")
        doDicionarioParaFile(biblioteca)
                
biblioteca= inicializar() #para retornar a variavel biblioteca que é uma variável local da função inicializar(), para poder usá-la fora da função inicializar()

while True:
    print("\n Gerenciamento de Biblioteca Pessoal \n")
    print("1. Cadastrar Livro")
    print("\n2. Listar Livros")
    print("\n3. Atualizar Livro")
    print("\n4. Excluir Livro")
    print("\n5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar(biblioteca)
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '2':
        listar(biblioteca)
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '3':
        atualizar(biblioteca)
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '4':
        deletar(biblioteca)
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '5':
        break
    else:
        print("Tente novamente")
