# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import time
import random
import shutil
import os
from pathlib import Path
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from pygame import mixer, math  # Load the popular external library


##########################################################
# Available actions for the aplication
##########################################################
# 1 - Mensaje de bienvenida

# 1  - A little explanation about how the classification works-
#   - Explain the two options: trainnig and classification part itself

# 2 - Training :
#   - Explain the five types of metheor's sounds

# 4 - Classification
#   - Sound selector
#   - Give points ?
# levels :
# Level 1 : Metheor 1 (or 2 ) Vs 5
# Level 2 : 3 or for vs type 5
# Level 3 : 1 o 2 vs 3 4
# Level 4 :


########################################################################################################################
## 1 - BIENVENIDA
##----------------------------------------------------------------------------------------------------------------------

##......................................................
## Recoge el nombre del usuario
##......................................................

class ActionHelloWorld(Action):
    """
    ActionHelloWorld Recoge el nombre de usuario y ademas da un mensaje de bienvenida que se envia
    al modulo conversacional del Bot para
    """
    def name(self) -> Text:
        return "action_hola_mundo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        player_name = tracker.get_slot('name')
        dispatcher.utter_message(text="Bienvenid@ {}, si deseas  podemos aprender, entrenar o clasificar sonidos del cielo. ¿Qué te gustaría hacer?".format(player_name))


        return []

########################################################################################################################
## 2 - ENTRENAMIENTO
##----------------------------------------------------------------------------------------------------------------------

class ActionUnderdenseSelector(Action):
    """
    En esta clase se selecciona un sonido, y se devuelve la URI del recurso de este sonido
    asi de esta manera el Modulo ChatBot podra enviarselo al Front. Otra de las funcionalidades
    especiales de esta clase, es que retornara, mediante el tracker, el valor de uno de los Slots
    llamado 'sonido_actual', de esa manera, el bot sabra sobre de que tipo de sonido se esta conversando
    con el usuario. En este caso , se devuelve la informacion del sonido de tipo underdense
    """
    def name(self) -> Text:
        return "action_underdense_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      #  dispatcher.utter_message(text="El sonido que escucharas a continuacion es de un "
       #                                   "meteoro underdense")
        #absPath=os.path.abspath("sounds/sonidos_entrenamiento/meteor1_underdense.wav")
       # absPath="sounds/sonidos_entrenamiento/meteor1_underdense.wav"
       # dispatcher.utter_message(absPath)
        dispatcher.utter_message(json_message={"soundUri": 'sounds/sonidos_entrenamiento/meteor1_underdense.wav'})
        return [SlotSet("sonido_actual","1")]



#--------------------------------------------------------------------------------------------------

class ActionMSelector(Action):
    """
    En esta clase se selecciona un sonido, y se devuelve la URI del recurso de este sonido
    asi de esta manera el Modulo ChatBot podra enviarselo al Front. Otra de las funcionalidades
    especiales de esta clase, es que retornara, mediante el tracker, el valor de uno de los Slots
    llamado 'sonido_actual', de esa manera, el bot sabra sobre de que tipo de sonido se esta conversando
    con el usuario. En este caso , se devuelve la informacion del sonido de tipo M
    """
    def name(self) -> Text:
        return "action_m_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       #     dispatcher.utter_message(text="El sonido que escucharas a continuacion es de un "
        #                                  "meteoro M ")
           # absPath = os.path.abspath('sounds/sonidos_entrenamiento/meteor2_M.wav')
            absPath = 'sounds/sonidos_entrenamiento/meteor2_M.wav'

            #Cuando hemos encontrado el sonido, entonces devolvemos el path
            #dispatcher.utter_message(text=absPath)

            dispatcher.utter_message(json_message={"soundUri":'sounds/sonidos_entrenamiento/meteor2_M.wav'})
            #mixer.init()
            #mixer.music.load('sounds/sonidos_entrenamiento/meteor5_short overdense.wav')
            #mixer.music.play()
            return [SlotSet("sonido_actual","2")]

#--------------------------------------------------------------------------------------------------

