import random
from time import sleep
from tkinter import *
cont = 1
pontos = 0

teste = Tk()
teste.title('Show do Milhão!')
teste.geometry('1000x700')
teste.configure(background='#008')
txt1=Label(teste,text="BEM VINDO AO SHOW DO MILHÃO!",background="#ff0",foreground='#000')#definindo um texto na interface
txt1.place(x=10, y=10, width= 350,height=30) #colocando as dimensoes do texto dentro da interface

print('\033[1m-='*20)
print('     BEM VINDO AO SHOW DO MILHÃO!')
print('-='*20)
sleep(1)
print('\n Você terá 5 rodadas de perguntas à sua frente, prepare-se!\n\n')
sleep(3)
caixa = {}

perguntas_e_respostas = ['Em qual bairro está localizado o IFPE Campus paulista?\n a) janga, b) maranguape 1, c) maranguape 2, d) pau amarelo\n',
            'Qual o nome da fronteira teórica ao redor de um buraco negro?\na) gravidade, b) super-nova, c) gigante branca, d)horizonte de eventos\n',
            'Qual o nome do jogo vencedor da premiação "Game of the Year 2015"?\na) the last of us, b) god of war, c) the witcher 3, d) red dead redemption 2\n',
            'Qual o nome da espaço-nave utilizada pela tripulação no filme "Interstellar"?\na) 737-800, b) endurance, c)rendezvouz, d) perseverance\n',
            'Em qual galáxia está localizado o maior buraco negro (até o momento) conhecido pela comunidade científica?\na) Messier 87, b) via-láctea, c) andrômeda, d) Canis Major Dwarf\n',
            'Qual personagem da mitologia grega construiu o famoso labirinto de creta?\na) Perseu, b) Rei minos, c) Dédalo, D) Dioniso\n',
            'Em qual missão espacial o homem pousou na lua pela primeira vez?\na) Apollo 11, b) Apollo 12, c) Apollo 13, d) Apollo 14\n',
            'Das opções abaixo, qual delas representa a forma mais limpa de geração de energia?\na) Hidreléticas, b) Fissão Nuclear, c) Fusão Nuclear, d) terméletricas\n',
            'Qual das opções abaixo não representa uma casa no universo da série televisiva "Game of Thrones"?\na) Lennister, b) Stark, c) Martell, d) Silva\n',
            'Em qual região do Brasil está localizado o estado do Amapá?\na) Norte, b) sul, c) sudeste, d) nordeste\n',
                        'Qual o nome do cantor conhecido como rei do pop?\na) Michael Jackson, b) Roberto Carlos, c) billy ocean, d) Tim Maia\n',
                         'Qual dessas NÃO é uma marca de computadores?\n a) Dell, b) apple, c) volkswagen, d) lenovo\n',
                         'Qual o nome do ônibus espacial que explodiu em 2003?\n a)Challenger, b) falcon-9, c) columbia, d) sts-700\n',
                         'Qual o nome da pessoa tida como o pai da computação?\na) Nikola Tesla, b) Alan Turing, c) Bill Gates, d) Steve Jobs\n',
                         'Qual das marcas de carros abaixo é especializada em carros elétricos?\na) Tesla, b) chevrolet, c) Volvo, d) Ford\n',
                         'Em qual ano terminou a segunda guerra mundial?\n a)1945, b) 1939, c) 1918, d) 1980\n',
                         'Quantos livros possui a saga Percy Jackson e os Olimpianos?\n a) 2, b) 8, c) 4, d) 5\n',
                         'De quem é a música Havana?\n a) Camila Cabello, b) Dua Lipa, C) Ivette Sangalo, d) Lulu Santos\n',
                         'Qual das bandas abaixo possui o integrante James Hetfield?\n a) Megadeth, b) Metallica, c) Slipknot, d) Angra\n',
                         'Qual era a cor do cavalo branco de napoleão?\n a) branco, b) marrom, c) cinza, d) preto',
                         'Quantas equipes competem na fórmula 1 atualmente?\n a) 10, b) 20, c) 15, d) 12',
                         'Qual a equipe mais tradicional da fórmula 1?\n a) Mercedes, b) Redbull, c) Ferrari, d) Aston Martim',
                         'Qual o nome do atual campeão mundial de fórmula 1?\n a) Sebastian Vettel, b) Max Verstappen, c) Lewis Hamilton, d) Kimi Raikkonen',
                         'Quantos títulos de copa do mundo possui a seleção brasileira de futebol?\n a) 5, b) 2, c) 3, d) 4',
                         'Quantas horas possui um dia exatamente?\n a) 24h, b) 22h30m, c) 23h56m, d) 23h:59m',
                         'Em que parte dos estados unidos fica o vale do silício?\n a) São Francisco, B) Los Angeles, c) Washington, d) Iowa',
                         'De qual vilão cinematográfico é a frase "Eu sou inevitável"?\n a) Voldemort, b) Arraia negra, c) Thanos, d) Caveira vermelha',
                         'Qual das séries abaixo é de origem asiática?\n a) Stranger Things, b) Mare of Easttown, c) Game of Thrones, d) Round 6',
                         'Qual dessas empresas pertence ao empresário Elon Musk?\n a) PayPal, b) SpaceX, c) Blue Origin, d) Amazon',
                         'Qual dos filmes abaixo é do diretor Quentim Tarantino?\n a) Vingadores, b) Pulp Fiction, c) Interstellar, d) Inception',
                         'Qual dos filmes abaixo é do diretor Christopher Nolan?\n a) Kill Bill, b) Interstellar, c) Laranja Mecânica, d) Bohemina Rhapsody',
                         'Qual o nome da primeira série dosPower Rangers?\n a)S.P.D, b) Mighty Morphin, c) Lost Galaxy, d) Lightspeed Rescue',
                         'Quantos meses possui um ano?\n a) 12, b) 13, c) 14, d) 15\n',
                         'Qual o nome do principal interesse amoroso do Geralt, na saga The witcher?\n a) Triss Merigold, b) Keira Metz, c) Cirilla Fiona, d) Yennefer',
                         'Qual o nome da fortaleza dos bruxos na saga The Witcher?\n a) Kaer Morhen, b) Hogwarts, c) Skellige, D) Novigrad\n',
                         'Qual dessas NÃO é uma plataforma de séries e filmes?\n a) Twitch, b) Netflix, c) HBO max, d) Prime Video',
                         'Qual dos jogos abaixo é um fps (first person shooter)?\n a) GTA 5, b) Hogwarts Legacy, c) Valorant, d) Watchdogs\n',
                         'Qual dessas não é um tipo de guitarra?\n a) Stratocaster, b) Stark, c) Explorer, d) Flying V',
                         'Qual das atrizes abaixo interpreta a capitã marvel nos cinemas?\n a) Scarlett Johansson, b) Brie Larson, c) Nina Dobrev, d) Victoria Justice',
                         'Quantos filmes possui a franquia Velozes e Furiosos até o momento[2022]?\n a) 5, b) 8, c) 7, d) 9']


