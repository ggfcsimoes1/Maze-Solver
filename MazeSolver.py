#Gustavo Simoes numero 95588


def eh_labirinto(maze):
 '''
 ARGUMENTO: LABIRINTO
 ----------------------------------------------------------------------------------------------
 Funcao que recebe um argumento e averigua se pode ser ou nao labirinto. Para ser labirinto, 
 tem de ser um tuplo de tuplos com igual dimensao, que se se encontra rodeado de paredes 
 lateralmente, superiormente e inferiormente.
 ----------------------------------------------------------------------------------------------
 '''
  
  
 if type(maze) == tuple:
  if len(maze) < 3:
   return False
  for coluna in maze:
   if type(coluna) is not tuple or coluna == () or len(coluna) < 3 or len(coluna) != len(maze[0]):
    return False
  
   for i_linha_inicial in maze[0]:
    if i_linha_inicial != 1:
     return False
   for i_linha_final in maze[len(maze)-1]:
    if i_linha_final != 1:
     return False
   for indice_l in coluna:
    if type(indice_l) is not int or coluna[0] != 1 or coluna[-1] != 1:
     return False
  return True
 return False 

#eh_posicao((1,-2))
#eh_posicao((1,1,2))
#eh_posicao((1,1))

def eh_posicao(pos):
  
 '''
 ARGUMENTO: POSICAO
 ----------------------------------------------------------------------------------------------
 Recebe um argumento e averigua se este corresponde a uma posicao valida ou nao. Para ser uma 
 posicao valida, esta tem de ser um tuplo com numeros inteiros nao negativos e com um numero de 
 elementos maior que 2.
 ----------------------------------------------------------------------------------------------
 '''
 
 if type(pos) is not tuple:
   return False  
 elif not len(pos) == 2:
   return False
 else:    
   for i in pos:    
     if type(i) is not int or i < 0:
       return False  

   return True


def eh_conj_posicoes(conj_pos,):
 ''''
 ARGUMENTO: CONJUNTO DE POSICOES
 ----------------------------------------------------------------------------------------------
 Recebe um tuplo com um conjunto de posicoes e averigua se sao validas ou nao. Para ser valida, 
 as posicoes tem de ser tuplos com 0 ou mais posicoes nao repetidas.
 ----------------------------------------------------------------------------------------------
 '''
 if type(conj_pos) is not tuple:
  return False
 else:
  for i in range(len(conj_pos)):
   if not eh_posicao(conj_pos[i]):    #Se nenhum dos tuplos e posicao, devolve false, caso contrario, ira devolver true
    return False
  if len(conj_pos) != len(set(conj_pos)):        
    return False   
  return True
           
  
def tamanho_labirinto(maze):
 '''
 ARGUMENTOS: LABIRINTO
 ----------------------------------------------------------------------------------------------
 Retorna o tamanho de um labirinto no formato (x,y) , dado que este e valido. Caso contrario, 
 gera uma mensagem de erro.
 ----------------------------------------------------------------------------------------------
 ''' 
 
 
 if not eh_labirinto(maze):
  raise ValueError('tamanho_labirinto: argumento invalido')
 
 else:
  return (len(maze),len(maze[0])) 
 
      
def eh_mapa_valido(maze, conj_pos): 
 '''
 ARGUMENTOS: LABIRINTO, CONJUNTO DE POSICOES
 ----------------------------------------------------------------------------------------------
 Esta funcao recebe um labirinto e um conjunto de posicoes e averigua se este conjunto de 
 posicoes, sendo um argumento valido (tuplo, inteiro), se encontra dentro do labirinto definido 
 inicialmente, devolvendo o predicado 'True' no caso afirmativo e 'False' no caso negativo.
 ----------------------------------------------------------------------------------------------
 '''
 
 if not eh_conj_posicoes(conj_pos) or not eh_labirinto(maze):
   raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')
 
 else:
   
   for j in range(len(conj_pos)):                                      #Indice j corresponde ao eixo dos xx
           
    if conj_pos[j][1] not in range(1,tamanho_labirinto(maze)[1]-1):    #Se a posicao ultrapassa o labirinto no eixo dos yy
      return False
    elif conj_pos[j][0] not in range(1,tamanho_labirinto(maze)[0]-1):  #Se a posicao ultrapassa o labirinto no eixo dos xx
      return False       
    if maze[conj_pos[j][0]][conj_pos[j][1]] == 1:                      #Se a posicao no labirinto colide com uma parede...
      return False   
   
   return True
    
  
