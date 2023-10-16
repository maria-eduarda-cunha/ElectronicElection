#Inicialização das listas

  #Candidatos
presidente = [] #[[votos, idade, nome, número, partido, cargo]]
governador = []
prefeito = []

  #Eleitores
eleitores = []
votantes = []

  #Votos brancos e nulos
branco = [0, 0, 0] #[votos prefeito, votos governador, votos presidente]
nulo = [0, 0, 0] #[votos prefeito, votos governador, votos presidente]

 #Informações dos candidatos para a realização do ranking
rankingPrefeito = sorted(prefeito, key=lambda x: (x[0], -x[3] if x[0] == prefeito[0][0] else x[3]), reverse=True)
rankingGovernador = sorted(governador, key=lambda x: (x[0], -x[3] if x[0] == governador[0][0] else x[3]), reverse=True)
rankingPresidente = sorted(presidente, key=lambda x: (x[0], -x[3] if x[0] == presidente[0][0] else x[3]), reverse=True)

 #Partidos com mais políticos eleitos e Total de votos apurados
partidos = {}
Total = []

#Definição das funções

  #Cadastrar candidatos
def cadastroCandidatos(cargo):
  print("\n***Cadastrar Candidatos***")
  nome = input("Nome: ")
  idade = int(input("Idade: "))
  numero = int(input("Número: "))
  partido = input("Partido: ")
  votos = 0
  candidatos = [votos, idade, nome, numero, partido, cargo]
  return candidatos

  #Cadastrar eleitores
def cadastroEleitor():
  print("\n***Cadastrar Eleitores***")
  nome = input("Nome: ").lower()
  cpf = int(input("CPF: "))
  eleitores = [nome, cpf]
  return eleitores

  #Votar em candidatos
def votarCandidato(cargo):
  continuar = True
  while continuar:
    votoCandidato = int(input("\nDigite -1 para branco e -2 para nulo\nNúmero do candidato que deseja votar: "))
    if votoCandidato == -1:
      return "branco"   
    elif votoCandidato == -2:
      return "nulo"
    else:
      for i in range(len(cargo)):
        if votoCandidato == cargo[i][3]:
          print(f"\nCandidato Selecionado: {cargo[i][2]}")
          continuar = False
          return i
        else:
          print("\nNúmero de candidato inválido, digite novamente.")
          break

  #Confirmar a opção
def confirmar():
  confirmar = input("\nDeseja confirmar?\n(Digite sim ou não): ").lower()
  if confirmar == "sim":
    return True
  else:
    return False

  #Apurar resultados