while cont <= 5:
    cont+=1
    questaoescolhida = random.choice(perguntas_e_respostas)
    print(questaoescolhida)

    if questaoescolhida == perguntas_e_respostas[0]:
        op1 = input('\nDigite a resposta: ')
        if op1 in 'bB':
            print('RESPOSTA CORRETA!\n')
            pontos+=100
            sleep(2)

        else:
            print('Você errou... Fechando o programa.')
            break

    else:
        if questaoescolhida == perguntas_e_respostas[1]:
            op2 = input('\nDigite a resposta: ')
            if op2 in 'dD':
                print('RESPOSTA CORRETA! \n')
                pontos+=100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[2]:
            op3 = input('\nDigite a resposta: ')
            if op3 in 'cC':
                print('RESPOSTA CORRETA!\n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[3]:
            op4 = input('\nDigite a resposta: ')
            if op4 in 'bB':
                print('RESPOSTA CORRETA!\n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[4]:
            op5 = input('\nDigite a resposta: ')
            if op5 in 'aA':
                print('RESPOSTA CORRETA!\n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[5]:
            op6 = input('\nDigite a resposta: ')
            if op6 in 'cC':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[6]:
            op7 = input('\nDigite a resposta: ')
            if op7 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[7]:
            op8 = input('\nDigite a resposta: ')
            if op8 in 'cC':
                print('RESPOSTA CORRETA!\n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[8]:
            op9 = input('\nDigite a resposta: ')
            if op9 in 'dD':
                print('RESPOSTA CORRETA!\n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[9]:
            op10 = input('\nDigite a resposta: ')
            if op10 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[10]:
            op11 = input('\nDigite a resposta: ')
            if op11 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[11]:
            op12 = input('\nDigite a resposta: ')
            if op12 in 'cC':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[12]:
            op13 = input('\nDigite a resposta: ')
            if op13 in 'cC':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[13]:
            op14 = input('\nDigite a resposta: ')
            if op14 in 'bB':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[14]:
            op15 = input('\nDigite a resposta: ')
            if op15 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[15]:
            op16 = input('\nDigite a resposta: ')
            if op16 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[16]:
            op17 = input('\nDigite a resposta: ')
            if op17 in 'dD':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[17]:
            op18 = input('\nDigite a resposta: ')
            if op18 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[18]:
            op19 = input('\nDigite a resposta: ')
            if op19 in 'bB':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[19]:
            op20 = input('\nDigite a resposta: ')
            if op20 in 'dD':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[20]:
            op21 = input('\nDigite a resposta: ')
            if op21 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[21]:
            op22 = input('\nDigite a resposta: ')
            if op22 in 'cC':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[22]:
            op23 = input('\nDigite a resposta: ')
            if op23 in 'bB':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[23]:
            op24 = input('\nDigite a resposta: ')
            if op24 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[24]:
            op25 = input('\nDigite a resposta: ')
            if op25 in 'cC':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[25]:
            op26 = input('\nDigite a resposta: ')
            if op26 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[26]:
            op27 = input('\nDigite a resposta: ')
            if op27 in 'cC':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[27]:
            op28 = input('\nDigite a resposta: ')
            if op28 in 'dD':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[28]:
            op29 = input('\nDigite a resposta: ')
            if op29 in 'bB':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[29]:
            op30 = input('\nDigite a resposta: ')
            if op30 in 'bB':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[30]:
            op31 = input('\nDigite a resposta: ')
            if op31 in 'bB':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[31]:
            op32 = input('\nDigite a resposta: ')
            if op32 in 'bB':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[32]:
            op33 = input('\nDigite a resposta: ')
            if op33 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[33]:
            op34 = input('\nDigite a resposta: ')
            if op34 in 'dD':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[34]:
            op35 = input('\nDigite a resposta: ')
            if op35 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[35]:
            op36 = input('\nDigite a resposta: ')
            if op36 in 'aA':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[36]:
            op37 = input('\nDigite a resposta: ')
            if op37 in 'cC':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[37]:
            op38 = input('\nDigite a resposta: ')
            if op38 in 'bB':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[38]:
            op39 = input('\nDigite a resposta: ')
            if op39 in 'bB':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

        elif questaoescolhida == perguntas_e_respostas[39]:
            op40 = input('\nDigite a resposta: ')
            if op40 in 'dD':
                print('RESPOSTA CORRETA! \n')
                pontos += 100
                sleep(2)
            else:
                print('Você errou... Fechando o programa.')
                break

print(f'Sua pontuação foi de: {pontos}')


teste.mainloop()