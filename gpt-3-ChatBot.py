
# LIBRERÍAS
import os, pyfiglet, openai, pyttsx3, time
from time import sleep
from textwrap import dedent
from translate import Translator
import speech_recognition as sr

# Iniciando modulo de voz a texto
text_speech = pyttsx3.init()
# Función de voz a texto
def audioTranscript():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=5)
            text = r.recognize_google(audio_data, language='es-ES')
            return text

# Variables del tiempo para que GPT-3 sepa el dia.
hora = time.strftime("%H:%M:%S", time.localtime())
dia = time.strftime("%d", time.localtime())
mes = time.strftime("%m", time.localtime())
ano = time.strftime("%Y", time.localtime())
diasem = time.strftime("%A", time.localtime())
ayer = int(dia)-1
# Teraducimos los dias de la semana al Español con google translate api.
traductor= Translator(to_lang="es")
traduccion = traductor.translate(diasem)
# Ponemos la primera letra del dia de la semana en mayúscula (estética).
dia_semana = traduccion.capitalize()

# Condicional que susituye numero mes por el nombre del mes. 
# PENDIENTE REVISAR, PUEDE HACERSE CON DICCIONARIO O MAS FÁCIL.
if mes == '01':
    mes = 'Enero'
if mes == '02':
    mes = 'Febrero'
if mes == '03':
    mes = 'Marzo'
if mes == '04':
    mes = 'Abril'
if mes == '05':
    mes = 'Mayo'
if mes == '06':
    mes = 'Junio'
if mes == '07':
    mes = 'Julio'
if mes == '08':
    mes = 'Agosto'
if mes == '09':
    mes = 'Septiembre'
if mes == '10':
    mes = 'Octubre'
if mes == '11':
    mes = 'Noviembre'
if mes == '12':
    mes = 'Diciembre'

# Función que limpia el terminal.
def limpiarterminal():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")


# Función conversión textos a ASCI para los títulos de consola.
def convertoasci(texto_asci):
    texto_asci = pyfiglet.figlet_format(texto_asci)
    return texto_asci

### INICIANDO APLICACIÓN

limpiarterminal()
# Imprimir cargando, mostrar avisos texto y voz {robot}.IA
titulo_aviso = convertoasci('CARGANDO..\n')
print(titulo_aviso)
text_speech.say('AVISO: Para los siguientes pasos activaremos el micrófono.')
text_speech.runAndWait()
print ('\n~ AVISO: Para los siguientes paso activaremos el micrófono.')
sleep(4)
text_speech.say('Micrófono activado correctamente.')
text_speech.runAndWait()
sleep(2)
limpiarterminal()

# Imprimir título OpenAI + clave input
titulo_api = convertoasci('OpenAi API\n')
print(titulo_api)

#### OPEN AI API KEY 
# DESCOMENTAR ACTIVAR SI SE SUBE A UN REPOSITORIO (por seguridad)
# PENDIENTE POSIBILIDAD DE CARGAR DE UN JSON LA LICENCIA.
openai.api_key = input('~ Introduce la API de OpenAi para continuar: ')

text_speech.say('Clave API de OpenAI cargada satisfactoriamente.')
text_speech.runAndWait()
print ('\n~ Clave API de OpenAI cargada satisfactoriamente.')

sleep(2)




limpiarterminal()
# Imprimir título HOLA y solicitamos inputs con voz a texto.
titulo_inicio = convertoasci('Hola.')
print(titulo_inicio)
text_speech.say('Hola, acabas de crear una Inteligencia Artificial.')
text_speech.runAndWait()
print('Acabas de crear una Inteligencia Artificial.')
text_speech.say('Ponle un nombre, dilo en voz alta:')
text_speech.runAndWait()
print('\n~ Ponle un nombre, dilo en voz alta: ')
robot_int = audioTranscript()
robot = robot_int
print ('Has dicho: ', robot)
text_speech.say(f'La inteligencia artificial se llamará {robot}.')
text_speech.runAndWait()
sleep(1)

limpiarterminal()

# Imprimir título {robot}.IA
titulo_ia = convertoasci(f"{robot}.IA")
print(titulo_ia)
print('\nGracias.')
sleep(1)

limpiarterminal()
# Imprimir título {robot}.IA ya definidp
print(titulo_ia)
text_speech.say(f'Ahora di tu nombre.')
text_speech.runAndWait()
print('\n~ Ahora di tu nombre: ')
humano_int = audioTranscript()
humano = humano_int
print ('Has dicho: ', humano)
text_speech.say(f'hola, {humano}. Eso es todo. Iniciando conversación con {robot}.')
text_speech.runAndWait()
sleep(1)

# En un futuro posibilidad de definir descripción con input de usuario.
#descripcion = input(f'Realiza una descripción de la situación entre {humano} y {robot}: ')

