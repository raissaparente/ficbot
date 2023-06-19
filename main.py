from fanfic_manager import Fanfic, delay

print('BEM VINDO(A) AO ADMINISTRADOR DE FANFICS!')
print('Vamos registrar sua fanfic?')
delay()

#inicializa instancia e faz registro basico
fic = Fanfic()
delay()
print(f'Fic "{fic.titulo} by {fic.autor}" cadastrada!')

while True:
    delay()
    opcao_menu = int(input('E agora, que gostaria de fazer?\n'
                  '[1] FAZER ACRESCIMO AO REGISTRO\n'
                  '[2] CONSULTAR REGISTRO\n'
                  '[3] COMPARAR COM PÁGINAS\n'
                  '[4] COMPARAR COM LIVRO\n'
                  '[5] SAIR\n'))

    delay()
    match opcao_menu:
        case 1:
            fic.cadastro_adicional()
        case 2:
            opcao = int(input('O que gostaria de consultar?\n'
                  '[1] TITULO\n'
                  '[2] AUTOR(A)\n'
                  '[3] CONTAGEM DE PALAVRAS\n'
                  '[4] SITE\n'
                  '[5] FANDOM\n'
                  '[6] GÊNERO\n'
                  '[7] SHIP\n'))
            consulta = fic.consulta(opcao)
            print(f'O {consulta[0]} da fic é {consulta[1]}.')
        case 3:
            print(f'Essa fic tem {fic.wordcount}, isso equivalente aproximadamanete a {fic.paginas:.0f} páginas.')
        case 4:
            livro_comparado = fic.compare_livro()
            print(f"UAU! Ao ler {fic.titulo} é como se você tivesse lido {livro_comparado[0]}, escrito por {livro_comparado[1]}!")
        case 5:
            print(f'VOLTE SEMPRE!')
            break
