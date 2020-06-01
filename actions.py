# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import sys
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pygame import mixer  # Load the popular external library


##########################################################
# Available actions for the aplication
##########################################################
# 1 - Mensaje de bienvenida

# 2 - A little explanation about how the classification works-
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


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hola_mundo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionTraining(Action):

    def name(self) -> Text:
        return "action_training"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=" Hola, ya estamos entrenando  !")
        mixer.init()
        mixer.music.load('Sounds/dontremove.mp3')
        mixer.music.play()

        ## En este caso deberiamos saber como dirigir el flujo segun nuestro codigo aqui

        ## y hacer preguntas al usuario par apoder ir

        return []


class ActionClassifying(Action):

    def name(self) -> Text:
        return "action_classifying"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ya estamos clasificando ....")
        print("FUCK THIS ")
        return []


####################################################################################################################
# 2: ACTIONS FOR SOUND SELECTION
####################################################################################################################

class ActionSoundASelector(Action):

    def name(self) -> Text:
        return "action_sounda_selector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ya estamos clasificando ....")

        return []


class ActionSoundBSelector(Action):

    def name(self) -> Text:
        return "action_soundb_selector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ya estamos clasificando ....")

        return []


class ActionSoundCSelector(Action):

    def name(self) -> Text:
        return "action_soundc_selector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ya estamos clasificando ....")

        return []


class ActionSoundDSelector(Action):

    def name(self) -> Text:
        return "action_soundd_selector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ya estamos clasificando ....")

        return []


class ActionSoundESelector(Action):

    def name(self) -> Text:
        return "action_sounde_selector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ya estamos clasificando ....")

        return []


class ActionRandomSoundSelector(Action):

    def name(self) -> Text:
        return "action_randomsound_selector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ya estamos clasificando ....")

        return []
