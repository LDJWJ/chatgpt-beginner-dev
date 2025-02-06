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
paddle_width = 60
paddle_height = 10
paddle_x = (screen_width - paddle_width) / 2
paddle_y = screen_height - paddle_height - 20
paddle_speed = 20

# 공 설정
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_radius = 10
ball_speed_x = 5
ball_speed_y = -5

# 폰트 설정
# 게임에서 사용할 폰트를 설정합니다.
# 시스템 기본 폰트, 폰트 크기를 74로 설정 
font = pygame.font.Font(None, 74)

# 게임 루프
running = True

# game_over 변수를 False로 초기화합니다. 이 변수는 게임 오버 여부를 추적하는 데 사용.
game_over = False
while running and not game_over:  # game_over가 True가 될 때까지만 게임 루프가 실행
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리 - 추가 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    # 패들의 화면 경계 처리 - 추가 
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > screen_width - paddle_width:
        paddle_x = screen_width - paddle_width

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 공의 화면 경계 처리
    if ball_x <= 0 or ball_x >= screen_width:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1

    # 공과 패들의 충돌 처리
    if (paddle_x < ball_x < paddle_x + paddle_width) and (paddle_y < ball_y < paddle_y + paddle_height):
        ball_speed_y *= -1

    # 게임 오버 조건 처리
    # 게임 오버 조건을 처리. 공의 y 좌표가 화면 높이보다 크면, 즉 공이 화면 아래로 떨어지면 game_over를 True로 설정.
    if ball_y > screen_height:
        game_over = True

    # 화면 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (int(ball_x), int(ball_y)), ball_radius) 

    # 게임 오버 메시지 출력
    # font.render("Game Over", True, white)는 "Game Over" 텍스트를 흰색으로 렌더링합니다.
    # screen.blit(text, (150, screen_height // 2 - 50))는 렌더링된 텍스트를 화면에 출력합니다. 위치는 (150, 화면 높이의 절반 - 50)
    # pygame.display.flip()은 화면을 업데이트
    # pygame.time.delay(2000)는 2초 동안 게임 오버 화면을 표시
    # print("Game Over!")는 콘솔에 "Game Over!"를 출력
    # running = False는 게임 루프를 종료
    if game_over:
        # 게임 오버 텍스트 렌더링 및 화면에 표시
        text = font.render("Game Over", True, white)
        screen.blit(text, (150, screen_height // 2 - 50))
        pygame.display.flip()
        pygame.time.delay(2000)  # 2초간 화면 표시
        print("Game Over!")
        running = False
        
    # 화면 업데이트
    pygame.display.flip()
    pygame.time.delay(30) 

   
# Pygame 종료
pygame.quit()
sys.exit()