import pygame, os, random, math, io
from pygame import mixer

# Rutas de los directorios, porque sino se pone de princesa de que: NI INQIENTRI LI RITI :v
ruta_imagenes = os.getcwd() + "\\DIA_10\\images\\"
ruta_musica = os.getcwd() + "\\DIA_10\\music\\"
ruta_fuentes = os.getcwd() + "\\DIA_10\\fonts\\"

#Importar fuente
def fuente_to_bytes(fuente):
    with open(fuente, "rb") as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)

# Inicializar el pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((900, 700))

# Titulo de la pantalla y el ícono
pygame.display.set_caption("Space Battle")
icono = pygame.image.load(f"{ruta_imagenes}nave_espacial.png")
fondo = pygame.image.load(f"{ruta_imagenes}espacio.jpg")
pygame.display.set_icon(icono)

# Agregar musica
mixer.music.load(f"{ruta_musica}MusicaFondo.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# inicial del jugador
img_player = pygame.image.load(f"{ruta_imagenes}cohete.png")
jugador_x = 415
jugador_y = 630
jugador_x_cambio = 0
jugador_y_cambio = 0

# inicial de la bala
balas = []
img_bala = pygame.image.load(f"{ruta_imagenes}bala.png")
bala_x = 0
bala_y = 630
bala_y_cambio = 2
bala_visible = False

# inicial del ovni
img_ovni = []
ovni_x = []
ovni_y = []
ovni_x_cambio = []
ovni_y_cambio = []
cantidad_ovnis = 8

#Crear enemigos de acuerdo a cantidad_ovnis
for ov in range(cantidad_ovnis):
    img_ovni.append(pygame.image.load(f"{ruta_imagenes}ovni.png"))
    ovni_x.append(random.randint(0, 825))
    ovni_y.append(random.randint(25, 625))
    ovni_x_cambio.append(0.6)
    ovni_y_cambio.append(25)

# Puntaje
puntaje = 0
fuente_bytes = fuente_to_bytes(f"{ruta_fuentes}freesansbold.ttf")
fuente = pygame.font.Font(fuente_bytes, 32)
posicion_puntaje_x = 10
posicion_puntaje_y = 10

# Game over
final_fuente = pygame.font.Font(fuente_bytes, 40)

def final_juego():
    fuente_final_1 = final_fuente.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(fuente_final_1, (65, 205))
    
# Mostrar puntaje
def mostrar_puntaje(eje_x, eje_y):
    etiqueta_puntaje = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(etiqueta_puntaje, (eje_x, eje_y))


# Llamada al jugador
def jugador(eje_x, eje_y):
    pantalla.blit(img_player, (eje_x, eje_y))
    
# Llamada al ovni
def ovni(eje_x, eje_y, ovnis):
    pantalla.blit(img_ovni[ovnis], (eje_x, eje_y))

# Llamada a disparar bala
def disparar_bala(eje_x, eje_y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (eje_x + 16, eje_y + 10))
    
def hay_colision(eje_x_1, eje_y_1, eje_x_2, eje_y_2):
    distancia_x = math.pow(eje_x_2 - eje_x_1, 2)
    distancia_y = math.pow(eje_y_2 - eje_y_1, 2)
    distancia = math.sqrt(distancia_x + distancia_y)
    if distancia < 25:
        return True
    else:
        return False

# Se ejecuta para mostrar la pantalla hasta cerrar
ejecuta = True
while ejecuta:
    pantalla.blit(fondo, (0, 0))# Se pinta la pantalla con el fondo
    
    for evento in pygame.event.get():
        # Verifica si se cerró la pantalla
        if evento.type == pygame.QUIT:
            ejecuta = False
        '''
            Verifica si se presionaron la teclas: 
                1. D(Izquierda)
                2. A(Derecha)
                3. W(Arriba) 
                4. S(Arriba)
                5. SPACCE(Disparar)
        '''   
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                jugador_x_cambio = 0.6
            if evento.key == pygame.K_a:
                jugador_x_cambio = -0.6
            if evento.key == pygame.K_w:
                jugador_y_cambio = -0.6
            if evento.key == pygame.K_s:
                jugador_y_cambio = 0.6
            if evento.key == pygame.K_SPACE:
                disparo = mixer.Sound(f"{ruta_musica}Disparo.mp3")
                disparo.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
            
        # Verifica si se soltó cualquiera de las teclas izquiera o derecha
        if evento.type == pygame.KEYUP:
            if (evento.key == pygame.K_d) or (evento.key == pygame.K_a):
                jugador_x_cambio = 0
            if (evento.key == pygame.K_w) or (evento.key == pygame.K_s):
                jugador_y_cambio = 0
    
    # Modifica la posición en eje X para el jugador
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio
    
    # Verifica si el jugador llegó al borde de la ventana en eje X (Izquierda o Derecha)            
    if jugador_x <= 0:
        jugador_x = 0       
    elif jugador_x >= 830:
        jugador_x = 830
    
    # Verifica si el jugador llegó al borde de la ventana en eje Y (Arriba o Abajo)            
    if jugador_y <= 0:
        jugador_y = 0       
    elif jugador_y >= 630:
        jugador_y = 630
        
    # Modifica la posición en eje X para los ovnis
    for ov in range(cantidad_ovnis):
        
        if ovni_y[ov] > 600:
            for cant in range(cantidad_ovnis):
                ovni_y[cant] = 1000
            final_juego()
            break
                
        ovni_x[ov] += ovni_x_cambio[ov]
        
        # Verifica si los ovnis llegaron al borde de la ventana en eje X (Izquierda o Derecha)            
        if ovni_x[ov] <= 0:
            ovni_x_cambio[ov] = 0.6
            ovni_y[ov] += ovni_y_cambio[ov]       
        elif ovni_x[ov] >= 830:
            ovni_x_cambio[ov] = -0.6
            ovni_y[ov] += ovni_y_cambio[ov]
        
        #Colisionador
        for bala in balas:
            colision = hay_colision(ovni_x[ov], ovni_y[ov], bala["x"], bala["y"])
            if colision:
                collision = mixer.Sound(f"{ruta_musica}Golpe.mp3")
                collision.play()
                balas.remove(bala)
                #bala_y = 630
                #bala_visible = False
                puntaje += 1
                ovni_x[ov] = random.randint(0, 825)
                ovni_y[ov] = random.randint(25, 625)
                break
        # Pintar ovni en la pantalla
        ovni(ovni_x[ov], ovni_y[ov], ov)
    
    # Movimiento balas
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
        
    # Movimiento de la bala
    if bala_y <= -65:
        bala_y = 630
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio
        
    # Pintar jugador en la pantalla
    jugador(jugador_x, jugador_y)
    
    # Mostrar puntaje
    mostrar_puntaje(posicion_puntaje_x, posicion_puntaje_y)
    
    # Actualiza pantalla
    pygame.display.update()