def eh_posicao_livre(maze, unidades, pos):
 '''
 ARGUMENTOS: LABIRINTO, UNIDADES PERTENCENTES AO LABIRINTO, POSICAO
 ----------------------------------------------------------------------------------------------
 Esta funcao recebe um labirinto, um conjunto de unidades e uma posicao, averiguando se esta se
 encontra dentro do labirinto e nao coincide com paredes nem outras unidades.
 ----------------------------------------------------------------------------------------------
 '''

 if eh_labirinto(maze) is False or eh_conj_posicoes(unidades) is False or eh_posicao(pos) is False: 
  raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
 
 elif eh_mapa_valido(maze, unidades,) is False:
  raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
 
 elif eh_mapa_valido(maze, (pos,)) is False: 
  return False
 
 else:
  
  for i in range(len(unidades)):
   if unidades[i] == pos:
    return False
  for j in range(len(pos)):
   if maze[pos[0]][pos[1]] == 1:        #Se a posicao no labirinto colide com uma parede...
    return False
  
 return True
      
def posicoes_adjacentes(pos):
 '''
 ARGUMENTO: POSICAO
 ----------------------------------------------------------------------------------------------
 Esta funcao recebe uma posicao (valida) e devolve o valor das suas posicoes adjacentes 
 por ordem de leitura do labirinto.
 ----------------------------------------------------------------------------------------------
 ''' 
 
 if eh_posicao(pos) is False:
  raise ValueError('posicoes_adjacentes: argumento invalido')
 
 else:
  
  list_adj = [(pos[0], pos[1]-1) , (pos[0]-1 , pos[1]) , (pos[0]+1 , pos[1]) , (pos[0], pos[1]+1)]
  i=len(list_adj)-1 
  
  while i >= 0:
   for j in range(0, len(pos)):          #Vai percorrer as posicoes da lista adjacente e ver se alguma se encontra fora do labirinto
     if list_adj[i][j] < 0:
      del list_adj[i]
     i=i-1 
     
  return tuple(list_adj)
 
def mapa_str(maze, unidades):
 '''
 ARGUMENTOS: LABIRINTO, CONJUNTO DE POSICOES (UNIDADES)
 ----------------------------------------------------------------------------------------------
 Esta funcao recebe um labirinto e um conjunto de posicoes correspondente as unidades presentes 
 no labirinto e devolve uma cadeia de caracteres que corresponde a sua representacao.
 ----------------------------------------------------------------------------------------------
 '''  
 if eh_conj_posicoes(unidades) is False:
  raise ValueError('mapa_str: algum dos argumentos e invalido')
 if eh_mapa_valido(maze, unidades) is False:
  raise ValueError('mapa_str: algum dos argumentos e invalido')
 
 else:
  novomapa = []     #Optei por interpretar um maze como sendo uma matriz, fazendo a sua transposta de modo a depois poder dar print em extenso da mesma
  novomapat = []    #Lista contendo o novo mapa constituido pela transposta da matriz original
  mapaprint= []
  novounidades = [] #Lista contendo as unidades a inserir dentro do labirinto
  mapafinal = ''
  for i in range(len(maze)):
   novomapa += [list((maze)[i])]              #Transformo maze em lista para poder alterar os seus conteudos
   
  for j in range(len(unidades)):
   novounidades += [list((unidades)[j])]      #Aplico o mesmo raciocinio para as unidades presentes dentro do labirinto
   
  for k in range(len(novounidades)):
   novomapa[novounidades[k][0]][novounidades[k][1]] = 2    #Coloco as unidades no labirinto com o numero 2 para mais tarde substituir
   
  for m in range(len(novomapa[0])):
   
   for l in range(len(novomapa)):        #Transposicao da matriz
    novomapat += [novomapa[l][m]]
   novomapat += ['\n']
  
  for n in range(len(novomapat)):
   
   if novomapat[n] == 1:
    mapaprint += ['#']
   elif novomapat[n] == 0:
    mapaprint += ['.']
   elif novomapat[n] == 2:
    mapaprint += ['O']
   else:
    mapaprint += ['\n']                  #Atribuicao dos caracteres aos numeros
  #print(mapaprint)
  for o in range(len(mapaprint)):
   mapafinal += mapaprint[o]
   
  return(mapafinal[:-1])                 #Corto o ultimo caracter da str de modo a nao imprimir o ultimo newline
 
 
 