def apuracao(presidente, governador, prefeito):
   #Tabela para presidente
  print('''
  ***RANKING DO RESULTADO PARA PRESIDENTE***
  Nome\t\t\tPartido\t\tTotal de Votos\t\t%Votos Válidos''')
  t = 0
  for x in range(len(presidente)):
    por = "%"
    nome = rankingPresidente[x][2]
    partido = rankingPresidente[x][4]
    totalCandidato = rankingPresidente[x][0] + branco[2] + nulo[2]
    t += rankingPresidente[x][0]
    totalVotos = len(votantes)
    votosValidos = rankingPresidente[x][0] * 100 / totalCandidato
    print(x + 1, ".", "%-11s%6s%13d%22.2f" % (nome, partido, totalCandidato, votosValidos))
  porcentagemValidos = (t * 100) / totalVotos
  print("Total de votos:", totalVotos)
  print("Total de votos válidos e % = ", "%-2.0f%7.2f%0s" % (t,porcentagemValidos, por))
  totalBranco = branco[2]
  porcentagemBranco = (totalBranco * 100) / totalVotos
  print("Total de votos brancos e % = ", "%-2.0f%7.2f%0s" % (totalBranco, porcentagemBranco, por))
  totalNulo = nulo[2]
  porcentagemNulo = (totalNulo * 100) / totalVotos
  print("Total de votos nulos e % =   ", "%-2.0f%7.2f%0s" % (totalNulo, porcentagemNulo, por))
  Total.append(t)

   #Tabela para governador
  print('''
  ***RANKING DO RESULTADO PARA GOVERNADOR***
  Nome\t\t\tPartido\t\tTotal de Votos\t\t%Votos Válidos''')
  t = 0
  for x in range(len(governador)):
    por = "%"
    nome = rankingGovernador[x][2]
    partido = rankingGovernador[x][4]
    totalCandidato = rankingGovernador[x][0] + branco[1] + nulo[1]
    t += rankingGovernador[x][0]
    totalVotos = len(votantes)
    votosValidos = rankingGovernador[x][0] * 100 / totalCandidato
    print(x + 1, ".", "%-11s%6s%13d%22.2f" % (nome, partido, totalCandidato, votosValidos))
  porcentagemValidos = (t * 100) / totalVotos
  print("Total de votos:", totalVotos)
  print("Total de votos válidos e % = ", "%-2.0f%7.2f%0s" % (t, porcentagemValidos, por))
  totalBranco = branco[1]
  porcentagemBranco = (totalBranco * 100) / totalVotos
  print("Total de votos brancos e % = ", "%-2.0f%7.2f%0s" % (totalBranco, porcentagemBranco, por))
  totalNulo = nulo[1]
  porcentagemNulo = (totalNulo * 100) / totalVotos
  print("Total de votos nulos e % =   ", "%-2.0f%7.2f%0s" % (totalNulo, porcentagemNulo, por))
  Total.append(t)
    
   #Tabela para prefeito
  print('''
  ***RANKING DO RESULTADO PARA PREFEITO***
  Nome\t\t\tPartido\t\tTotal de Votos\t\t%Votos Válidos''')
  t = 0
  for x in range(len(prefeito)):
    por = "%"
    nome = rankingPrefeito[x][2]
    partido = rankingPrefeito[x][4]
    totalCandidato = rankingPrefeito[x][0] + branco[0] + nulo[0]
    t += rankingPrefeito[x][0]
    totalVotos = len(votantes)
    votosValidos = rankingPrefeito[x][0] * 100 / totalCandidato
    print(x + 1, ".", "%-11s%6s%13d%22.2f" % (nome, partido, totalCandidato, votosValidos))
  porcentagemValidos = (t * 100) / totalVotos
  print("Total de votos:", totalVotos)
  print("Total de votos válidos e % = ", "%-2.0f%7.2f%0s" % (t, porcentagemValidos, por))
  totalBranco = branco[0]
  porcentagemBranco = (totalBranco * 100) / totalVotos
  print("Total de votos brancos e % = ", "%-2.0f%7.2f%0s" % (totalBranco, porcentagemBranco, por))
  totalNulo = nulo[0]
  porcentagemNulo = (totalNulo * 100) / totalVotos
  print("Total de votos nulos e % =   ", "%-2.0f%7.2f%0s" % (totalNulo, porcentagemNulo, por))
  Total.append(t)

  #Relatório e Estatística
def relatorio(votantes, partidos, Total):  
   #Lista	dos	votantes, ordenados	por	nome
  listaVotantes = sorted(votantes)
  print('''
  ***LISTA DOS ELEITORES QUE VOTARAM***''')
  for eleitor in listaVotantes:
     print(eleitor[0])
   #Adiciona em uma lista o partido que ficou em primeiro lugar de cada cargo:
  if rankingPresidente[0][4] in partidos: 
    partidos[rankingPresidente[0][4]] += 1
  else:
    partidos[rankingPresidente[0][4]] = 1
  if rankingGovernador[0][4] in partidos: 
    partidos[rankingGovernador[0][4]] += 1
  else:
    partidos[rankingGovernador[0][4]] = 1
  if rankingPrefeito[0][4] in partidos:
    partidos[rankingPrefeito[0][4]] += 1
  else:
    partidos[rankingPrefeito[0][4]] = 1
  
  if len(listaVotantes) == (sum(Total) + sum(branco) + sum(nulo))/3:
    print("\n*Votação Auditada!*\n")
     #Partidos que elegeram mais ou menos políticos
    mais = max(partidos, key=partidos.get)
    menos = min(partidos, key=partidos.get)
    quantidadeMais = partidos[mais]
    quantidadeMenos = partidos[menos]
    print(f"O partido que elegeu mais políticos: {mais}. Com {quantidadeMais} eleitos.")
    print(f"O partido que elegeu menos políticos: {menos}. Com {quantidadeMenos} eleitos.")
  else:
    print("\n*Problema na Auditoria!*")