class ActionLongOverdenseSelector(Action):
    """
    En esta clase se selecciona un sonido, y se devuelve la URI del recurso de este sonido
    asi de esta manera el Modulo ChatBot podra enviarselo al Front. Otra de las funcionalidades
    especiales de esta clase, es que retornara, mediante el tracker, el valor de uno de los Slots
    llamado 'sonido_actual', de esa manera, el bot sabra sobre de que tipo de sonido se esta conversando
    con el usuario. En este caso , se devuelve la informacion del sonido de tipo  long over sample
    """
    def name(self) -> Text:
        return "action_long_over_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       # dispatcher.utter_message(text="El sonido que escucharas a continuacion es de un "
       #                                   "meteoro overdense largo ")
        #absPath = os.path.abspath('sounds/sonidos_entrenamiento/meteor3_long_overdense.wav')
      #  absPath = 'sounds/sonidos_entrenamiento/meteor3_long_overdense.wav'
       # dispatcher.utter_message(text=absPath)
        dispatcher.utter_message(json_message={"soundUri":'sounds/sonidos_entrenamiento/meteor3_long_overdense.wav'})
        # mixer.init()
        # mixer.music.load('sounds/sonidos_entrenamiento/meteor5_short overdense.wav')
        # mixer.music.play()
        return [SlotSet("sonido_actual","3")]
#--------------------------------------------------------------------------------------------------


class ActionMediumOverdenseSelector(Action):
    """
    En esta clase se selecciona un sonido, y se devuelve la URI del recurso de este sonido
    asi de esta manera el Modulo ChatBot podra enviarselo al Front. Otra de las funcionalidades
    especiales de esta clase, es que retornara, mediante el tracker, el valor de uno de los Slots
    llamado 'sonido_actual', de esa manera, el bot sabra sobre de que tipo de sonido se esta conversando
    con el usuario. En este caso , se devuelve la informacion del sonido de tipo overdense medio
    """

    def name(self) -> Text:
        return "action_med_over_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      #  dispatcher.utter_message(text="El sonido que escucharas a continuacion es de un "
                                      #    "meteoro overdense medio")
       # absPath = os.path.abspath('sounds/sonidos_entrenamiento/meteor4_medium_overdense.wav')
        #absPath ='sounds/sonidos_entrenamiento/meteor4_medium_overdense.wav'
        dispatcher.utter_message(json_message={"soundUri":'sounds/sonidos_entrenamiento/meteor4_medium_overdense.wav'})
        #dispatcher.utter_message(text=absPath)
        return [SlotSet("sonido_actual","4")]

#--------------------------------------------------------------------------------------------------

class ActionShortOverdenseSelector(Action):
    """
    En esta clase se selecciona un sonido, y se devuelve la URI del recurso de este sonido
    asi de esta manera el Modulo ChatBot podra enviarselo al Front. Otra de las funcionalidades
    especiales de esta clase, es que retornara, mediante el tracker, el valor de uno de los Slots
    llamado 'sonido_actual', de esa manera, el bot sabra sobre de que tipo de sonido se esta conversando
    con el usuario. En este caso , se devuelve la informacion del sonido de tipo overdense corto
    """

    def name(self) -> Text:
        return "action_short_over_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(text="El sonido que escucharas a continuacion es de un "
         #                                 "meteoro overdense corto ")
       # absPath = os.path.abspath('sounds/sonidos_entrenamiento/meteor5_short overdense.wav')
       # absPath ='sounds/sonidos_entrenamiento/meteor5_short overdense.wav'
        dispatcher.utter_message(json_message= {"soundUri":'sounds/sonidos_entrenamiento/meteor5_short overdense.wav'})
    #    dispatcher.utter_message(text=absPath)

        return [SlotSet("sonido_actual","5")]
#--------------------------------------------------------------------------------------------------


########################################################################################################################
## 3 - CLASIFICACION
##----------------------------------------------------------------------------------------------------------------------

##......................................................
## Escogeun sonido, teniendo en cuenta ciertos parametros
## para enviarlos al usuario para su clasificacion
##......................................................

