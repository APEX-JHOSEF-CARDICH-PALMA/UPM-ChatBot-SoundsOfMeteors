 # Sonidos del Cielo ( Sounds of Meteors )
  - [EN] This chatbot is being developed by Jhosef A. Cardich Palma as part of his Final Degree Project (TFG) for the Polytechnic University of Madrid. It is an application that offers an entertaining experience to classify sounds from the sky, with the idea of bringing the general public closer to science.
  - [ES] Este proyecto esta siendo desarrollado por Jhosef A. Cardich Palma como el trabajo de fin de carrera en la UPM. El trabajo tiene como objetivo la realizacion de un bot para el publico infanti, el cual podra clasificar los sonidos del cielo interanctuando con el asistente virtual. 
  
 ## Funcionamiento
 - En este repositorio se encuentra el proyecto, en el que se incluye el entorno virtual con el que se ha trabajado en  local (carpeta venv)
 sin embargo, en esta carpeta, se encuentra otra llamada "lib" (/venv/lib), la cual no se esta sincronizando con el repositorio aqui (pero si usa en local),
 debido a que  esta carpeta tiene dos modulos que pesand demasiado, por ello es recomendable, si deseas hacer funcionar esto:
 
 - Clonar el proyecto
 - Recomiendo usar Pycharm
 - Abrir el proyecto con Pycharm, entonces
 - Pycharm > preferencias .. 
 - Instalar paquete rasa (Esto reinstalara las dependencias que estan dentro de venv y asi instalara las que faltan tambien.
 - Una vez istalado podemos empezar a interactuar via teclado con nuestro bot ejecutando en la terminal: rasa shell
 - En el caso de que tengamos servicios, entonces tendremos que arrancar el servidor de servicios de rasa: rasa run services...
   en ese momento lo servicios estaran disponibles para que nuestro bot pueda llamarlos si reconoce alguno en la conversacion con el usuario

