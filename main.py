"""
Aquest fitxer conté el codi principal del joc "Corre Cristià!".
El joc consisteix en controlar un personatge que ha d'evitar els sables mentre arreplega taronges per sumar punts.
Les mecàniques del joc són les següents:
    Els sables apareixen a la pantalla i el jugador els ha d'esquivar movent-se cap als costats.
    Hi haurà taronges que donaran 10 punts al jugador per arreplegar cada una.
    El joc acaba quan el personatge xoca amb un sable.

Autor: VicentMY
Versió: 1.0
Última modificació: 12/10/2024
"""
# Dependències
import os
import pygame
import const
from jugador import Jugador
from obstacle import Obstacle
from taronja import  Taronja

# Inicialització de Pygame
pygame.init()

# Configuració de la pantalla
pantalla = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption("Corre Cristià!")

# Fonts
font = pygame.font.Font(None, 74)
font.set_underline(True)
font.set_italic(True)
smallFont = pygame.font.Font(None, 36)

# Música de fons
pygame.mixer.music.load(os.path.join(const.BASE_DIR, "assets/audio/Paquito_el_chocolatero.mp3"))
pygame.mixer.music.play(-1) # Reproduir la cançó en bucle

def mostrarPantallaTitol():
    """Mostar la pantalla de títol del joc."""
    # Asignar fons de pantalla
    fons = pygame.image.load(os.path.join(const.BASE_DIR, "assets/img/title-screen-background.jpg")).convert()
    fons = pygame.transform.scale(fons, (const.WIDTH, const.HEIGHT))
    pantalla.blit(fons, (0, 0))

    # Crear quadres de text
    textTitol = font.render("Corre Cristià!", True, const.VERD, const.GRIS)
    textInici = smallFont.render("Apreta qualsevol tecla per a començar.", True, const.VERD, const.GRIS)
    textAjuda =smallFont.render("Per a vore els controls apreta la tecla 'H'.", True, const.VERD, const.GRIS)

    # Afegir quadres de text a la pantalla
    pantalla.blit(textTitol, textTitol.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 200) ))
    pantalla.blit(textInici, textInici.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 150) ))
    pantalla.blit(textAjuda, textAjuda.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 200) ))
    # Actualitzar la pantalla
    pygame.display.flip()

    esperant = True
    while esperant:
        # KeyListener
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[pygame.K_h]:
                # Mostrar la pantalla d'ajuda
                mostrarPantallaAjuda()
                mostrarPantallaTitol()
            elif event.type == pygame.QUIT:
                # Tancar el joc
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                # Eixir de la pantalla de títol
                esperant = False

def mostrarPantallaAjuda():
    """Mostrar la pantalla d'ajuda del joc."""
    # Asignar fons de pantalla
    fons = pygame.image.load(os.path.join(const.BASE_DIR, "assets/img/main-background.jpg")).convert()
    fons = pygame.transform.scale(fons, (const.WIDTH, const.HEIGHT))
    pantalla.blit(fons, (0, 0))

    # Crear quadres de text
    textLiniaT = font.render("Corre Cristià! - Ajuda", True, const.VERD, const.GRIS)
    textLinia1 = smallFont.render("El jugador controla un personatge que ha d'evitar els", True, const.VERD, const.GRIS)
    textLinia2 = smallFont.render("els sables mentre arreplega taronges per sumar punts.", True, const.VERD, const.GRIS)
    textLinia3 = smallFont.render("El joc acaba quan el personatge xoca amb un sable.", True, const.VERD, const.GRIS)
    textLinia4 = smallFont.render("Apreta qualsevol tecla per tornar al joc.", True, const.VERD, const.GRIS)
    textLinia5 = smallFont.render("Utilitza les tecles '<-' i '->' o 'A' i 'D' per a mouret.", True, const.VERD, const.GRIS)
    textLiniaF = smallFont.render("Joc v.1 realitzat per VicentMY.", True, const.VERD, const.GRIS)

    # Afegir quadres de text a la pantalla
    pantalla.blit( textLiniaT, textLiniaT.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 200) ))
    pantalla.blit( textLinia1, textLinia1.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 150) ))
    pantalla.blit( textLinia2, textLinia2.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 125) ))
    pantalla.blit( textLinia3, textLinia3.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 50) ))
    pantalla.blit( textLinia4, textLinia4.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 50) ))
    pantalla.blit( textLinia5, textLinia5.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 100) ))
    pantalla.blit( textLiniaF, textLiniaF.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 250) ))
    # Actualitzar la pantalla
    pygame.display.flip()

    esperant = True
    while esperant:
        # KeyListener
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                # Eixir de la pantalla d'ajuda
                esperant = False

