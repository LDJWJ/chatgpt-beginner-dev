import pygame
import sys

# Pygame 초기화
pygame.init()

# 게임 화면 설정
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)

# 패들 설정
# 패들(paddle)의 크기, 위치, 속도를 설정 
paddle_width = 60
paddle_height = 10

# 패들의 초기 x, y좌표를 설정합니다.
paddle_x = (screen_width - paddle_width) / 2
paddle_y = screen_height - paddle_height - 20

# 패들의 이동 속도를 설정합니다.
paddle_speed = 20

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리 - 추가 
    # 
    keys = pygame.key.get_pressed() # 현재 눌린 키의 정보를 반환합니다.
    if keys[pygame.K_LEFT]:         # 왼쪽 화살표가 눌렸는지 확인
        paddle_x -= paddle_speed    # paddle_x를 paddle_speed만큼 감소시켜 패들을 왼쪽으로 이동
    if keys[pygame.K_RIGHT]:        # 오른쪽 화살표가 눌렸는지 확인
        paddle_x += paddle_speed    # paddle_x를 paddle_speed만큼 증가시켜 패들을 오른쪽으로 이동

    # 패들의 화면 경계 처리 - 추가 
    # 이 부분은 패들이 화면 경계를 벗어나지 않도록 처리합니다.
    if paddle_x < 0:    # 패들이 화면 왼쪽 경계를 벗어났으므로 paddle_x를 0으로 설정 
        paddle_x = 0
    if paddle_x > screen_width - paddle_width: # 패들의 화면 오른쪽 경계를 벗어났으므로 paddle_x를 
        paddle_x = screen_width - paddle_width # screen_width - paddle_width로 설정

    # 화면 그리기
    screen.fill(black)  # screen.fill(black)은 화면을 검은색

    # 흰색 사각형(패들)을 그립니다. 
    # paddle_x, paddle_y : 사각형의 좌상단 좌표
    # paddle_width, paddle_height : 사각형의 너비와 높
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()