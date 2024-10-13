"""
Aquest fitxer conté el codi principal del joc "Corre Cristià!".
El joc consisteix en controlar un personatge que ha d'evitar els sables mentre arreplega taronges per sumar punts.
Les mecàniques del joc són les següents:
    Els sables apareixen a la pantalla i el jugador els ha d'esquivar movent-se cap als costats.
    Hi haurà taronges que donaran 10 punts al jugador per arreplegar cada una.
    El joc acaba quan el personatge xoca amb un sable.

Autor: VicentMY
Versió: 1.0
Última modificació: 13/10/2024
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
pygame.mixer.init()
musica = pygame.mixer.music
musica.load(os.path.join(const.BASE_DIR, "assets/audio/Paquito_el_chocolatero.mp3"))
musica.play(-1) # Reproduir la cançó en bucle
musica.set_volume(1.0) # Ajustar el volum de la música al 100%

def mostrarPantallaTitol():
    """Mostar la pantalla de títol del joc."""
    # Asignar fons de pantalla
    fons = pygame.image.load(os.path.join(const.BASE_DIR, "assets/img/title-screen-background.jpg")).convert()
    fons = pygame.transform.scale(fons, (const.WIDTH, const.HEIGHT))
    pantalla.blit(fons, (0, 0))

    # Crear quadres de text
    textTitol = font.render("Corre Cristià!", True, const.VERD, const.GRIS)
    textInici = smallFont.render("Apreta la tecla 'SPACE' per a començar.", True, const.VERD, const.GRIS)
    textAjuda =smallFont.render("Per a vore els controls apreta la tecla 'H'.", True, const.VERD, const.GRIS)
    textEixir = smallFont.render("Per a eixir del joc apreta la tecla 'ESC'.", True, const.VERD, const.GRIS)

    # Afegir quadres de text a la pantalla
    pantalla.blit(textTitol, textTitol.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 200) ))
    pantalla.blit(textInici, textInici.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 150) ))
    pantalla.blit(textAjuda, textAjuda.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 200) ))
    pantalla.blit(textEixir, textEixir.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 250) ))

    # Actualitzar la pantalla
    pygame.display.flip()

    esperant = True
    while esperant:
        # KeyListener
        tecla_presionada = False
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[pygame.K_h]:
                # Mostrar la pantalla d'ajuda i altra vegada aquesta quan es tanque
                mostrarPantallaAjuda()
                esperant = False
                mostrarPantallaTitol()

            elif key[pygame.K_SPACE]:
                # Eixir de la pantalla de títol
                esperant = False

            elif key[pygame.K_m] and not tecla_presionada:
                # Pausar o reanudar la música
                pausaMusicaFons()
                tecla_presionada = True

            elif key[pygame.K_PLUS] and not tecla_presionada:
                # Pujar el volum de la música
                pujarVolMusica()
                tecla_presionada = True

            elif key[pygame.K_MINUS] and not tecla_presionada:
                # Baixar el volum de la música
                baixarVolMusica()
                tecla_presionada = True

            elif event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                # Tancar el joc
                pygame.quit()
                exit()

            elif not any(key):
                # Resetejar tecla_pressionada quant no s'apreta cap tecla (Evita que es repetisca la funció de la tecla)
                tecla_presionada = False

def mostrarPantallaAjuda():
    """Mostrar la pantalla d'ajuda del joc."""
    # Asignar fons de pantalla
    fons = pygame.image.load(os.path.join(const.BASE_DIR, "assets/img/main-background.jpg")).convert()
    fons = pygame.transform.scale(fons, (const.WIDTH, const.HEIGHT))
    pantalla.blit(fons, (0, 0))

    # Crear quadres de text
    textLiniaT = font.render("Corre Cristià! - Ajuda", True, const.VERD, const.GRIS)
    textLinia1 = smallFont.render("El jugador controla un personatge que ha d'evitar els els sables mentre arreplega", True, const.VERD, const.GRIS)
    textLinia2 = smallFont.render("taronges per sumar punts.", True, const.VERD, const.GRIS)
    textLinia3 = smallFont.render("El joc acaba quan el personatge xoca amb un sable.", True, const.VERD, const.GRIS)
    textLinia4 = smallFont.render("Apreta la tecla 'ESC' per tornar al joc i per parar el joc durant la partida.", True, const.VERD, const.GRIS)
    textLinia5 = smallFont.render("Utilitza les tecles '<-' i '->' o 'A' i 'D' per a mouret cap als costats.", True, const.VERD, const.GRIS)
    textLinia6 = smallFont.render("Apreta la tecla 'M' per parar la música de fons i '+' o '-' per a pujar o baixar el volumen.", True, const.VERD, const.GRIS)
    textLiniaF = smallFont.render("Joc v.1 realitzat per VicentMY.", True, const.VERD, const.GRIS)

    # Afegir quadres de text a la pantalla
    pantalla.blit(textLiniaT, textLiniaT.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 200) ))
    pantalla.blit(textLinia1, textLinia1.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 150) ))
    pantalla.blit(textLinia2, textLinia2.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 125) ))
    pantalla.blit(textLinia3, textLinia3.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 50) ))
    pantalla.blit(textLinia4, textLinia4.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 50) ))
    pantalla.blit(textLinia5, textLinia5.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 100) ))
    pantalla.blit(textLinia6, textLinia6.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 150) ))
    pantalla.blit(textLiniaF, textLiniaF.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 250) ))

    # Actualitzar la pantalla
    pygame.display.flip()

    esperant = True
    while esperant:
        # KeyListener
        tecla_presionada = False
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[pygame.K_m] and not tecla_presionada:
                # Pausar o reanudar la música
                pausaMusicaFons()
                tecla_presionada = True

            elif key[pygame.K_PLUS] and not tecla_presionada:
                # Pujar el volum de la música
                pujarVolMusica()
                tecla_presionada = True

            elif key[pygame.K_MINUS] and not tecla_presionada:
                # Baixar el volum de la música
                baixarVolMusica()
                tecla_presionada = True

            elif event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                # Eixir de la pantalla d'ajuda
                esperant = False

            elif not any(key):
                # Resetejar tecla_pressionada quant no s'apreta cap tecla (Evita que es repetisca la funció de la tecla)
                tecla_presionada = False

