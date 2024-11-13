import pyttsx3, webbrowser 
import speech_recognition as sr
import pywhatkit, wikipedia
import yfinance as yf 
import pyjokes, datetime

'''
Escuchar el audio y transcribirlo a texto
'''
# id_1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
# id_2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

def trans_audio_texto():
    r = sr.Recognizer()
    
    # Configurar el micro
    with sr.Microphone() as origen:
        
        # Tiempo
        r.pause_threshold = 0.8
        
        # Debbug de la grabación
        print("Simón ya sirve")
        
        # Guardar la grabación
        audio = r.listen(origen)
        
        try:
            #Buscar en google lo que haya buscado
            solicitud = r.recognize_google(audio, language="es-mx")
            print("Dijistes: " + solicitud)
            
            return solicitud
        
        except sr.UnknownValueError:
            print("Cámara maik habla bien :v")
            
            return "Te estoy esperando... anciano"
        except sr.RequestError:
            print("Cámara maik no carburo :c")
            
            return "Te sigo esperando... anciano"
        except:
            print("Cámara maik no pos algo salió mal :c: ")
            
            return "Te sigo esperando... anciano x2"

def hablar(mensaje):
    
    # Encender pyttsx3
    engine = pyttsx3.init()
    
    # Reproducir mensaje
    engine.say(mensaje)
    engine.runAndWait()
        
def consultar_dia():
    
    fecha = datetime.date.today()
    
    # Sacar el día de la semana
    dia = fecha.weekday()
    print(dia)
    
    # Diccionario con los nombres de los días
    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miércoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sábado",
                  6: "Domigo"}
    # Decir el día de la semana
    hablar(f"Hoy es: {calendario[dia]}")

def consultar_hora():
    
    hora = datetime.datetime.now()
    hora = f"En este momento son las: {hora.hour} horas, con {hora.minute} minutos y {hora.second} segundos."
    # Decir hora
    hablar(hora)

def saludar():
    hablar("¡Hola, me llamo Katy! Soy tu asistente virtual.")
    
    #Decir hora y fecha
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento_hora = f"¡Descansa! Buenas noches, te escucho mañana por la mañana. En este momento son las: {hora.hour} horas, con {hora.minute} minutos y {hora.second} segundos. Dime, ¿En qué te puedo ayudar?"

    elif 6 <= hora.hour < 13:
        momento_hora =f"¡Buenos días! Espero que hayas descansado bien. Escucha como las aves cantan. En este momento son las: {hora.hour} horas, con {hora.minute} minutos y {hora.second} segundos. Dime, ¿En qué te puedo ayudar?"
    else:
        momento_hora = f"¿Ya terminaste las tareas matutinas? ¡Que tu tarde sea excelente! ¡Provecho! En este momento son las: {hora.hour} horas, con {hora.minute} minutos y {hora.second} segundos. Dime, ¿En qué te puedo ayudar?"
    
    hablar(momento_hora)
    
    
# Funcion central
def peticiones():
    
    # Activar el saludo
    saludar()
    
    # Bandera para continuar con las instrucciones
    iniciar = True
    while iniciar:
        
        #Activar el microfono y guardar el pedido
        solicitud = trans_audio_texto().lower()
        
        if "abre youtube" in solicitud:
            hablar("¡Con gusto! Estoy abriendo YouTube, permíteme un momento.")
            webbrowser.open("https://www.youtube.com")
            continue
        
        elif "abre el navegador" in solicitud:
            hablar("¡Con gusto! Estoy abriendo el navegador, permíteme un momento.")
            webbrowser.open("https://www.google.com")
            continue
        
        elif "qué día es hoy" in solicitud:
            consultar_dia()
            continue
        
        elif "qué hora es" in solicitud:
            consultar_hora()
            continue
        
        elif "busca en wikipedia" in solicitud:
            hablar("¡Con gusto! Estoy buscando en Wikipedia, permíteme un momento.")
            solicitud = solicitud.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado_busqueda = wikipedia.summary(solicitud, sentences=1)
            hablar("En Wikipedia encontré lo siguiente:")
            hablar(resultado_busqueda)
            continue
        
        elif "busca en internet" in solicitud:
            hablar("¡Con gusto! Estoy buscando en internet, permíteme un momento.")
            solicitud = solicitud.replace("busca en internet", "")
            pywhatkit.search(solicitud)
            hablar("Esto es lo que encontré en internet.")
            continue
        
        elif ("reproduce en youtube la canción de" in solicitud):
            hablar("¡Excelente! Estoy abriendo YouTube con tu canción, permíteme un momento.")
            solicitud = solicitud.replace("reproduce en youtube la canción de", "")
            pywhatkit.playonyt(solicitud)
            continue
        
        elif "cuéntame un chiste" in solicitud:
            hablar("¿Tienes ganas de un chiste? ¡Bueno! aquí va uno")
            hablar(pyjokes.get_joke("es"))
            continue
        
        elif "precio de las acciones" in solicitud:
            hablar("¡Veremos que tal van los mercados! permíteme un momento.")
            accion = solicitud.split("de")[-1].strip().lower()
            cartera = {"apple": "APPL",
                       "amazon": "AMZN",
                       "google": "GOOGL"}
            
            try:
                accion_busqueda = cartera[accion]
                accion_busqueda = yf.Ticker(accion_busqueda)
                precio_actual = accion_busqueda.info["regularMarketPrice"]
                hablar(f"Encontré la acción de {accion}, su precio es de: {precio_actual}")
                continue
            except:
                hablar("Lo siento, pero no he encontrado la acción")
                continue
            
        elif ("adiós" in solicitud) or ("hasta luego" in solicitud):
            hablar("¡Gracias por ocupar mis servicios!")
            break
        
peticiones()
            