def obter_objetivos(maze, unidades, pos):
 '''
 ARGUMENTOS: LABIRINTO, CONJUNTO DE POSICOES (UNIDADES), E UMA POSICAO
 ----------------------------------------------------------------------------------------------
 Esta funcao obtem os objetivos respetivos da posicao dada. Estes objetivos sao as posicoes 
 adjacentes validas dessa posicao.
 ----------------------------------------------------------------------------------------------
 '''   
 adj_obj = () #Criacao de uma lista intermedia que armazena posicoes que serao filtradas mais tarde
 obj_final = () #Lista com o objetivo final
 try:
  if pos not in unidades or eh_labirinto(maze) is False or eh_posicao(pos) is False or eh_conj_posicoes(unidades) is False:
   raise ValueError('obter_objetivos: algum dos argumentos e invalido')
  else:
   for i in range(len(unidades)):
    if pos != unidades[i]:
     adj_obj += (posicoes_adjacentes(unidades[i]))
   
   for j in range(len(adj_obj)):
    
    if eh_posicao_livre(maze, unidades, adj_obj[j]) is True: #Eliminacao das posicoes adjacentes que nao sao validas
     obj_final += (adj_obj[j]),
     
   return tuple(set(obj_final))    
 except ValueError:
  raise ValueError('obter_objetivos: algum dos argumentos e invalido')
  
def obter_caminho(maze, unidades, pos):
 '''
 ARGUMENTOS: LABIRINTO, CONJUNTO DE POSICOES (UNIDADES), E UMA POSICAO
 ----------------------------------------------------------------------------------------------
 Esta funcao, atraves do algoritmo BFS, devolve um tuplo com tuplos correspondentes as posicoes
 que correspondem ao menor numero de passos possiveis ate ao objetivo dado.
 ----------------------------------------------------------------------------------------------
 '''  
 if not eh_labirinto(maze) or not eh_conj_posicoes(unidades) or not eh_posicao(pos) or pos not in unidades:
  raise ValueError('obter_caminho: algum dos argumentos e invalido')
 elif not eh_mapa_valido(maze, unidades):
  raise ValueError('obter_caminho: algum dos argumentos e invalido')
 else:
  if unidades == tuple((pos,)) or len(unidades) < 2:
   return ()
  else:              
   for i in unidades:                      #Verifico se a minha posicao ja se encontra adjacente ao meu objetivo, parando o ciclo seja esse o caso.
    if i != pos:
     if pos in posicoes_adjacentes(i):
       return unidades                            
   fila_exp = []
   objetivo = obter_objetivos(maze, unidades, pos)
   pos_at = (pos)
   caminho_at = ()
   pos_visitadas = ()
   elm_fila_exp = tuple((pos_at,) + (caminho_at,),)
   fila_exp += [elm_fila_exp] 
   
   #---Aplicacao do algoritmo---
   
   while fila_exp != []:
    pos_at = fila_exp[0][0]
    caminho_at = fila_exp[0][1] 
    
    if pos_at not in pos_visitadas:
     pos_visitadas += (pos_at,)
     
     if pos_at in objetivo:
      return ((caminho_at)+(pos_at,))
     
     else:
      caminho_at += (pos_at,)
  
      if pos_at == ():
       return caminho_at
      
      for pos_adj_i in posicoes_adjacentes(pos_at):
       if eh_posicao_livre(maze, unidades, pos_adj_i) is True:
        elm_fila_exp = tuple((pos_adj_i,)+ (caminho_at,),)
        fila_exp += list((elm_fila_exp,))
        
    else: 
     fila_exp = fila_exp[1:]
     
   return ()     
  
def mover_unidade(maze, unidades, pos):
 '''
 ARGUMENTOS: LABIRINTO, CONJUNTO DE POSICOES (UNIDADES), E UMA POSICAO
 ----------------------------------------------------------------------------------------------
 Esta funcao devolve os valores que correspondem a movimentacao das unidades 1 vez.
 ----------------------------------------------------------------------------------------------
 '''   
 
 if pos not in unidades:
  raise ValueError('mover_unidade: algum dos argumentos e invalido')
 
 elif eh_labirinto(maze) is False or eh_conj_posicoes(unidades) is False or eh_posicao(pos) is False:
  raise ValueError('mover_unidade: algum dos argumentos e invalido')
 
 elif eh_mapa_valido(maze, unidades) is False: 
  raise ValueError('mover_unidade: algum dos argumentos e invalido')
 else:
  
  caminho = obter_caminho(maze, unidades, pos) 
  caminho = caminho[1:]   #Obtem do caminho correspondente a posicao dada e retira a posicao atual do mesmo.
  if caminho == ():
   return unidades

  unidades_novas = ()
  for i in unidades:
   if i != pos:
    if pos in obter_objetivos(maze,unidades,i):  
      return unidades                          
    else:
     for i in unidades:
       if i == pos:
        unidades_novas += (caminho[0],)             #Percorre 'unidades' e altera a posicao que foi dada como argumento da funcao
       else:
        unidades_novas += (i,)
        
     return unidades_novas 
       
    