class ActionClassifying(Action):
    """
    Para el funcioamiento de esta clase, se hace un llamado a la clase soundListing
    la cual devolvera todos los sonidos y sus datos de clasificacion. 
    Cuando ya tenga los sonidos, esta clase analizara, quien tiene menos clasificaciones 
    asi podra escoger los sonidos mas nuevos para enviarselos al usuario mediante 
    el módulo conversacional
    """
    def name(self) -> Text:
        return "action_classifying"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Estoy escogiendo un sonido para ti...")

        sonidosAClasificar = SoundListing.make_SoundListing('sounds/classify_sounds','sounds/classify_sounds')
        #Buscamos el elemento que tenga 0 clasificaciones, si no existe cogemos cualquier de manera aleatorea
        try:
         soundIndex = sonidosAClasificar.counterClasificationList.index(0)
        except ValueError:
         soundIndex = random.choice(sonidosAClasificar.counterClasificationList)

        dispatcher.utter_message(text="Dime, ¿De que tipo crees que es el siguiente sonido ? ")

        dispatcher.utter_message(json_message= {"soundUri":sonidosAClasificar.soundsList[soundIndex]})
        #todo este le envia la uri del sonido, cuando el sonido esta en el bot  y despues en el frontal
        # el bot le tiene que preguntar ¿dime de que que tipo es el sonido? , si el niño le pide que le repita el
        # sonido, entonces se vuelve a enviar mendiante un slot. Ese slot llamado clasificando_sonido
        # tendra la uri que pondremos aqui, rellenandola desde aqui


        # tambien se puede hacer una clase en la que se busque quienes son los que mas clasifican, apareciendo de menor a mayot
        # en un listado

        return [SlotSet("txtclasificacionactual",sonidosAClasificar.listaDePathsDeArchivosTextoClass[soundIndex])]


#--------------------------------------------------------------------------------------------------

class ActionSaveClasificacion(Action):
    """
        todo tambien hay que hacer otra clase , una acccion que una vez que se el usuario haya dado una repsuesta
     que se rellene en un slot_respuesta, se ejecutara una accion en la que se extraera la respueta.
    dicha respuesta se almacenara, en el archivo de clasificaciones, se aumentara en uno el numero de clasificaciones
    del sonido en la lista (la primera linea ) yy junto con la clasificacion se podra el nombre.

        # todo ademas de ello se podria crear una clase que para que cuando el usuario pidiera el tipo de clasificacion
        # que se la ha ido dando, esta accion accediera al archivo e hiciera una media de todas las clasifiacaciones
        # para que asi hiciera una consulta de los datos (mejor hacer la mediana ...)

    """

    def name(self) -> Text:
        return "action_save_clasificacion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        player_resp = tracker.get_slot('respuesta')
        player_name = tracker.get_slot('name')
        uri_textoClasificacion= tracker.get_slot('txtclasificacionactual')

        #----------------------- GUARDANNDO RESP
        ##Aqui leemos tod el dfichero y lo pasamos a un array

        if int(player_resp) <= 5 and  int(player_resp) >= 1 :

            dispatcher.utter_message(text="El numero de clasificaciones esta siendo actualizado. ->"  + player_resp)

            with open(uri_textoClasificacion) as f:
                lines = f.readlines()
                # lines  # ['This is the first line.\n', 'This is the second line.\n']
            numClassi = int(lines[0])
            numClassi += 1
            lines[0] = str(numClassi)
            # lines  # ["This is the line that's replaced.\n", 'This is the second line.\n']
            f.close()

            with open(uri_textoClasificacion, "w") as f: # Escriebiendo el fichero otra vez ..
                f.writelines(lines)
            f.close()
            msg = str(numClassi)

            print("Num de clasificaciones VAL - ACT: " + msg  + "en  " + uri_textoClasificacion)
            dispatcher.utter_message(text="actualizado el num de clasificaciones  VAL - ACT : "+ msg + "en  " + uri_textoClasificacion)

            # ----------------------- AGREGAR CLASIFICACION (nombre de usuario y clasificacion)

            with open(uri_textoClasificacion, "w") as f:
                newClasificaction = player_resp+" "+player_name+"\n"
                f.write(newClasificaction)
            f.close()


            # ----------------------- INFORMACION SOBRE LA CLASIFICACION DE UN ARCHIVO
            acumulado = 0

            with open(pathsTxtSounfFileClasification) as f:  # Si existe solo lo abrimos en modo lectura
                first_line = f.readline().rstrip()  # Leemos la primera linea y ademas quitamos el salto de linea
                denominador = int(first_line)


                with open(uri_textoClasificacion) as f:
                    allLines = f.readlines()
                for linea in range(1, len(allLines)):
                    classificationPerUserX = allLines[linea][0] #El carcater de la  primera linea de cada clasificacion
                    acumulado = acumulado + int(classificationPerUserX) # los pasamos a int

                f.close()

                #----- CALCULAMOS LA MEDIA
                division_media = acumulado/denominador
                media = math.floor(int(division_media))

                dispatcher.utter_message(text=" INFO: Las clasificaciones anteriores dicen que este sonido podria ser de tipo " + media)
        else:
            dispatcher.utter_message(text= player_resp+ "no es una clasificacion valida")

            SlotSet("txtclasificacionactual"," ")
        return [SlotSet("sonido_actual","0")]


