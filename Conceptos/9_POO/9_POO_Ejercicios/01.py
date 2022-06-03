 Nueva_linea_Peligro = []

            #ataque 
            Ubicacion_Todas_fichas_Arriba= []
            Ubicacion_Todas_fichas_Abajo= []
            #ataques de las fichas de arriba 
            Todos_Los_posiblesAtaques_Arriba = []
            #ataque de las fichas de ababjp
            Todos_Los_posiblesAtaques_Abajo = []
            

            #buscará las fichas 
            for i in range(len(M)):
                for j in range(len(M[i])):
                    if M[i][j] in Colorde_ficha:
                        Ubicacion_Todas_fichas_Arriba.append([i,j])
                    if M[i][j] in Colorde_ficha2:
                        Ubicacion_Todas_fichas_Abajo.append([i,j])

            # print("Ubicacion de las fichas De Arriba arriba")
            # print(Ubicacion_Todas_fichas_Arriba)
            # print("Ubicacion de las fichas De abajo")
            # print(Ubicacion_Todas_fichas_Abajo)


            #este es un clico que va recorreindo todas las posiciones de las fichas de arriba 
            #fichas de arriba 
            def Algorimit_maximous(Color_variable,Color_Opuesto,Ubicacion,Ataques,Operador_positivo,Operador_negativo):
                for a in range(len(Ubicacion)):

                    # si son peones......
                    if M[ Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[0]:
                        # print(M[ Ubicacion_Todas_fichas_Arriba[a][0]][Ubicacion_Todas_fichas_Arriba[a][1]])
                        #derecha 
                        if  M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_negativo] in Color_Opuesto or M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_negativo] == ".":
                            Ataques.append([ Ubicacion[a][0]+Operador_positivo,Ubicacion[a][1]+Operador_negativo])
                        #isquierda
                        if  M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_positivo] in Color_Opuesto or M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_positivo] == ".":
                            Ataques.append([ Ubicacion[a][0]+Operador_positivo,Ubicacion[a][1]+Operador_positivo])
                    
                    # ##########################################################################################################################################
                    #si es un rey 
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[4]:
                        #arriba
                        def Algoritmo_deciciones_rey(Diagonal,Vertical):
                            if M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] in Color_Opuesto or M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] == ".":
                                Ataques.append([Ubicacion[a][0]+Diagonal,Ubicacion[a][1]+Vertical])
                        #arriba                                              #abajo                                #Derecha                                       isquierda                                     #arriba Derecha                                                 #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_deciciones_rey(Operador_positivo,0),Algoritmo_deciciones_rey(Operador_negativo,0),Algoritmo_deciciones_rey(0,Operador_positivo),Algoritmo_deciciones_rey(0,Operador_negativo),Algoritmo_deciciones_rey(Operador_positivo,Operador_positivo),Algoritmo_deciciones_rey(Operador_positivo,Operador_negativo), Algoritmo_deciciones_rey(Operador_negativo,Operador_positivo),Algoritmo_deciciones_rey(Operador_negativo,Operador_negativo)
                        
                    # ##########################################################################################################################################
                    ## ******************************************************************************************************************************************
                    #si es una reina
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[2]:
                        def Algoritmo_Deciciones_Reina(Diagonal,Vertical):
                            Fila_mas = Diagonal
                            Columna_mas = Vertical
                            while True:
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_Opuesto or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == ".":
                                    Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_variable or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] != ".":
                                    break
                                
                                if not Fila_mas == 0:
                                    if Diagonal == +1:
                                        Fila_mas = Fila_mas + 1
                                    if Diagonal == - 1:
                                        Fila_mas = Fila_mas - 1

                                if not Columna_mas == 0:
                                    if Vertical == -1:
                                        Columna_mas = Columna_mas - 1
                                    if Vertical == +1:
                                        Columna_mas = Columna_mas + 1

                        #arriba                                         #abajo                                          #Derecha                                       isquierda                                     #arriba Derecha                                                 #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Reina(Operador_positivo,0),Algoritmo_Deciciones_Reina(Operador_negativo,0),Algoritmo_Deciciones_Reina(0,Operador_positivo),Algoritmo_Deciciones_Reina(0,Operador_negativo),Algoritmo_Deciciones_Reina(Operador_positivo,Operador_positivo),Algoritmo_Deciciones_Reina(Operador_positivo,Operador_negativo), Algoritmo_Deciciones_Reina(Operador_negativo,Operador_positivo),Algoritmo_Deciciones_Reina(Operador_negativo,Operador_negativo)

                    # ******************************************************************************************************************************************
                    ## ******************************************************************************************************************************************
                    #si es un arfil 
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[5]:
                        def Algoritmo_Deciciones_Arfil(Diagonal,Vertical):
                            Fila_mas = Diagonal
                            Columna_mas = Vertical
                            while True:
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_Opuesto or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == ".":
                                    Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_variable or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] != ".":
                                    break
                                
                                if not Fila_mas == 0:
                                    if Diagonal == +1:
                                        Fila_mas = Fila_mas + 1
                                    if Diagonal == - 1:
                                        Fila_mas = Fila_mas - 1

                                if not Columna_mas == 0:
                                    if Vertical == -1:
                                        Columna_mas = Columna_mas - 1
                                    if Vertical == +1:
                                        Columna_mas = Columna_mas + 1

                        #arriba Derecha                                                  #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Arfil(Operador_positivo,Operador_positivo),Algoritmo_Deciciones_Arfil(Operador_positivo,Operador_negativo), Algoritmo_Deciciones_Arfil(Operador_negativo,Operador_positivo),Algoritmo_Deciciones_Arfil(Operador_negativo,Operador_negativo)
                    
                    # ******************************************************************************************************************************************
                    # Si es una torre
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[1]:
                        def Algoritmo_Deciciones_Torre(Diagonal,Vertical):
                            Fila_mas = Diagonal
                            Columna_mas = Vertical
                            while True:
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_Opuesto or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == ".":
                                    Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_variable or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] != ".":
                                    break
                                
                                if not Fila_mas == 0:
                                    if Diagonal == +1:
                                        Fila_mas = Fila_mas + 1
                                    if Diagonal == - 1:
                                        Fila_mas = Fila_mas - 1

                                if not Columna_mas == 0:
                                    if Vertical == -1:
                                        Columna_mas = Columna_mas - 1
                                    if Vertical == +1:
                                        Columna_mas = Columna_mas + 1

                        #arriba                                         #abajo                                          #Derecha                                        #isquierda                                    
                        Algoritmo_Deciciones_Torre(Operador_positivo,0),Algoritmo_Deciciones_Torre(Operador_negativo,0),Algoritmo_Deciciones_Torre(0,Operador_positivo),Algoritmo_Deciciones_Torre(0,Operador_negativo)

                    # ####################################################################################################################################################
                    #sie es un caballo 
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[3]:
                        def Algoritmo_Deciciones_Caballo(Diagonal,Vertical):
                            if M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] in Color_Opuesto or M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] == ".":
                                Ataques.append([Ubicacion[a][0]+Diagonal,Ubicacion[a][1]+Vertical])
                            
                        # L arriba Derecha                                                                                                                                           #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Caballo(Operador_negativo + Operador_negativo,Operador_positivo)
                        # L arriba isquierda
                        Algoritmo_Deciciones_Caballo(Operador_negativo + Operador_negativo,Operador_negativo)
                        # L Derecha arriba 
                        Algoritmo_Deciciones_Caballo(Operador_negativo,Operador_positivo + Operador_positivo)
                        # L Derecha Abajo 
                        Algoritmo_Deciciones_Caballo(Operador_positivo,Operador_positivo + Operador_positivo)
                        # L Isquierda Arriba
                        Algoritmo_Deciciones_Caballo(Operador_negativo,Operador_negativo + Operador_negativo)
                        # L Isquierda Abajo 
                        Algoritmo_Deciciones_Caballo(Operador_positivo,Operador_negativo + Operador_negativo)
                        # L Abajo Derecha                        
                        Algoritmo_Deciciones_Caballo(Operador_positivo + Operador_positivo,Operador_positivo)
                        # L Abajo isquierda
                        Algoritmo_Deciciones_Caballo(Operador_positivo + Operador_positivo,Operador_negativo)
                    
                        
 



            #Las fichas de arriba 
            Algorimit_maximous(Color_Variable2,Color_Variable1,Ubicacion_Todas_fichas_Arriba,Todos_Los_posiblesAtaques_Arriba,+1,-1)
            #las fuchas de abajo
            Algorimit_maximous(Color_Variable1,Color_Variable2,Ubicacion_Todas_fichas_Abajo,Todos_Los_posiblesAtaques_Abajo,-1,+1)
        

            # print("Estos son todos los ataques de las fichas De arriba ")
            # print(Todos_Los_posiblesAtaques_Arriba)
            
            # print("Estos son todos los ataques de las fichas De abajo ")
            # print(Todos_Los_posiblesAtaques_Abajo)
            
            Linea_del_ataque_hacia_el_rey = []
            Las_fichas_que_estan_atacando_al_rey = []

            for a in range(len(Ubicacion_Todas_fichas_Abajo)):
                if M[Ubicacion_Todas_fichas_Abajo[a][0]][Ubicacion_Todas_fichas_Abajo[a][1]] == Color_Variable1[4]:
                    POSICION = [Ubicacion_Todas_fichas_Abajo[a][0],Ubicacion_Todas_fichas_Abajo[a][1]] 
                    if POSICION in Todos_Los_posiblesAtaques_Arriba:
                        print("El REY ESTA EN HAKE POR LA FICHA")
                        

                        def Alagoritmo_logaritmatico_del_cambio_haker(Atacante1,Atacante2,Atacante3,Atacante4,Diagonal1,Vertical1):
                            logaritmo_del_cambio = []
                            Fichas_ataque_Ralla = [Color_Variable2[Atacante1],Color_Variable2[Atacante2],Color_Variable2[Atacante3],Color_Variable2[Atacante4]]
                        
                            Iterador1 = Diagonal1
                            Iterador2 = Vertical1
                            while True:

                                
                                if M[POSICION[0]+Iterador1][POSICION[1]+Iterador2] == ".":
                                    logaritmo_del_cambio.append([POSICION[0]+Iterador1,POSICION[1]+Iterador2])

                                elif M[POSICION[0]+Iterador1][POSICION[1]+Iterador2] in Fichas_ataque_Ralla:
                                    logaritmo_del_cambio.append([POSICION[0]+Iterador1,POSICION[1]+Iterador2])
                                    Las_fichas_que_estan_atacando_al_rey.append(M[POSICION[0]+Iterador1][POSICION[1]+Iterador2])

                                    for logor in range(len(logaritmo_del_cambio)):
                                        Linea_del_ataque_hacia_el_rey.append(logaritmo_del_cambio[logor])
                                    break
                                elif M[POSICION[0]+Iterador1][POSICION[1]+Iterador2] in Color_Variable2:
                                    break
                                else:
                                    break
                                
                                if not Diagonal1 == 0:
                                    if Diagonal1 == +1:
                                        Iterador1 = Iterador1 + 1
                                    if Diagonal1 == - 1:
                                        Iterador1 = Iterador1 - 1

                                if not Vertical1 == 0:
                                    if Vertical1 == -1:
                                        Iterador2 = Iterador2 - 1
                                    if Vertical1 == +1:
                                        Iterador2 = Iterador2+ 1

                            
                            print(Las_fichas_que_estan_atacando_al_rey)
                            
                        # Arriba 
                        Alagoritmo_logaritmatico_del_cambio_haker(1,2,1,1,-1,0)
                        # Arriba derecha
                        Alagoritmo_logaritmatico_del_cambio_haker(2,2,2,5,-1,-1)
                        # Arriba Isuquierda
                        Alagoritmo_logaritmatico_del_cambio_haker(2,2,2,5,-1,+1)
                        # Derecha 
                        Alagoritmo_logaritmatico_del_cambio_haker(2,1,1,1,0,+1)
                        # Abajo 
                        Alagoritmo_logaritmatico_del_cambio_haker(2,1,1,1,0,-1)
                        #abajo derecha 
                        Alagoritmo_logaritmatico_del_cambio_haker(2,2,2,5,+1,+1)
                        #Abajo isquierda 
                        Alagoritmo_logaritmatico_del_cambio_haker(2,2,2,5,+1,-1)

                        
                        # is the jaque is of the kind is a peon
                        #the jaque is from a peon or a kind
                        
                        #the wachahca 
                        the_wachachaca = [Color_Variable2[0],Color_Variable2[4]]
                        # the wachachaca horse
                        the_wachachaca_horse = [Color_Variable2[3]]
                        #derecha 
                        if  M[POSICION[a][0]-1][POSICION[a][1]+1] in the_wachachaca :
                            Linea_del_ataque_hacia_el_rey.append([POSICION[a][0]-1,POSICION[a][1]+1])
                            Las_fichas_que_estan_atacando_al_rey.append(M[POSICION[a][0]-1][POSICION[a][1]+1])
                        #isquierda
                        if  M[POSICION[a][0]-1][POSICION[a][1]-1] in the_wachachaca :
                            Linea_del_ataque_hacia_el_rey.append([POSICION[a][0]-1,POSICION[a][1]-1])
                            Las_fichas_que_estan_atacando_al_rey.append(M[POSICION[a][0]-1][POSICION[a][1]-1])

                        # the jaque of a horse   
                        def Algoritmo_Deciciones_Caballo(Diagonal12,Vertical12):
                            if M[POSICION[a][0]+Diagonal12][POSICION[a][1]+Vertical12] in the_wachachaca_horse:

                                Linea_del_ataque_hacia_el_rey.append([POSICION[a][0]+Diagonal12,POSICION[a][1]+Vertical12])
                                Las_fichas_que_estan_atacando_al_rey.append(M[[POSICION[a][0]+Diagonal12][POSICION[a][1]+Vertical12]])
                            
                        # L arriba Derecha                                                                                                                         #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Caballo(-2,+1)
                        # L arriba isquierda
                        Algoritmo_Deciciones_Caballo(-2,-1)
                        # L Derecha arriba 
                        Algoritmo_Deciciones_Caballo(-1,+2)
                        # L Derecha Abajo 
                        Algoritmo_Deciciones_Caballo(+1,+2)
                        # L Isquierda Arriba
                        Algoritmo_Deciciones_Caballo(-1,-2)
                        # L Isquierda Abajo 
                        Algoritmo_Deciciones_Caballo(+1,-2)
                        # L Abajo Derecha                        
                        Algoritmo_Deciciones_Caballo(+2,+1)
                        # L Abajo isquierda
                        Algoritmo_Deciciones_Caballo(+2,-1)
                    
                        



                        print("Esta es la linea que está atacando al rey ")
                        print(Linea_del_ataque_hacia_el_rey)