#Menu

#Inicia a variável de opção do menu
op = 0

#Faz com que o programa pare de executar caso a opção escolhida seja 7 ou mais
while op < 7:
  op = int(input("\n***Selecione a opção desejada: ***\n1. Cadastrar Candidatos\n2. Cadastrar Eleitores\n3. Votar\n4. Apurar Resultados\n5. Relatório e Estatísticas\n6. Gravar Apuração\n7. Encerrar\n\nOpção Escolhida: "))
  
  #Inicializando condição para loop
  continuar = True
  #Diminuindo as comparações de pior caso
  if op < 4:
    #Opção 1
    if op == 1:
      while continuar:
      
        #Verificando qual o cargo do candidato
        cargo_op = int(input("\n***Selecione o cargo do candidato: ***\n1. Presidente\n2. Governador\n3. Prefeito\n\nOpção escolhida: "))
      
        #Adicionando as informações do candidato em sua respectiva lista
        if cargo_op == 1:
          presidente.append(cadastroCandidatos("presidente"))
        elif cargo_op == 2:
          governador.append(cadastroCandidatos("governador"))
        elif cargo_op == 3:
          prefeito.append(cadastroCandidatos("prefeito"))
        else:
          print("\nNúmero inválido, retornando para o menu")
          continuar = False
        
        #Perguntar se o usuário deseja continuar cadastrando candidatos
        continuar_op = input("\n***Candidato Cadastrado***\n\nDeseja continuar cadastrando candidatos? (Digite sim ou não): ").lower()
        if continuar_op == "não" or continuar_op == "nao":
          continuar = False
          print("\n***Retornando ao menu***")
        
    #Opção 2  
    elif op == 2:
      while continuar:
      
        #Adicionando as informações do eleitor
        eleitores.append(cadastroEleitor())
      
        #Perguntar se o usuário deseja continuar cadastrando eleitores
        continuar_op = input("\n***Eleitor Cadastrado***\n\nDeseja continuar cadastrando eleitores? (Digite sim ou não): ").lower()
        if continuar_op == "não" or continuar_op == "nao":
          continuar = False
          print("\n***Retornando ao menu***")
        
    #Opção 3
    else:

      #Criando condição
      encontrado = False
    
      #Verificando se o eleitor está cadastrado ou se já votou
      print("\n***Votar***\n\nVerifique se você está apto a votar.\nDigite seu nome e CPF:\n")
      nomeEleitor = input("Nome: ").lower()
      cpfEleitor = int(input("CPF: "))

      #Achando o eleitor na lista de eleitores
      for eleitor in range(len(eleitores)):
        if nomeEleitor == eleitores[eleitor][0] and cpfEleitor == eleitores[eleitor][1]:
          encontrado = True
          break
        else:
          encontrado = False
        
      #Se o eleitor for encontrado, prosseguir para a votação
      if encontrado:

        #Voto para prefeito
        while True:
          print("\n***Voto Prefeito***")
          votarPrefeito = votarCandidato(prefeito)
          
          #Se o usuário selecionar voto branco
          if votarPrefeito == "branco":
            print("\nVotar Branco selecionado")
            
            #Confirma se o usuário deseja mesmo votar no que selecionou
            if confirmar():

              #Adiciona o voto
              branco[0] += 1
              print("\nVoto Computado")
              
              #Encerra o laço
              break
            else:
              print("Digite Novamente")
              #Retorna para o início do laço, possibilitando que digite novamente outra opção
              
          #Se o usuário selecionar voto nulo
          elif votarPrefeito == "nulo":
            print("\nVotar Nulo selecionado")

            #Confirma se o usuário deseja mesmo votar no que selecionou
            if confirmar():

              #Adiciona o voto
              nulo[0] += 1
              print("\nVoto Computado.")

              #Encerra o laço
              break
            else:
              print("Digite Novamente.")
              #Retorna para o início do laço, possibilitando que digite novamente outra opção

          #Se o usuário selecionar um número de um candidato ou um número inválido
          else:

            #Confirma se o usuário deseja mesmo votar no que selecionou (caso o número seja válido)
            if confirmar():

              #Adiciona o voto ao candidato
              prefeito[votarPrefeito][0] += 1
              print("\nVoto computado.")

              #Encerra o laço
              break
            else:
              print("Digite Novamente")
              #Retorna para o início do laço, possibilitando que digite novamente outra opção

        #Voto para governador
        while True:
          print("\n***Voto Governador***")
          votarGovernador = votarCandidato(governador)
          if votarGovernador == "branco":
            print("\nVotar Branco selecionado")
            if confirmar():
              branco[1] += 1
              print("\nVoto Computado")
              break
            else:
              print("Digite Novamente")
          elif votarGovernador == "nulo":
            print("\nVotar Nulo selecionado")
            if confirmar():
              nulo[1] += 1
              print("\nVoto Computado.")
              break
            else:
              print("Digite Novamente.")
          else:
            if confirmar():
              governador[votarGovernador][0] += 1
              print("\nVoto Computado.")
              break
            else:
              print("Digite Novamente")

        #Voto para presidente
        while True:
          print("\n***Voto Presidente***")
          votarPresidente = votarCandidato(presidente)
          if votarPresidente == "branco":
            print("\nVotar Branco selecionado")
            if confirmar():
              branco[2] += 1
              print("\nVoto Computado")
              break
            else:
              print("Digite Novamente")
          elif votarPresidente == "nulo":
            print("\nVotar Nulo selecionado")
            if confirmar():
              nulo[2] += 1
              print("\nVoto Computado.")
              break
            else:
              print("Digite Novamente.")
          else:
            if confirmar():
              presidente[votarPresidente][0] += 1
              print("\nVoto Computado.")
              break
            else:
              print("Digite Novamente")
            
        #Após votar, adiciona o eleitor à lista de votantes e o deleta da lista de eleitores para que vote apenas uma vez
        votantes.append(eleitores[eleitor][0])
        del(eleitores[eleitor])
        print("\nObrigado por comparecer!")

      #Se o eleitor não for encontrado na lista, retorna ao menu
      else:
        print("\nVocê já votou ou seu cadastro não foi encontrado.\n\n***Retornando para o Menu***")
  #op > 4
  else:
    #Opção 4
    if op == 4:
      #Apuração de votos e criação das tabelas com o ranking para cada cargo
      apuracao(presidente, governador, prefeito)
      
    #Opcão 5
    elif op == 5:
      #Apresenta a lista de eleitores que votaram (votantes) e quais partidos elegeram mais e menos políticos 
      relatorio(votantes, partidos, Total)
      
    #Opção 6
    else:
      #Criação do arquivo apuracao.txt
      arquivo = open("apuracao.txt", "w")
      # Tabela para presidente
      arquivo.write('''***RANKING DO RESULTADO PARA PRESIDENTE***
      Nome\t\t\tPartido\t\tTotal de Votos\t\t%Votos Válidos\n''')
      t = 0
      for x in range(len(presidente)):
        por = "%"
        nome = rankingPresidente[x][2]
        partido = rankingPresidente[x][4]
        totalCandidato = rankingPresidente[x][0] + branco[2] + nulo[2]
        t += rankingPresidente[x][0]
        totalVotos = len(votantes)
        votosValidos = rankingPresidente[x][0] * 100 / totalCandidato
        arquivo.write(f"{x + 1}. {nome:<11}{partido:<6}{totalCandidato:<13d}{votosValidos:>22.2f}\n")
      porcentagemValidos = (t * 100) / totalVotos
      arquivo.write(f"Total de votos: {totalVotos}\n")
      arquivo.write(f"Total de votos válidos e % = {t:<2.0f}{porcentagemValidos:>7.2f}{por}\n")
      totalBranco = branco[2]
      porcentagemBranco = (totalBranco * 100) / totalVotos
      arquivo.write(f"Total de votos brancos e % = {totalBranco:<2.0f}{porcentagemBranco:>7.2f}{por}\n")
      totalNulo = nulo[2]
      porcentagemNulo = (totalNulo * 100) / totalVotos
      arquivo.write(f"Total de votos nulos e % = {totalNulo:<2.0f}{porcentagemNulo:>7.2f}{por}\n")
      Total.append(t)

      # Tabela para governador
      arquivo.write('''\n***RANKING DO RESULTADO PARA GOVERNADOR***
      Nome\t\t\tPartido\t\tTotal de Votos\t\t%Votos Válidos\n''')
      t = 0
      for x in range(len(governador)):
        por = "%"
        nome = rankingGovernador[x][2]
        partido = rankingGovernador[x][4]
        totalCandidato = rankingGovernador[x][0] + branco[1] + nulo[1]
        t += rankingGovernador[x][0]
        totalVotos = len(votantes)
        votosValidos = rankingGovernador[x][0] * 100 / totalCandidato
        arquivo.write(f"{x + 1}. {nome:<11}{partido:<6}{totalCandidato:<13d}{votosValidos:>22.2f}\n")
      porcentagemValidos = (t * 100) / totalVotos
      arquivo.write(f"Total de votos: {totalVotos}\n")
      arquivo.write(f"Total de votos válidos e % = {t:<2.0f}{porcentagemValidos:>7.2f}{por}\n")
      totalBranco = branco[1]
      porcentagemBranco = (totalBranco * 100) / totalVotos
      arquivo.write(f"Total de votos brancos e % = {totalBranco:<2.0f}{porcentagemBranco:>7.2f}{por}\n")
      totalNulo = nulo[1]
      porcentagemNulo = (totalNulo * 100) / totalVotos
      arquivo.write(f"Total de votos nulos e % = {totalNulo:<2.0f}{porcentagemNulo:>7.2f}{por}\n")
      Total.append(t)
    
      # Tabela para prefeito
      arquivo.write('''\n***RANKING DO RESULTADO PARA PREFEITO***
      Nome\t\t\tPartido\t\tTotal de Votos\t\t%Votos Válidos\n''')
      t = 0
      for x in range(len(prefeito)):
        por = "%"
        nome = rankingPrefeito[x][2]
        partido = rankingPrefeito[x][4]
        totalCandidato = rankingPrefeito[x][0] + branco[0] + nulo[0]
        t += rankingPrefeito[x][0]
        totalVotos = len(votantes)
        votosValidos = rankingPrefeito[x][0] * 100 / totalCandidato
        arquivo.write(f"{x + 1}. {nome:<11}{partido:<6}{totalCandidato:<13d}{votosValidos:>22.2f}\n")
      porcentagemValidos = (t * 100) / totalVotos
      arquivo.write(f"Total de votos: {totalVotos}\n")
      arquivo.write(f"Total de votos válidos e % = {t:<2.0f}{porcentagemValidos:>7.2f}{por}\n")
      totalBranco = branco[0]
      porcentagemBranco = (totalBranco * 100) / totalVotos
      arquivo.write(f"Total de votos brancos e % = {totalBranco:<2.0f}{porcentagemBranco:>7.2f}{por}\n")
      totalNulo = nulo[0]
      porcentagemNulo = (totalNulo * 100) / totalVotos
      arquivo.write(f"Total de votos nulos e % = {totalNulo:<2.0f}{porcentagemNulo:>7.2f}{por}\n")
      Total.append(t)
      arquivo.close()