def mostrarPantallaFinal(puntuacio):
    """Mostrar la pantalla final del joc."""
    # Asignar fons de pantalla
    fons = pygame.image.load(os.path.join(const.BASE_DIR, "assets/img/end-screen-background.jpg")).convert()
    fons = pygame.transform.scale(fons, (const.WIDTH, const.HEIGHT))
    pantalla.blit(fons, (0, 0))

    # Crear quadres de text
    textTitol = font.render("Corre Cristià! - Fi de la partida", True, const.VERD, const.GRIS)
    textPuntuacio = smallFont.render(f"La teua puntuació és {puntuacio} punts.", True, const.VERD, const.GRIS)
    textFi = smallFont.render("Apreta qualsevol tecla per tancar el joc.", True, const.VERD, const.GRIS)
    textInstruccio = smallFont.render("Apreta la tecla 'R' per a començar una nova partida ", True, const.VERD, const.GRIS)

    # Afegir quadres de text a la pantalla
    pantalla.blit(textTitol, textTitol.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 200) ))
    pantalla.blit(textPuntuacio, textPuntuacio.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 100) ))
    pantalla.blit(textFi, textFi.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 100) ))
    pantalla.blit(textInstruccio, textInstruccio.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 150) ))
    # Actualitzar la pantalla
    pygame.display.flip()

    esperant = True
    while esperant:
        # KeyListener
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                # Començar una nova partida
                main()
            elif event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                # Tancar el joc
                pygame.quit()
                exit()

# Funció principal del joc
def main():
    """Funció principal del joc."""
    clock = pygame.time.Clock()
    # Crear el jugador
    jugador = Jugador()

    # Crear els grups d'objectes
    obstacles = pygame.sprite.Group()
    taronges = pygame.sprite.Group()
    objectes = pygame.sprite.Group()
    # Afegir el jugador al grup principal d'objectes
    objectes.add(jugador)

    # Fons principal
    fons = pygame.image.load(os.path.join(const.BASE_DIR, "assets/img/main-background.jpg")).convert()
    fons = pygame.transform.scale(fons, (const.WIDTH, const.HEIGHT))

    # Crear els obstacles i afegir-los al grup
    for i in range(8):
        obstacle = Obstacle()
        obstacles.add(obstacle)
        objectes.add(obstacle)

    # Crear les taronges i afegir-les al grup
    for i in range(5):
        taronja = Taronja()
        taronges.add(taronja)
        objectes.add(taronja)

    mostrarPantallaTitol()
    # Començar l'execució del joc
    puntuacio = 0
    run = True
    while run:
        # Asignar fotogràmes per segon del joc
        clock.tick(const.FPS)

        # Permitir tancar el joc an qualsevol moment
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Actualitzar cada objecte de la llista d'objectes
        objectes.update()

        # Comprovar col·lisions amb obstacles
        if pygame.sprite.spritecollideany(jugador, obstacles):
            # Parar el joc
            run = False

        # Comprovar les col·lisions amb taronges i eliminar la taronja en la que es col·lisiona
        xocsTaronja = pygame.sprite.spritecollide(jugador, taronges, True)
        # Sumar puntuació i afegir una nova taronja a la llista
        for xoc in xocsTaronja:
            puntuacio += 10
            taronja = Taronja()
            taronges.add(taronja)
            objectes.add(taronja)

        # Asignar el fons
        pantalla.blit(fons, (0, 0))
        # Dibuixar els objectes en la pantalla
        objectes.draw(pantalla)
        # Dibuixar la puntuació actual
        textPuntuacio = smallFont.render(f"{puntuacio} punts.", True, const.VERD, const.GRIS)
        pantalla.blit(textPuntuacio, (50, 50))
        # Actualitzar la pantalla abans de iterar
        pygame.display.flip()

    mostrarPantallaFinal(puntuacio)

if __name__ == "__main__":
    main()