#--------------------------------------------------------------------------------------------------

class ActionGivmeStaticsSound(Action):
    """
    Esta clase calcula la media de las clasificaciones de un sonido
    hay que coger el numero de clasificaicones para sumar todas las clasificaciones posibles


    """

    def name(self) -> Text:
        return "action_giveme_statics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("sonido_actual","0")]


class SoundListing(object):
    """
    Esta clase sirve para poder listar los sonidos de un directorio
    Devuelve una lista con todos los sonidos (y sus localizaciones)
    y crea un archivo de texto en el path especificado, con la misma informacion
    asociados a cada sonido. Si un archivo de clasificacion, para un sonido dado, no
    existe, entonces lo crea.
    """
    soundsList = [] #Lista de sonidos (su localizacion), dento de un directorio
    counterClasificationList = [] # En cada posicion de esta lista se almacena la cantidad de veces que ha sido clasificado  cada sonido
    soundListFilePath = '' #Archivo txt, con los nombres, linea a linea, de todos los sonidos de un directorio
    listaDePathsDeArchivosTextoClass = [] #Aqui estan todos los path de todos los ficheros de texto asociado a las clasificaciones
    #Constructor de la lista de sonidos
    def __init__(self,path_origen,path_destino):

        listAux = []
        listadoNumClasificaciones = []
        listaDePathsDeArchivosTextoClassAux = []
        file_path = os.path.join(path_destino, "soundList.txt" )

        if not os.path.isdir(path_destino): #Si el directorio no existe, entonces se crea
            os.mkdir(path_destino)

        soundListFile = open(file_path, "w")

        # r=root, d=directories, f = files
        for r, d, f in os.walk(path_origen):
            for file in f:

             if '.wav' in file:
                 listAux.append(os.path.join(r, file)) ## Aqui metemos to do el path de cada archivo encontrado
                 soundFileName= Path(file).stem ## Obtiene el nombre de un fichero sin su extension
                 global pathsTxtSounfFileClasification
                 pathsTxtSounfFileClasification = os.path.join(path_destino,soundFileName+'.txt')

                 if not os.path.isfile(pathsTxtSounfFileClasification):
                     #Comprobamos en el path destino, si el ficher txt asociado a un sonido existe,
                     #Sino, lo creamos
                    txt =open (pathsTxtSounfFileClasification,"w")
                    print('creado el archivo: '+txt.name )
                    txt.write('0') #Escribimos un cero en la primera linea, asi se entiende que han habido 0 clasificaciones para ese sonido
                    listadoNumClasificaciones.append(0)
                    txt.close()
                    listaDePathsDeArchivosTextoClassAux.append(pathsTxtSounfFileClasification)  ## Aqui metemos to do el path de cada archivo encontrado
                    soundListFile.write(pathsTxtSounfFileClasification)  ## Escribe todos los nombres de todos los ficheros en un archivo en el path destino

                 else:
                     with open(pathsTxtSounfFileClasification) as f: # Si existe solo lo abrimos en modo lectura
                         first_line = f.readline().rstrip()   #Leemos la primera linea y ademas quitamos el salto de linea
                     listadoNumClasificaciones.append(first_line) #ahora ponemos lo que hay en la primera linea dentro de la lista de numero de clasificaciones
                     listaDePathsDeArchivosTextoClassAux.append(pathsTxtSounfFileClasification)  ## Aqui metemos to do el path de cada archivo encontrado
                     soundListFile.write(pathsTxtSounfFileClasification+"\n")  ## Escribe todos los nombres de todos los ficheros en un archivo en el path destino

        soundListFile.close()
        self.soundsList = listAux # aqui tenemos la lista de sonidos a ser usados para una session de juego
        self.counterClasificationList = list(map(int, listadoNumClasificaciones)) #Convertimos la lista a Int
        self.listaDePathsDeArchivosTextoClass=listaDePathsDeArchivosTextoClassAux
        self.soundListFilePath=file_path





    def make_SoundListing(path_origen,path_destino):
        soundListSession = SoundListing(path_origen,path_destino)
        return soundListSession