def mostrarPantallaFinal(puntuacio):
    """Mostrar la pantalla final del joc."""
    # Asignar fons de pantalla
    fons = pygame.image.load(os.path.join(const.BASE_DIR, "assets/img/end-screen-background.jpg")).convert()
    fons = pygame.transform.scale(fons, (const.WIDTH, const.HEIGHT))
    pantalla.blit(fons, (0, 0))

    # Crear quadres de text
    textTitol = font.render("Corre Cristià! - Fi de la partida", True, const.VERD, const.GRIS)
    textPuntuacio = smallFont.render(f"La teua puntuació és {puntuacio} punts.", True, const.VERD, const.GRIS)
    textFi = smallFont.render("Apreta la tecla 'ESC' per tancar el joc.", True, const.VERD, const.GRIS)
    textInstruccio = smallFont.render("Apreta la tecla 'R' per a començar una nova partida ", True, const.VERD, const.GRIS)

    # Afegir quadres de text a la pantalla
    pantalla.blit(textTitol, textTitol.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 200) ))
    pantalla.blit(textPuntuacio, textPuntuacio.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 - 100) ))
    pantalla.blit(textFi, textFi.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 100) ))
    pantalla.blit(textInstruccio, textInstruccio.get_rect( center=(const.WIDTH / 2, const.HEIGHT / 2 + 150) ))

    # Actualitzar la pantalla
    pygame.display.flip()

    sonant = True
    esperant = True
    while esperant:
        # KeyListener
        tecla_presionada = False
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                # Començar una nova partida
                main()

            elif key[pygame.K_m] and not tecla_presionada:
                # Pausar o reanudar la música
                pausaMusicaFons()
                tecla_presionada = True

            elif key[pygame.K_PLUS] and not tecla_presionada:
                # Pujar el volum de la música
                pujarVolMusica()
                tecla_presionada = True

            elif key[pygame.K_MINUS] and not tecla_presionada:
                # Baixar el volum de la música
                baixarVolMusica()
                tecla_presionada = True

            elif event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                # Tancar el joc
                pygame.quit()
                exit()

            elif not any(key):
                # Resetejar tecla_pressionada quant no s'apreta cap tecla (Evita que es repetisca la funció de la tecla)
                tecla_presionada = False

def pausaMusicaFons():
    """Pausar o reanudar la música de fons."""
    if musica.get_busy():
        musica.pause()
    else:
        musica.unpause()

def pujarVolMusica():
    """Pujar el volum de la música de fons."""
    musica.set_volume(musica.get_volume() + 0.25)

def baixarVolMusica():
    """Baixar el volum de la música de fons."""
    musica.set_volume(musica.get_volume() - 0.25)

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

        # Preparar el KeyListener
        key = pygame.key.get_pressed()

        # Control de la música
        # Pausar o reanudar
        if key[pygame.K_m] and not tecla_presionada:
            pausaMusicaFons()
            tecla_presionada = True

        # Pujar o baixar volumen
        if key[pygame.K_PLUS] and not tecla_presionada:
            pujarVolMusica()
            tecla_presionada = True

        if key[pygame.K_MINUS] and not tecla_presionada:
            baixarVolMusica()
            tecla_presionada = True

        # Resetejar tecla_pressionada quant no s'apreta cap tecla
        if not any(key):
            tecla_presionada = False

        # Permitir tancar el joc an qualsevol moment
        for event in pygame.event.get():
            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
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

        # Dibuixar el contador de la puntuació actual
        textPuntuacio = smallFont.render(f"{puntuacio} punts.", True, const.VERD, const.GRIS)
        pantalla.blit(textPuntuacio, (50, 50))

        # Actualitzar la pantalla abans de iterar
        pygame.display.flip()

    mostrarPantallaFinal(puntuacio)

if __name__ == "__main__":
    main()