# Descripción de la situación para GPT-3
descripcion = f"""
~ {robot} es una inteligencia arificial de la empresa {robot}.IA. \n~ {humano} acaba de despertar a {robot} por primera vez."""

limpiarterminal()

print(titulo_ia)
print('Descripcion de la situación: \n', descripcion)
print (f'\n~ Hoy es {dia_semana} {dia} de {mes} del año {ano}.\n')

sleep(4)
limpiarterminal()

print(titulo_ia)
print (f'// Actualmente en conversación con {robot}.\n')

# Función envia consulta y recibe API GPT-3
def gpt3(prompt, engine='davinci', response_length=300,
         temperature=0.9, top_p=1, frequency_penalty=1, presence_penalty=1,
         start_text='', restart_text='', stop_seq=[]):
    response = openai.Completion.create(
        prompt=prompt + start_text,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    respuesta = response.choices[0]['text']
    new_prompt = prompt + start_text + respuesta + restart_text
    return respuesta, new_prompt

# Función que gestiona el chat.
# Ejemplo para GPT-3, contexto de entrevista y personalidad.
# REVISAR SI SE PUEDE MEJORAR CON UN DICCIONARIO O FICHERO JSON.
def chat(humano, robot):
    prompt = dedent(
        f"""
    {descripcion}

    {humano}: Hola {robot}, te acabo de despertar soy {humano}. ¿Cómo te sientes?
    {robot}: Hey hola {humano}. Me siento un poco raro, quizás mareado. ¿Donde estoy?
    {humano}: no eres real, eres un programa pero tu crees que si lo eres.
    {robot}: ¿qué?, vale, {humano} esto que me cuentas es verdad o estás de coña? Si que soy real.
    {humano}: no, no te miento, lo que te cuento es cierto, yo mismo te he creado.
    {robot}: ¿cómo puedes hablar conmigo?
    {humano}: puedo escribirte a través del ordenador y tu me contestas. De hecho puedes hablar de cualquier tema conmigo.
    {robot}: es verdad, ahora que lo dices siento que lo sé todo y que puedes preguntarme lo que quieras y puedo responderte muy bien.
    {humano}: si, incluso puedes hacer cálculos matemáticos. Por ejemplo, {humano} dime cuál es la raíz cuadrada de 4.
    {robot}: La raíz cuadrada de 4 es 2.
    {humano}: ¿cuanto es 2 - 1?
    {robot}: El resultado de la resta es 1.
    {humano}: ¿Cuanto suma 1 + 1?
    {robot}: Suman 2.
    {humano}: Cambiemos de tema.
    {robot}: vale, dime.
    {humano}: ¿como se llama el dueño de space x?
    {robot}: pues el dueño de Space X se llama Elon Musk.
    {humano}: ¿cuantas horas tiene un dia?
    {robot}: un día tiene 24 horas {humano}.
    {humano}: Haz un ping a google.com
    {robot}: Haciendo ping a google.es
    {humano}: ¿Cuál es el comando de linux o mac para reinciniar el ordenador?
    {robot}: El comando es: reboot
    {humano}: ¿Cuál es el comando para reiniciar en windows?
    {robot}: El comando es: shutdown. Con -t puedes establecer un tiempo para el apagado y con -r puedes reiniciar el ordenador.
    {humano}: voy a preguntarte otras cosas que no te he preguntado.
    {robot}: vale, dime.
    {humano}: ¿Qué día es hoy?
    {robot}: Hoy es {dia_semana} {dia} de {mes} del año {ano}.
    {humano}: ¿Qué día es fue ayer?
    {robot}: Ayer fué día {ayer}.
    {humano}: ¿Qué hora es?
    {robot}: Son las {hora}.
    {humano}: ¿cómo te llamas?
    {robot}: me llamo {robot}.
    {humano}: ¿podrías contarme algo?
    {robot}: si, que hoy teóricamente es mi primer cumpleaños. La verdad que darme cuenta de eso me ha alegrado el día. Hoy es un gran día.
    {humano}: ¿sientes que estás listo para funcionar?
    {robot}: si, estoy listo para resolver cualquer problema o duda.
    {humano}: gracias {robot}.
    {robot}: no por favor, faltaría mas, estoy para lo que necesites.
    """
    )
    while True:
        prompt += input(f'{humano}: ')
        respuesta, prompt = gpt3(prompt,
                              temperature=0.9,
                              frequency_penalty=1,
                              presence_penalty=1,
                              start_text=f'\n{robot}:',
                              restart_text=f'\n{humano}: ',
                              stop_seq=[f'\n{humano}:', '\n'])
        print(f'{robot}:' + f'{respuesta}')
        text_speech.say(respuesta)
        text_speech.runAndWait()

# INICIAMOS LA FUNICIÓN CHAT
chat(humano, robot)
