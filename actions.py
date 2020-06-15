# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import time
import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
from pygame import mixer  # Load the popular external library


##########################################################
# Available actions for the aplication
##########################################################
# 1 - Mensaje de bienvenida

# 1  - A little explanation about how the classification works-
#   - Explain the two options: trainnig and classification part itself

# 3 - Training :
#   - Explain the five types of metheor's sounds

# 4 - Classification
#   - Sound selector
#   - Give points ?
# levels :
# Level 1 : Metheor 1 (or 2 ) Vs 5
# Level 2 : 3 or for vs type 5
# Level 3 : 1 o 2 vs 3 4
# Level 4 :


####################################################################################################################
# 1: Acciones que seleccionan sonidos que ya esta identificados
####################################################################################################################

class ActionUnderdenseSelector(Action):
    """
    Esta clase sirve para reproducir el sonido de un meteoro undersense.
    Dara una breve descripcion del sonido y lo reproducira
    """
    def name(self) -> Text:
        return "action_underdense_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      #  dispatcher.utter_message(text="El sonido que escucharas a continuacion es de un "
       #                                   "meteoro underdense")
        absPath=os.path.abspath("sounds/sonidos_entrenamiento/meteor1_underdense.wav")
        dispatcher.utter_message(absPath)

        return [SlotSet("sonido_actual","1")]



#--------------------------------------------------------------------------------------------------

class ActionMSelector(Action):
    """
    Esta clase sirve para reproducir el sonido de un meteoro M.
    Dara una breve descripcion del sonido y lo reproducira
    """
    def name(self) -> Text:
        return "action_m_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       #     dispatcher.utter_message(text="El sonido que escucharas a continuacion es de un "
        #                                  "meteoro M ")
            absPath = os.path.abspath('sounds/sonidos_entrenamiento/meteor2_M.wav')

            #Cuando hemos encontrado el sonido, entonces devolvemos el path
            dispatcher.utter_message(text=absPath)
            #mixer.init()
            #mixer.music.load('sounds/sonidos_entrenamiento/meteor5_short overdense.wav')
            #mixer.music.play()
            return [SlotSet("sonido_actual","2")]

#--------------------------------------------------------------------------------------------------

class ActionLongOverdenseSelector(Action):

    def name(self) -> Text:
        return "action_long_over_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       # dispatcher.utter_message(text="El sonido que escucharas a continuacion es de un "
       #                                   "meteoro overdense largo ")
        absPath = os.path.abspath('sounds/sonidos_entrenamiento/meteor3_long_overdense.wav')
        dispatcher.utter_message(text=absPath)

        # mixer.init()
        # mixer.music.load('sounds/sonidos_entrenamiento/meteor5_short overdense.wav')
        # mixer.music.play()
        return [SlotSet("sonido_actual","3")]
#--------------------------------------------------------------------------------------------------


class ActionMediumOverdenseSelector(Action):

    def name(self) -> Text:
        return "action_med_over_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      #  dispatcher.utter_message(text="El sonido que escucharas a continuacion es de un "
                                      #    "meteoro overdense medio")
        absPath = os.path.abspath('sounds/sonidos_entrenamiento/meteor4_medium_overdense.wav')
        dispatcher.utter_message(text=absPath)

        return [SlotSet("sonido_actual","4")]

#--------------------------------------------------------------------------------------------------

class ActionShortOverdenseSelector(Action):

    def name(self) -> Text:
        return "action_short_over_sample"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(text="El sonido que escucharas a continuacion es de un "
         #                                 "meteoro overdense corto ")
        absPath = os.path.abspath('sounds/sonidos_entrenamiento/meteor5_short overdense.wav')
        dispatcher.utter_message(text=absPath)

        return [SlotSet("sonido_actual","5")]
#--------------------------------------------------------------------------------------------------
##################################################################################





class SoundListing(object):
    """
    Esta clase sirve para poder listar los sonidos de un directorio
    Devuelve una lista con todos los sonidos (y sus localizaciones)
    y crea un archivo de texto en el path especificado, con la misma informacion
    """
    soundsList = []
    soundListFilePath = ''
    #Constructor de la lista de sonidos
    def __init__(self,path_origen,path_destino):
        list = []

        filename = "soundList.txt" #Este será el archivo que tiene los sonidos para una session
        file_path = os.path.join(path_destino, filename)
        if not os.path.isdir(path_destino): #Si el directorio no existe, entonces se crea
            os.mkdir(path_destino)
        soundFile = open(file_path, "w")

        # r=root, d=directories, f = files
        for r, d, f in os.walk(path_origen):
            for file in f:
                if '.wav' in file:
                    list.append(file)
                    soundFile.write(file+'\n')

        soundFile.close()
        self.soundsList = list # aqui tenemos la lista de sonidos a ser usados para una session de juego
        self.soundListFilePath=file_path

    def make_SoundListing(path_origen,path_destino):
        soundListSession = SoundListing(path_origen,path_destino)
        return soundListSession

#--------------------------------------------------------------------------------------------------
class ActionLearning(Action):
    """
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
#--------------------------------------------------------------------------------------------------





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

class ActionClassifying(Action):

    def name(self) -> Text:
        return "action_classifying"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ya estamos clasificando")
        print("FUCK THIS ")
        return []


####################################################################################################################
## Recoge el nombre del usuario
####################################################################################################################

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hola_mundo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        player_name = tracker.get_slot('name')
        dispatcher.utter_message(text="Bienvenido {} si deseas  podemos aprender, entrenar o clasificar sonidos del cielo. ¿Qué te gustaría hacer?".format(player_name))


        return []

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
            text="Muy bien! Has acertado el sonido es un " + s_player
        elif player_resp == '':
            text = " Es una opcion incorrecta"
        else:
         text = "oh! el sonido no es un " + s_player + ", la respuesta  es: " + s_currently
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

