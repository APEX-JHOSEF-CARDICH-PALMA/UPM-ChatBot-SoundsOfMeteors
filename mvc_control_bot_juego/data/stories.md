
## Ejeuccion Hola mundo
* mi_nombre
  - action_hola_mundo
  
  
#------------------------------------------------------------

## SAD PATH 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## SAD PATH 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_question_a
  
######################################################
## Historias de los flujos del juego 
######################################################
* bot_opciones
  - utter_opciones
  - utter_if_you_want
  - utter_question_b

######################################################
## Historias de los flujos del juego 
######################################################

## 1A camino para empezar el dialogo del programa 
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_question_a

## 1B - Preguntar el nombre 
* mi_nombre
  - utter_if_you_want
  - utter_question_b
  

######################################################
######################################################


## 2A - Aprendizaje
##-----------------------
* bot_aprender
  - utter_aprender
  - utter_presentando
  - utter_sonido_escucharas
  - utter_underdense_sample
  - action_underdense_sample 
  - utter_question_c
* affirm
  - utter_sonido_escucharas
  - utter_m_sample
  - action_m_sample
  - utter_question_c
* affirm
  - utter_sonido_escucharas
  - utter_over_larg
  - action_long_over_sample
  - utter_question_c
* affirm
  - utter_sonido_escucharas
  - utter_over_med
  - action_med_over_sample
  - utter_question_c
* affirm
  - utter_sonido_escucharas
  - utter_over_short
  - action_short_over_sample
  - utter_if_you_want
  - utter_question_b
  
# Reproducir un ejemplo de una underdense
* underdense_sample
  - utter_sonido_escucharas
  - action_underdense_sample
  - utter_underdense_sample
  - utter_if_you_want
  - utter_question_b
  
# Reproducir un ejemplo de una m
* m_sample
  - utter_sonido_escucharas
  - action_m_sample
  - utter_m_sample
  - utter_if_you_want
  - utter_question_b
  
# Reproducir un ejemplo de una overdense larga 
* long_over_sample
  - utter_sonido_escucharas
  - action_long_over_sample
  - utter_over_larg
  - utter_if_you_want
  - utter_question_b
  
# Reproducir un ejemplo de una overdense mediana 
* med_over_sample
  - utter_sonido_escucharas
  - action_med_over_sample
  - utter_over_med
  - utter_if_you_want
  - utter_question_b
  
# Reproducir un ejemplo de una overdense cortas 
* short_over_sample
  - action_short_over_sample
  - utter_over_short
  - utter_if_you_want
  - utter_question_b

#------------------------------------------------------------
  
## 2B - entrenamiento
##-----------------------------------------------------------

* bot_entrenar
  - utter_entrenar
  - utter_presentando
  - utter_metienes
  - utter_msg_audio
  - action_underdense_sample
  - utter_dime_de_que 
* tipo_sonidos 
  - action_check_sound
  - utter_msg_audio
  - action_m_sample
  - utter_dime_de_que 
* tipo_sonidos 
  - action_check_sound
  - utter_msg_audio
  - action_long_over_sample
  - utter_dime_de_que 
* tipo_sonidos 
  - action_check_sound
  - utter_msg_audio
  - action_med_over_sample
  - utter_dime_de_que 
* tipo_sonidos 
  - action_check_sound
  - utter_msg_audio
  - action_short_over_sample
  - utter_dime_de_que 
* tipo_sonidos
  - action_check_sound
  - utter_if_you_want
  - utter_question_b
#------------------------------------------------------------
## 2A - clasificacion
* bot_clasificar
  - utter_clasificar
  - action_classifying
  - utter_dime_de_que
  - action_save_clasificacion





######################################################
## Historias de despedida 
######################################################





## say goodbye
* goodbye
  - utter_goodbye
  

## bot challenge
* bot_challenge
  - utter_iamabot


