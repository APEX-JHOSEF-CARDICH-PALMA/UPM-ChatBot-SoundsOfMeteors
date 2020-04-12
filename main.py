from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import  ChatterBotCorpusTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

#trainer.train(
#    "chatterbot.corpus.english.greetings"
#   "chatterbot.corpus.spanish.greetings"
#)

print('Hola! que tal todo ?? aqui podras clasificar sonidos del cielo ')
print('Puedes empezar entrenando, o si quieres podemos clasificar directamente')
print('Dime que quieres hacer ?')



trainer.train(
    "chatterbot.corpus.spanish.greetings",
)

trainer.train([
   "Quiero  entrenar",
   "Bien, entonces empecemos a entrenar!"
])


trainer.train([
   "Quiero  entrenar",
   "Bien, entonces empecemos a entrenar!"
])

trainer.train([
   "entrenar",
   "Vale!, pues vamos a entrenar!."
])

trainer.train([
   "deseo entrenar",
   "Venga, vamos a entrenar"
])


trainer.train([
   "Quiero  clasificar",
   "Bien, entonces empecemos a clasificar!"
])

trainer.train([
   "clasificar",
   "Vale!, pues vamos a clasificar!."
])

trainer.train([
   "deseo clasificar",
   "Venga, vamos a clasificar!"
])



#En esta parte tenemos la entrada del usuario
while True:
    terminal = input ('Tu: ')
    respuesta = chatbot.get_response(terminal)
    print('Bot: ', respuesta)


# Get a response to the input text 'I would like to book a flight.'



#response = chatbot.get_response('I would like to book a flight.')

#print(response)