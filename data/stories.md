## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_if_you_want
  - utter_question_a
  
## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_if_you_want
  - utter_question_a

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye


## 1A camino para empezar el dialogo del programa 
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_if_you_want
  - utter_question_a
  
  
## 2A - entrenamiento
* bot_entrenar
  - utter_entrenar
  - action_training

## 2b - clasificacion
* bot_clasificar
  - utter_clasificar
  - action_classifying

## 2C - Opciones 

* bot_opciones
  - utter_if_you_want
  - utter_question_a    


## say goodbye
* goodbye
  - utter_goodbye
  

## bot challenge
* bot_challenge
  - utter_iamabot

## Ejeuccion Hola mundo
* hola_mundo
  - action_hola_mundo
  
