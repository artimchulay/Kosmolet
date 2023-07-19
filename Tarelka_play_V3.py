#ЭТО ВЕРСИЯ ИГРЫ 3.1(ребаг)
import pygame
import random
#экран
pygame.init()
infoObject = pygame.display.Info()
pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
size = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
x = 0
#нужно для работы без ошибок при выходе
V = 1
L = 1
B = 1
st = 1
#создание звёзд на фоне
def draw():
    for i in range(100):
        screen.fill(pygame.Color('white'),
                    (random.random() * infoObject.current_w,
                     random.random() * infoObject.current_h, 1, 1))

# Берём из папки фотки
def load_image(name):
    fullname = "Foto" + "/" + name
    try:
        if name[-2:] == 'jpg':
            image = pygame.image.load(fullname).convert()
        else:
            image = pygame.image.load(fullname).convert_alpha()
    except:
        print('Cannot load image:', name)

        raise SystemExit()
    return image

#музыка
my_sound_1 = pygame.mixer.Sound("Cafeteria.mp3")
my_sound_1.play(-1)
#название окна
pygame.display.set_caption('WING COMMANDER')
running = True

#выбор сложности и заставка
while running:
    screen.fill((0, 0, 0))  # для чёткости текста
    draw()
    background = load_image("pipboy2.gif")
    screen.blit(background, (200, infoObject.current_h - 670))
    #вывод текста
    f1 = pygame.font.Font(None, 36)

    #текст
    text1 = f1.render('Выберите сложность игры: ', True, (50, 205, 50))
    screen.blit(text1, (520, infoObject.current_h - 550))

    text2 = f1.render('1-Легко', True, (50, 205, 50))
    screen.blit(text2, (520, infoObject.current_h - 500))

    text3 = f1.render('2-Сложно', True, (50, 205, 50))
    screen.blit(text3, (520, infoObject.current_h - 450))

    text4 = f1.render('3-Невозможно', True, (50, 205, 50))
    screen.blit(text4, (520, infoObject.current_h - 400))

    text5 = f1.render("'Нажмите нужную цифру на клавиатуре'", True, (50, 205, 50))
    screen.blit(text5, (520, infoObject.current_h - 350))

    pygame.display.flip()
    clock.tick(fps)

    #сложность(параметры)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            V = 3
            L = 100
            st = 60
            B = 25
            x = x + 1
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            V = 3
            L = 100
            st = 40
            B = 30
            x = x + 2
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            V = 4
            L = 100
            st = 30
            B = 40
            x = x + 3
            running = False
            # выход
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

#нужно для вывода в конце
if x == 1:
    Level = "Легко"
if x == 2:
    Level = "Сложно"
if x == 3:
    Level = "Невозможно"

#движене тарелки
def update(image, speed):
    #по Х
    if tal.rect.x + tal.rect.width >= infoObject.current_w:
        speed = -speed
    elif tal.rect.x < 0:
        speed = -speed
    tal.rect.x = tal.rect.x + speed
    return speed
#к звездолёту
image = load_image('Kosmolet_1.gif')
all_sprites = pygame.sprite.Group()
car = pygame.sprite.Sprite()
car.image = image
car.rect = car.image.get_rect()

if st != 1:
    all_sprites.add(car)

#для красного
image_5 = load_image('Kosmolet_2.gif')
car_red = pygame.sprite.Sprite()
car_red.image = image_5
car_red.rect = car_red.image.get_rect()
#Тарелка
image_2 = load_image('Tarelka.gif')
tal = pygame.sprite.Sprite()
tal.image = image_2
tal.rect = tal.image.get_rect()
if st != 1:
    all_sprites.add(tal)
random.seed()
tal.rect.x, tal.rect.y = random.randint(200, infoObject.current_w - 200), random.randint(100, 300)

#красная тарелка
image_6 = load_image('Tarelka_2.gif')
tal_red = pygame.sprite.Sprite()
tal_red.image = image_6
tal_red.rect = tal.image.get_rect()
#пересоздане тарелки
def tall():
    tal.rect.x, tal.rect.y = random.randint(200, infoObject.current_w - 200), random.randint(100, 300)
    all_sprites.add(tal_red)
#кординаты
car.rect.x = 500
car.rect.y = 500

#луч космолёта
image_3 = load_image('Piy.gif')
piy = pygame.sprite.Sprite()
piy.image = image_3
piy.rect = piy.image.get_rect()

#луч  тарелки
image_4 = load_image('Piy_2.gif')
piy_2 = pygame.sprite.Sprite()
piy_2.image = image_4
piy_2.rect = piy_2.image.get_rect()

#скорость тарелки и лучей и ещё некоторые переменные
v = V
r = 0
l = L
b = B
step = st

#музыка в игре
my_sound_1.set_volume(0)
my_sound_2 = pygame.mixer.Sound("musik.mp3")
my_sound_2.play(-1)
my_sound_2.set_volume(0.5)
running = True
#цикл

