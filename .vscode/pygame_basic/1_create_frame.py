import pygame
pygame.init()# 초기화 필수

# 화면크기 설정
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정 
pygame.display.set_caption("NADO GAME")

# 이벤트 루프
running= True 
while running:
    for event in pygame.event.get():#어떤 이벤트가 발생하는가
        if event.type==pygame.QUIT: #창이 닫히는 이밴트가 발생했는가
            running=False

#pygame 종료
pygame.quit()