#--------------------------------------------------------------------------------------------------




####################################################################################################################
## Comprueba la respuesta con el sonido actual
####################################################################################################################




class ActionSoundCheck(Action):
    """
    Esta clase sirve para reproducir el sonido de un meteoro undersense.
    Dara una breve descripcion del sonido y lo reproducira
    """

    def name(self) -> Text:
        return "action_check_sound"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        player_resp = tracker.get_slot('respuesta')
        currently_sound= tracker.get_slot('sonido_actual')


        s_player = self.switch(int(player_resp))
        s_currently = self.switch(int(currently_sound))

        if player_resp == currently_sound:
            text="Muy bien! Has acertado el sonido es un meteoro tipo " + s_player
        elif player_resp == '':
            text = " Es una opcion incorrecta"
        else:
         text = "Oh! El sonido no es un " + s_player + ", este meteoro es de tipo: " + s_currently
        dispatcher.utter_message(text)
        return []


    def switch(self,case):
        sw = {
            1: 'underdense',
            2: 'm',
            3: 'overdense largo',
            4: 'overdense medio',
            5: 'overdense corto'
        }
        return sw.get(case, 'Opcion incorrecta')










########################################################################################################################
## CLASES AUXILIARES
##----------------------------------------------------------------------------------------------------------------------
class ActionLearning(Action):
    """
    EN DESHUSO, EN CASO DE QUE EL BACK REPRODUZCA EL SONIDO
    Esta clase sirve para crear la Accion que sera iniciada por el Bot.
    Reproduce los sonidos del cielo y su significado para que el usuario pueda aprender
    """
    def name(self) -> Text:
        return "action_learning"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=" Aqui escucharas algunos del cielo, asi podras aprender")

        #Creamos un listado de sonidos para poder reproducirlos en cadena
        path_origen='sounds/sonidos_entrenamiento/'
        path_destino='sounds/sonidos_entrenamiento/'
        listaSonidos= SoundListing.make_SoundListing(path_origen,path_destino)

        mixer.init()
        """ Hay que hacer una pequeña descripcion de los sonidos antes 
        de poder reproducirlos, tambien hay que poner un retard de 2 
        segundos para poder dar tiempo a escucharlos bien """


        for sound in listaSonidos.soundsList:
            mixer.music.load('sounds/sonidos_asistente/Bleep.wav') #El pitido de cuando empieza a ahblar el bot
            mixer.music.play()

            # Se reproduce la descripcion
            dispatcher.utter_message(text="Este sonido es:" + sound)

            # Se reproduce el sonido
            mixer.music.load(path_origen+sound)
            mixer.music.play()
            time.sleep(1)

        return []


class ActionTraining(Action):

    def name(self) -> Text:
        return "action_training"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=" Hola, ya estamos entrenando  !")
        mixer.init()
       # mixer.music.load('Sounds/dontremove.mp3')
        mixer.music.load('sounds/sonidos_entrenamiento/meteor5_short overdense.wav')
        mixer.music.play()

        ## En este caso deberiamos saber como dirigir el flujo segun nuestro codigo aqui
        ## y hacer preguntas al usuario par apoder ir
        return []

#--------------------------------------------------------------------------------------------------