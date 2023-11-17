#manipulacao de dados

biblioteca = {
    "titulo" : [],
    "autor" : [],
    "categoria": [],
    "valor": []
}
bibliotecaExemplo = {
    "titulo" : ["harry potter", "metamorfose"],
    "autor" : ["jk", "franz kafka"],
    "categoria" : [1, 2],
    "valor" : [105, 200]

}



categorias = ["Terror", "Aventura", "Sci-fi"]

def cadastrar():
    global biblioteca #ter certeza de que variavel biblioteca é o mesmo da global
    
    with open("antonio.txt", "a", encoding="utf-8") as arquivo:
        titulo = input("Digite o nome do livro: ")
        autor = input("Digite o nome do autor do livro: ")
    
        print(f"Essas sao as categorias disponiveis: {list(enumerate(categorias))}")
    
        categoria = int(input("Digite a qual categoria o livro pertence: "))
        preco = float(input("Digite o preço do livro: "))
        if biblioteca == {}:
            biblioteca = {
                "titulo" : [titulo],
                "autor" : [autor],
                "categoria" : [categoria],
                "valor" : [preco]
            }
        else:

            biblioteca["titulo"].append(titulo)
            biblioteca["autor"].append(autor)
            biblioteca["categoria"].append(categoria)
            biblioteca["valor"].append(preco)
        
    #arquivo.write(titulo + " " + autor + " " + str(categoria) + " " + str(preco) + "\n")
        arquivo.write(titulo + "\n") # I want each of these to be in one line
        arquivo.write(autor + "\n")
        arquivo.write(str(categoria) + "\n")
        arquivo.write(str(preco) + "\n")
        arquivo.close()


def deletar():
    # TODO: considerar se só tem um livro pra deletar e criar uma bibklioteca vazianesse caso
    global biblioteca #ter certeza de que variavel biblioteca é o mesmo da global
    if biblioteca == {}:
        print("A biblioteca está vazia!")
    else:
        listar()
        tituloParaDeletar = input("Digite o ID do livro que deseja deletar: ")
        if biblioteca["titulo"].count(tituloParaDeletar) > 1:
            #quero mostrar lista apenas do titulo, com autor,categoria e valor
            print("Escreva o nome do autor para confirmar o livro certo: ")
            for x in biblioteca:
                if biblioteca["titulo"][x]:
                    print(biblioteca[x])
            autorParaDeletar = input()


                    #get index to delete
            contador = -1
            for x in range(len(biblioteca["titulo"])):
                contador += 1
                if biblioteca["titulo"][x] == tituloParaDeletar and biblioteca["autor"][x] == autorParaDeletar:
                    indexParaDeletar = contador
                    break
            del biblioteca["titulo"][indexParaDeletar]
            del biblioteca["autor"][indexParaDeletar]
            del biblioteca["categoria"][indexParaDeletar]
            del biblioteca["valor"][indexParaDeletar]
        else:

            biblioteca = {}

def listar():
    global biblioteca
    if biblioteca == {}:
        print("A biblioteca está vazia!")
    for i in range(len(biblioteca['titulo'])):
        print(f"""{i}. '{biblioteca['titulo'][i]}' por {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; R$: {biblioteca["valor"][i]}.""")


def atualizar():
        posicao=int(input(f"Digite o número do livro que deseja modificar de acordo com a listagem: {listar()}"))
        item=input("Digite de qual categoria deseja modificar a informação:")
        novo=input("Qual será o novo valor?")


        if item == "titulo":
            biblioteca["titulo"][posicao] = novo

        elif item =="autor":
            biblioteca["autor"][posicao] = novo

        elif item =="categoria":
            biblioteca["categoria"][posicao] = novo

        elif item =="valor":
            biblioteca["valor"][posicao] = float(novo)
    
        

while True:
    print("\n Gerenciamento de Biblioteca Pessoal \n")
    print("1. Cadastrar Livro")
    print("\n2. Listar Livros")
    print("\n3. Atualizar Livro")
    print("\n4. Excluir Livro")
    print("\n5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar()
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '2':
        listar()
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '3':
        atualizar()
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '4':
        deletar()
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '5':
        break
    else:
        print("Tente novamente")
