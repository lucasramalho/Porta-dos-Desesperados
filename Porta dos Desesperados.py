#       Grupo (apenas 1 aluno):
#               Nome: Lucas Alfonso Ramalho     RA: 138725
#       
#       ME323C: Porta dos Desesperados
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from random import randint

#Funcoes
def trocandoDePorta(iteracoes):
        """
                Faz o jogo com o jogador trocando de porta depois da revelacao, executando
                o numero desejado de iteracoes
        """
        vitoriasTrocando = 0
        for i in range(iteracoes):      #numero de iteracoes do jogo
                portas = [1, 2, 3]      #vetor utilizado pra saber para qual porta devera trocar
                premio = randint(1,3)   #seleciona qual porta tera o premio
                escolhida = randint(1,3)        #jogador escolhe uma porta
                portas.remove(escolhida)        #remove do vetor a porta ja escolhida (pois nao podera trocar para ela)
                for j in range(1, 4):
                        if j != escolhida and j != premio:      #abre uma porta que nao possui premio
                                errada = j
                portas.remove(errada)        #remove do vetor a porta aberta
                escolhida = portas[0]           #jogador troca de porta (unica troca possivel)
                if escolhida == premio:
                        vitoriasTrocando += 1
        return vitoriasTrocando



def semTrocarPorta(iteracoes):
        """
                Faz o jogo em que o jogador nao troca de porta
        """
        vitoriasNaoTrocando = 0
        for i in range(iteracoes):
                portas = [1, 2, 3]
                premio = randint(1,3)
                escolhida = randint(1,3)
                portas.remove(escolhida)
                for j in range(1, 4):
                        if j != escolhida and j != premio:
                                errada = j
                portas.remove(errada)
                if escolhida == premio:         #jogador nao troca de porta
                        vitoriasNaoTrocando += 1
        return vitoriasNaoTrocando



def imprimir(vt1, vnt1, vt2, vnt2, vt3, vnt3, vt4, vnt4, vt5, vnt5):
        """
                Funcao que imprime de maneira grafica os resultados dos 5 diferentes numeros de iteracoes
        """
        #listax onde x eh o numero de iteracoes. Ira conter o ponto no grafico
        lista10 = "                                                                                                    "
        lista50 = "                                                                                                    "
        lista100 = "                                                                                                    "
        lista1000 = "                                                                                                    "
        lista10000 = "                                                                                                    "

        #vtx: vitorias trocando a porta com um numero x de iteracoes
        #vntx: vitorias sem trocar a porta com um numero x de iteracoes
        vt1 = 10*vt1    #acertando a posicao do ponto na lista
        vnt1 = 10*vnt1  #(pois cada numero de iteracoes tera um resultado de ordem diferente, por exemplo 6 na de 10 iteracoes e 60 na de 100)

        vt2 = 2*vt2
        vnt2 = 2*vnt2

        vt4 = int(vt4/10)
        vnt4 = int(vnt4/10)

        vt5 = int(vt5/100)
        vnt5 = int(vnt5/100)

        #Colocando o ponto na lista
        lista10 = lista10[:vt1] + "-" + lista10[vt1:]
        lista10 = lista10[:vnt1] + "*" + lista10[vnt1:]

        lista50 = lista50[:vt2] + "-" + lista50[vt2:]
        lista50 = lista50[:vnt2] + "*" + lista50[vnt2:]

        lista100 = lista100[:vt3] + "-" + lista100[vt3:]
        lista100 = lista100[:vnt3] + "*" + lista100[vnt3:]

        lista1000 = lista1000[:vt4] + "-" + lista1000[vt4:]
        lista1000 = lista1000[:vnt4] + "*" + lista1000[vnt4:]

        lista10000 = lista10000[:vt5] + "-" + lista10000[vt5:]
        lista10000 = lista10000[:vnt5] + "*" + lista10000[vnt5:]

        #Imprimindo os resultados
        print("1: 10 iteracoes, 2: 50 iteracoes, 3: 100 iteracoes, 4: 1.000 iteracoes, 5: 10.000 iteracoes")
        print("*: sem trocar de porta;    -: trocando de porta\n")

        print("1: ", lista10)
        print("2: ", lista50)
        print("3: ", lista100)
        print("4: ", lista1000)
        print("5: ", lista10000)

        print("\n%:  0         .1        .2        .3        .4        .5        .6        .7        .8        .9        1")



#Programa Principal
for i in range(5):
        if i == 0:
                vt1 = trocandoDePorta(10)
                vnt1 = semTrocarPorta(10)
        if i == 1:
                vt2 = trocandoDePorta(50)
                vnt2 = semTrocarPorta(50)
        if i == 2:
                vt3 = trocandoDePorta(100)
                vnt3 = semTrocarPorta(100)
        if i == 3:
                vt4 = trocandoDePorta(1000)
                vnt4 = semTrocarPorta(1000)
        if i == 4:
                vt5 = trocandoDePorta(10000)
                vnt5 = semTrocarPorta(10000)

imprimir(vt1, vnt1, vt2, vnt2, vt3, vnt3, vt4, vnt4, vt5, vnt5)
input("Pressione qualquer tecla para encerrar")