while running:
    #для выхода из выбора сложности
    if st == 1:
        running = False
    # возрат космолёта в экран
    #при увеличении размера экрана менять значения учитывая что шаг = 50
    #верх
    if car.rect.x <= infoObject.current_w - 100 and car.rect.y <= 0:
        # += step тк step = одному движению
        car.rect.y += step
    #низ
    if car.rect.x <= infoObject.current_w - 100 and car.rect.y >= infoObject.current_h - 100:
        car.rect.y -= step
    #лево
    if car.rect.x <= 50:
        car.rect.x += step
    #право
    if car.rect.x >= infoObject.current_w - 150:
        car.rect.x -= step

    # это кординаты
    tal_red.rect.x, tal_red.rect.y = tal.rect.x, tal.rect.y
    car_red.rect.x, car_red.rect.y = car.rect.x, car.rect.y
    #проверка на попадание от космолёта
    if  tal.rect.y <= piy.rect.y <= tal.rect.y + 140:
        if tal.rect.x + 10 <= piy.rect.x <= tal.rect.x + 100:
            b -= 1
            piy.kill()
            r += 1
            #звук попадания
            my_sound_3 = pygame.mixer.Sound("piy.mp3")
            my_sound_3.play(0)
            my_sound_3.set_volume(0.3)
            #убираем спрайт
            tal.kill()
            # добовляем новый
            tall()

    # проверка на попадание от тарелки
    if car.rect.y <= piy_2.rect.y <= car.rect.y + 140:
        if car.rect.x <= piy_2.rect.x <= car.rect.x + 150:
            l -= 1
            piy_2.kill()
            car.kill()
            #звук попадания
            my_sound_3 = pygame.mixer.Sound("piy.mp3")
            my_sound_3.play(0)
            my_sound_3.set_volume(0.3)
            all_sprites.add(car_red)

    # стрельба тарелки
    if car.rect.x <= tal.rect.x <= car.rect.x + 100:
        all_sprites.add(piy_2)
        piy_2.rect.x = tal.rect.x + 50
        piy_2.rect.y = tal.rect.y + 10
    car_red.rect.x, car_red.rect.y = car.rect.x, car.rect.y
    #основной
    for event in pygame.event.get():
        car_red.kill()
        all_sprites.add(car)
        tal_red.kill()
        all_sprites.add(tal)
        #движение космолёта
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            car.rect.y -= step

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            car.rect.y += step

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            car.rect.x -= step

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            car.rect.x += step

        # создание лазера ИЗ КОСМОЛЁТА  и стрельба при ЛКМ
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.add(piy)
            piy.rect.x = car.rect.x + 75
            piy.rect.y = car.rect.y - 30
        #выход
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #изменение цвета для космолётаd
    if l <= 150:
        Color = (50, 205, 50)
    if l <= 50:
        Color = (255, 255, 0)
    if l <= 25:
        Color = (255, 0, 0)

    # изменение цвета для тарелки
    if b <= 40:
        Color_t = (50, 205, 50)
    if b <= 20:
        Color_t = (255, 255, 0)
    if b <= 10:
        Color_t = (255, 0, 0)

    #проверка на то что энергия закончилась
    # у космолёта
    if l <= 0:
        running = False
    # у тарелки
    if b <= 0:
        running = False
    #заливка экрана
    screen.fill((0, 0, 0))
    #Энергия врага
    if st != 1:
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('ЭНЕРГИЯ ВРАГА: ' + str(b), True, (Color_t))
        screen.blit(text1, (350, 30))
    if st != 1:
        #Энергия космолёта
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render('ТВОЯ ЭНЕРГИЯ: ' + str(l), True, (Color))
        screen.blit(text2, (670, 30))
    #движене лазеров
    piy.rect.y -= 20
    piy_2.rect.y += 10
    #движене тарелки
    for sprite in all_sprites:
        v = update(sprite, v)
    #громкость лазера в 0
    #создане звёзд
    draw()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
my_sound_2.set_volume(0)
running = True
my_sound_1 = pygame.mixer.Sound("Cafeteria.mp3")
my_sound_1.play(-1)
my_sound_1.set_volume(1)
while running:
    screen.fill((0, 0, 0))  # для чёткости текста
    draw()
    background = load_image("pipboy2.gif")
    screen.blit(background, (200, infoObject.current_h - 670))

    #проигрыш
    if l <= 0:
        #вывод текста
        f1 = pygame.font.Font(None, 36)

        text1 = f1.render('Вас сбили!', True, (50, 205, 50))
        screen.blit(text1, (520, infoObject.current_h - 550))

        text2 = f1.render('У врага осталось ' +str(b) + ' энергии', True, (50, 205, 50))
        screen.blit(text2, (520, infoObject.current_h - 500))

        text2 = f1.render('На сложности: ' + str(Level), True, (50, 205, 50))
        screen.blit(text2, (520, infoObject.current_h - 450))

        text2 = f1.render('Для выхода нажмите esc ', True, (50, 205, 50))
        screen.blit(text2, (520, infoObject.current_h - 400))

    #победа
    if b <= 0:
        # вывод текста
        f1 = pygame.font.Font(None, 36)
        # текст
        text1 = f1.render('Вы сбили врага!', True, (50, 205, 50))
        screen.blit(text1, (520, infoObject.current_h - 550))

        text2 = f1.render('На сложности: ' + str(Level), True, (50, 205, 50))
        screen.blit(text2, (520, infoObject.current_h - 500))

        text2 = f1.render('Для выхода нажмите esc ', True, (50, 205, 50))
        screen.blit(text2, (520, infoObject.current_h - 450))

    #для нормального выхода из выбора сложности
    if l > 0 and b > 0:
        f1 = pygame.font.Font(None, 36)
        text2 = f1.render('Для выхода нажмите Esc', True, (50, 205, 50))
        screen.blit(text2, (520, infoObject.current_h - 500))
    pygame.display.flip()
    clock.tick(fps)

    #нажатие на цифры
    for event in pygame.event.get():
        # выход
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    print("Вы вышли из игры")

pygame.quit()