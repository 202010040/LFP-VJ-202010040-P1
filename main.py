class Gestor:
    def __init__(self):
        #DATOS NECESARIOS PARA QUE EL PROGRAMA CORRA BIEN
        self.letras = ['A','B','C','D','E','F','G','H','I','J'',K',"L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                       "a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.numeros = ['0','1','2','3','4','5','6','7','8','9']
        self.espacio = [' ']
        self.simbolos = ['\n',';','+','-','*','/']
        self.tokens = []
        self.afds = []
        self.errores = []
        self.iterador1 = 0
        self.iterador2 = 1
        self.fila = 1
        self.columna = 1
        self.leer_archivo()

    #LEE EL ARCHIVO Y LO CONVIERTE A STRING
    def leer_archivo(self):
        archivo = open (r"C:\Users\Compu Fire\Documents\LFP\PROYECTO 1\fuente.sc", 'r', encoding="utf8")
        contenido = self.arreglar(archivo.read())
        self.lector(contenido)

    #LEE EL STRING Y LO VUELVE TOKENS
    def lector(self, contenido):
        self.iterador1 = 0
        #BUCLE PRINCIPAL PARA IRLO RECORRIENDO
        while self.iterador1 <= (len(contenido)-1):
            #PREGUNTA SI ES COMENTARIO DE UNA SOLA LINEA O TAMBIEN PUEDE SER MULTILINEA
            if contenido[self.iterador1] == "/":
                self.AFDComenntario(contenido)
                self.ADFComentarioMultilinea(contenido)
            self.ADFString(contenido)
            self.ADFIntFloat(contenido)
            self.AFDChar(contenido)
            self.AFDBooleano(contenido)
            #Avanzar
            self._avanzar(contenido)

        self._reportar()
    
    def AFDBooleano(self,contenido):
        Diccionario = [

            #----------------------BOOLEANOS-----------------------
            {'Columna': 0,
            'Fila': 0,    #La fila y la columna se asignaran despues
            'Lexema': '', #El lexema quedara por definir
            'Token': 'Booleano_verdadero',
            'Patron': "True",
            'Estados': ''},#Por definir

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'Booleano_falso',
            'Patron': "False",
            'Estados': ''},

            #----------------------OPERADORES-----------------------
            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_suma',
            'Patron': "+",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_resta',
            'Patron': "-",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_multiplicacion',
            'Patron': "*",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_division',
            'Patron': "/",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_resto',
            'Patron': "%",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_igualacion',
            'Patron': "==",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_diferenciacion',
            'Patron': "!=",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_mayor',
            'Patron': ">",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_mayor_o_igual',
            'Patron': ">=",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_menor',
            'Patron': "<",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_menor_o_igual',
            'Patron': "<=",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_and',
            'Patron': "&&",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_or',
            'Patron': "||",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'operador_not',
            'Patron': "!",
            'Estados': ''},

            #----------------------TIPOS DE DATOS-----------------------

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'tipo_int',
            'Patron': "Int",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'tipo_double',
            'Patron': "Double",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'tipo_string',
            'Patron': "String",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'tipo_char',
            'Patron': "Char",
            'Estados': ''},

            {'Columna': 0,
            'Fila': 0,
            'Lexema': '', 
            'Token': 'tipo_booleano',
            'Patron': "Boolean",
            'Estados': ''},



        ]
        #Primero se ve que la palabra no este en otro caracter
        if ((contenido[self.iterador1 - 1 ]) not in self.letras) and ((contenido[self.iterador1 -1 ]) not in self.numeros):
            #Como son dos valores se haran dinamicamente
            for b in Diccionario:
                col = self.columna
                fila = self.fila
                #En cada token se buscaran las cadenas que coincidan
                Aceptado = 1 #Variable para ver si hay un estadoo de aceptacion
                s = 0
                lexe = ''
                estados0 = []
                for a in b['Patron'].upper():
                    if (self.iterador1<= (len(contenido)-1)):
                        if ((contenido[self.iterador1]).upper() == a.upper()) :#Case insensitive
                            #Se crea el estado
                            estado = {
                                'Estado' : 'S' + str(s),
                                'Caracter': contenido[self.iterador1],
                                'Lexema Reconocido': lexe,
                                'Siguiente estado':'S' + str(int(s)+1)
                            }
                            estados0.append(estado)
                            s += 1
                            lexe += contenido[self.iterador1]
                            self._avanzar(contenido)
                        else:
                            Aceptado = 0
                            break
                        #Si todo sale bien, entonces 
                        #Crea el estado de aceptacion
                        if (self.iterador1<len(contenido)):
                            if Aceptado == 1:
                                #Verificar si es el ultimo carcater, necesita un tratamiento especial
                                if (self.iterador1 == (len(contenido) -1)):
                                    #Ultimo estado antes del de aceptacion
                                    estado = {
                                            'Estado' : 'S' + str(s),
                                            'Caracter': contenido[self.iterador1],
                                            'Lexema Reconocido': lexe,
                                            'Siguiente estado':'S' + str(int(s)+1)
                                        }
                                    lexe += contenido[self.iterador1]
                                    estados0.append(estado)

                                    estadoA = {
                                            'Estado' : 'S' + str(s),
                                            'Caracter': '#',
                                            'Lexema Reconocido': lexe,
                                            'Siguiente estado':'S' + str(int(s)+2) + "(Aceptacion)"
                                        }
                                    lexe += contenido[self.iterador1]
                                    estados0.append(estadoA)
                                    #Crea el token para el reporte
                                    b['Columna'] = col
                                    b['Fila'] = fila
                                    b['Lexema'] = lexe
                                    b['Estados'] = estados0
                                    self.tokens.append(b)
                                    break
                                elif  (contenido[self.iterador1] in self.simbolos) or (contenido[self.iterador1] in self.espacio):
                                    #Ultimo estado antes del de aceptacion
                                    estadoA = {
                                            'Estado' : 'S' + str(s),
                                            'Caracter': '#',
                                            'Lexema Reconocido': lexe,
                                            'Siguiente estado':'S' + str(int(s)+1) + "(Aceptacion)"
                                        }
                                    lexe += contenido[self.iterador1]
                                    estados0.append(estadoA)
                                    #Crea el token para el reporte
                                    b['Columna'] = col
                                    b['Fila'] = fila
                                    b['Lexema'] = lexe
                                    b['Estados'] = estados0
                                    self.tokens.append(b)
                                    break






            
    #AUTOMATA DE CARACTERES
    def AFDChar(self, contenido):
        col = self.columna
        fila = self.fila
        estados =[]
        caracter = ''
        #Pregunta si esta entre comillas
        if contenido[self.iterador1] == '\'':
            s0 = {'Estado':'S0','Caracter':'\'', 'Lexema reconocido': '', 'Siguiente estado':'S1'}
            estados.append(s0)
            caracter += contenido[self.iterador1]
            s1 = {'Estado':'S1','Caracter':contenido[self.iterador1], 'Lexema reconocido': caracter, 'Siguiente estado':'S1'}
            estados.append(s1)
            self._avanzar(contenido)
            if (contenido[self.iterador1] in self.letras):
                caracter += contenido[self.iterador1]
                s1 = {'Estado':'S1','Caracter':contenido[self.iterador1], 'Lexema reconocido': caracter, 'Siguiente estado':'S1'}
                estados.append(s1)
                self._avanzar(contenido)
                if contenido[self.iterador1] == '\'':
                    caracter += contenido[self.iterador1]
                    s1 = {'Estado':'S1','Caracter':contenido[self.iterador1], 'Lexema reconocido': caracter, 'Siguiente estado':'S1'}
                    estados.append(s1)
                    s2 = {'Estado':'S2','Caracter':"#", 'Lexema reconocido': caracter, 'Siguiente estado':'S3(Aceptacion)'}
                    estados.append(s2)
                    #Luego de validar todo lo mete al reporte
                    lexema0 = {
                        'Lexema':caracter,
                        'Token':'dato_char',
                        'Estados': estados
                    }
                    self.afds.append(lexema0)
                    lexema1 = {
                        'Columna': col,
                        'Fila': fila,
                        'Lexema': caracter,
                        'Token': 'dato_char',
                        'Patron': "(')(a-zA-Z)(')",
                        'Estados': estados
                        }
                    self.tokens.append(lexema1)
                else:
                    error = {
                            'Linea': self.fila,
                            'Columna': self.columna,
                            'Lexema':contenido[self.iterador1]
                        }
                    self.errores.append(error)
   
    #AUTOMATA DE INTS Y FLOATS
    def ADFIntFloat (self,contenido):
        #Verifica que anteriormente solo hayan espacios
        #(((contenido[self.iterador1 - 1] in self.espacio) or (contenido[self.iterador1 - 1] in self.simbolos)) and
        if  ((contenido[self.iterador1] in self.numeros) and ((contenido[self.iterador1 - 1] in self.espacio) or (contenido[self.iterador1 - 1] in self.simbolos)) ):
            #Iterador de la cantidad de puntos que hay en un numero
            col = self.columna
            fila = self.fila
            puntos = 0
            numero = ''
            estados = []
            s0 = {'Estado':'S0','Caracter':contenido[self.iterador1], 'Lexema reconocido': '', 'Siguiente estado':'S1'}
            estados.append(s0)
            numero += contenido[self.iterador1]
            self._avanzar(contenido)
            #Ejecuta el bucle, mientras el indice sea menor al arreglo y mientras no haya un espacio
            while (self.iterador1 <= (len(contenido)-1)) and (contenido[self.iterador1] not in self.espacio) and (contenido[self.iterador1] not in self.simbolos):
                #Ahora verifica que hayan numeros
                if (contenido[self.iterador1] in self.numeros):
                    numero += contenido[self.iterador1]
                    s1 = {'Estado':'S1','Caracter':contenido[self.iterador1], 'Lexema reconocido': numero, 'Siguiente estado':'S1'}
                    estados.append(s1)
                #Verifica si hay un punto
                elif (contenido[self.iterador1] == '.'):
                    if puntos == 0:
                        puntos = 1
                        numero += contenido[self.iterador1]
                        s1 = {'Estado':'S1','Caracter':contenido[self.iterador1], 'Lexema reconocido': numero, 'Siguiente estado':'S1'}
                        estados.append(s1)
                    #Mas de un punto no puede haber
                    else:
                        error = {
                            'Linea': self.fila,
                            'Columna': self.columna,
                            'Lexema':contenido[self.iterador1]
                        }
                        self.errores.append(error)
                        return
                else:
                    error = {
                        'Linea': self.fila,
                        'Columna': self.columna,
                        'Lexema':contenido[self.iterador1]
                    }
                    self.errores.append(error)
                    return
                #Si es el utimo numero antes del espacio entonces se acepta
                if (contenido[self.iterador1] == ' '):
                    s1 = {'Estado':'S1','Caracter':contenido[self.iterador1 - 1], 'Lexema reconocido': numero, 'Siguiente estado':'S2'}
                    estados.append(s1)
                    s2 = {'Estado':'S2','Caracter':'#', 'Lexema reconocido': numero, 'Siguiente estado':'S3(Aceptacion)'}
                    estados.append(s2)
                self._avanzar(contenido)
            #Ahora pregunta si es float o int
            if puntos == 0:
                lexema0 = {
                        'Lexema':numero,
                        'Token':'dato_int',
                        'Estados': estados
                    }
                self.afds.append(lexema0)
                lexema1 = {
                    'Columna': col,
                    'Fila': fila,
                    'Lexema': numero,
                    'Token': 'dato_int',
                    'Patron': '([0-9])([0-9])*',
                    'Estados': estados
                    }
                self.tokens.append(lexema1)
            elif puntos == 1:
                lexema0 = {
                        'Lexema':numero,
                        'Token':'dato_double',
                        'Estados': estados
                    }
                self.afds.append(lexema0)
                lexema1 = {
                    'Columna': col,
                    'Fila': fila,
                    'Lexema': numero,
                    'Token': 'dato_double',
                    'Patron': '([0-9])([0-9])*(.)([0-9])([0-9])*',
                    'Estados': estados
                    }
                self.tokens.append(lexema1)
            
    #AUTOMATA DE STRINGS
    def ADFString (self, contenido):
        #Si hay comillas dobles al inicio entonces comienza a analizar
        if contenido[self.iterador1] == "\"":
            #Guarda estos datos para usarlos en las tablas
            col = self.columna
            fila = self.fila
            estados = []
            cadena = ""
            s0 = {'Estado':'S0','Caracter':'\"', 'Lexema reconocido': '', 'Siguiente estado':'S1'}
            estados.append(s0)
            cadena += contenido[self.iterador1]
            self._avanzar(contenido)
            #Ver si aun no se ha acabado la cadena
            while self.iterador1 <=(len(contenido)-1):
                #Si no se ha acabado va concatenando
                if (contenido[self.iterador1] != '\"'):
                    #Pregunta si son numeros o letras
                    if ((contenido[self.iterador1] in self.numeros) or (contenido[self.iterador1] in self.letras) or (contenido[self.iterador1] in self.espacio)):
                        cadena += contenido[self.iterador1]
                        s1 = {'Estado':'S1','Caracter':contenido[self.iterador1], 'Lexema reconocido': cadena, 'Siguiente estado':'S1'}
                        estados.append(s1)
                    #Si no, manda un error
                    else:
                        error = {
                            'Linea': self.fila,
                            'Columna': self.columna,
                            'Lexema':contenido[self.iterador1]
                        }
                        self.errores.append(error)
                    self._avanzar(contenido)
                elif (contenido[self.iterador1] == '\"'):
                    #Si se acabo solo concatena lo ultimo y ya
                    s2 = {'Estado':'S2','Caracter':contenido[self.iterador1], 'Lexema reconocido': cadena, 'Siguiente estado':'S2'}
                    cadena += contenido[self.iterador1]
                    s3 = {'Estado':'S2','Caracter':'#', 'Lexema reconocido': cadena, 'Siguiente estado':'S3(aceptacion)'}
                    estados.append(s2)
                    estados.append(s3)
                    #Manda a hacer el afd
                    lexema0 = {
                        'Lexema':cadena,
                        'Token':'dato_string',
                        'Estados': estados
                    }
                    self.afds.append(lexema0)
                    #Manda a hacer el token
                    lexema1 = {
                    'Columna': col,
                    'Fila': fila,
                    'Lexema': cadena,
                    'Token': 'dato_string',
                    'Patron': '(")([0-9]|[a-zA-Z])([0-9]|[a-zA-Z])*(")',
                    'Estados': estados
                    }
                    self.tokens.append(lexema1)
                    self._avanzar(contenido)
                    break

    #AUTOMATA DE COMENTARIO MULTILINEA
    def ADFComentarioMultilinea (self,contenido):
        estados= []
        comentario = ""
        col = self.columna
        fila = self.fila
        #Verificar que no este al fina; de la cadena 
        if self.iterador2 <= (len(contenido)-1):
            if contenido[self.iterador1] =="/" :
                #Crea estado para la tabla de estados
                s0 = {'Estado':'S0','Caracter':'/', 'Lexema reconocido': '', 'Siguiente estado':'S1'}
                estados.append(s0)
                if contenido[self.iterador2] == "*" :
                    #Reconociendo ambos se llaga a la conclusion de que es un comentario de una sola linea
                    s1 = {'Estado':'S1','Caracter':'*', 'Lexema reconocido': '/', 'Siguiente estado':'S2'}
                    s2 = {'Estado':'S2','Caracter':'#', 'Lexema reconocido': '/*', 'Siguiente estado':'S3 (Aceptacion)'}
                    estados.append(s1)
                    estados.append(s2)
                    lexema0 = {
                        'Lexema':'/*',
                        'Token':'comentario_multilinea_apertura',
                        'Estados': estados
                    }
                    #Avanza dos pasos y comienza con la iteracion del comentario
                    self.afds.append(lexema0)
                    self._avanzar(contenido)
                    self._avanzar(contenido)
                    while self.iterador2 <= (len(contenido)-1):
                        #Pregunta cuando cerrar el comentario
                        if (contenido[self.iterador1] == "*"):
                            #Cuando cierra el comentario se crea otro lexema
                            estadosB= []
                            s0B = {'Estado':'S0','Caracter':'*', 'Lexema reconocido': '', 'Siguiente estado':'S1'}
                            estadosB.append(s0B)
                            if (contenido[self.iterador2] == "/"):
                                #Como cierra el comentario, entonces se guarda el comentario
                                lexema1 = {
                                'Columna': col + 2,
                                'Fila': fila,
                                'Lexema': comentario,
                                'Token': 'comentario_multilinea',
                                'Patron': '([0-9]|[a-zA-Z]|[S])([0-9]|[a-zA-Z]|[S])*',
                                'Estados': estados
                                }
                                self.tokens.append(lexema1)
                                s1B = {'Estado':'S1','Caracter':'/', 'Lexema reconocido': '*', 'Siguiente estado':'S2'}
                                estadosB.append(s1B)
                                s2B = {'Estado':'S2','Caracter':'#', 'Lexema reconocido': '*/', 'Siguiente estado':'S3(Aceptacion)'}
                                estadosB.append(s2B)
                                #Agrega los estados al reporte
                                lexema0B = {
                                    'Lexema':'/*',
                                    'Token':'comentario_multilinea_cierre',
                                    'Estados': estadosB
                                }
                                self.afds.append(lexema0B)
                                self._avanzar(contenido)
                                self._avanzar(contenido)
                                break
                        else:
                            comentario += contenido[self.iterador1]
                            self._avanzar(contenido)

    #AUTOMATA DE COMENTARIO DE UNA SOLA LINEA
    def AFDComenntario(self, contenido):
        estados = []
        comentario = ""
        col = self.columna
        fila = self.fila
        #Verificar que no este al final de la cadena 
        if self.iterador2 <= (len(contenido)-1):
            #Ahora verifica si es un comentario de una sola linea
            if contenido[self.iterador1] =="/" :
                #Crea estado para la tabla de estados
                s0 = {'Estado':'S0','Caracter':'/', 'Lexema reconocido': '', 'Siguiente estado':'S1'}
                estados.append(s0)
                if contenido[self.iterador2] == "/" :
                    #Reconociendo ambos se llaga a la conclusion de que es un comentario de una sola linea
                    s1 = {'Estado':'S1','Caracter':'/', 'Lexema reconocido': '/', 'Siguiente estado':'S2'}
                    s2 = {'Estado':'S2','Caracter':'#', 'Lexema reconocido': '//', 'Siguiente estado':'S3 (Aceptacion)'}
                    estados.append(s1)
                    estados.append(s2)
                    #Agrega los estados al reporte
                    lexema0 = {
                        'Lexema':'//',
                        'Token':'comentario_linea_apertura',
                        'Estados': estados
                    }
                    self.afds.append(lexema0)
                    #AVANZAR
                    self._avanzar(contenido)
                    self._avanzar(contenido)
                    #Mientras exista una cadena
                    #Y mientras no haya salto de linea
                    while (self.iterador1 <= (len(contenido)-1))and (contenido[self.iterador1] != "\n"):
                        comentario += contenido[self.iterador1]
                        self._avanzar(contenido)
                    #Con el comentario listo, agrega los lexemas
                    lexema1 = {
                        'Columna':col,
                        'Fila': fila,
                        'Lexema': '//',
                        'Token': 'comentario_linea_apertura',
                        'Patron': '//'
                        }
                    lexema2 = {
                        'Columna': col + 2,
                        'Fila': fila,
                        'Lexema': comentario,
                        'Token': 'comentario_una_linea',
                        'Patron': '([0-9]|[a-zA-Z]|[S])([0-9]|[a-zA-Z]|[S])*',
                        'Estados': estados
                    }
                    #Agrega los lexemas a un listado
                    self.tokens.append(lexema1)
                    self.tokens.append(lexema2)

    #IMPRIMIR LISTADOS
    def  _reportar(self):
        print ("REPORTE DE TOKENS")
        for lexema in self.tokens:
            for estado in (lexema['Estados']):
                print(estado)
        for error in self.errores:
            print(error)
            
    #AVANZAR
    def _avanzar(self, contenido):
        #Verifica que no haya finalizado
        if self.iterador1 <= (len(contenido)-1):
            #Si hay un salto de linea resetea la columna
            if contenido[self.iterador1] == "\n":
                self.fila +=1
                self.columna = 1
                self.iterador2 += 1
                self.iterador1 +=1
            #Si no lo hay, simplemente avanza
            else:
                self.columna += 1
                self.iterador2 += 1
                self.iterador1 +=1

    #REEMPLAZA POR ACENTOS VALIDOS YA QUE PYTHON NO LOS SOPORTA NATIVAMENTE
    def arreglar(self, texto):
        reemplazos = (
        ('Á', 'A'),
        ('É', 'E'),
        ('Í', 'I'),
        ('Ó', 'O'),
        ('Ú', 'U'),
        ('Ã¡', 'a'),
        ('Ã©', 'e'),
        ('Ã\xad', 'i'),
        ('Ã³', 'o'),
        ('Ãº', 'u'),
        )
        for a,b in reemplazos:
            texto = texto.replace(a, b)
        return texto

gestor = Gestor()
#C:\Users\Compu Fire\Documents\LFP\PROYECTO 1\fuente.sc