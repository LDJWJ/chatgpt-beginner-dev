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
# 공의 초기 위치, 반지름, 속도를 설정
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_radius = 10
ball_speed_x = -5
ball_speed_y = -5

# 게임 루프
running = True
while running:
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
    # 공의 초기 x, y좌표를 화면 가운데로 설정
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 공의 화면 경계 처리
    # ball_x가 0이하이거나 screen_width 이상이면, ball_speed_x의 방향을 반대로 바꿉니다.
    if ball_x <= 0 or ball_x >= screen_width:
        ball_speed_x *= -1
    # ball_y가 0이하이거나 screen_height 이상이면, ball_speed_y의 방향을 반대로 바꿉니다.
    if ball_y <= 0 or ball_y >= screen_height:
        ball_speed_y *= -1

    # 공과 패들의 충돌 처리
    # (paddle_x < ball_x < paddle_x + paddle_width) 공의 x좌표가 패들의 너비 범위 내에 있는지 확인
    # (paddle_y < ball_y < paddle_y + paddle_height) 공의 y좌표가 패들이ㅡ 높이 범위 내에 있는지 확인
    # 두 조건이 만족될 경우, 공과 패들이 충돌된 것으로 판단하여 ball_speed_y의 방향을 반대로 변경.
    if (paddle_x < ball_x < paddle_x + paddle_width) and (paddle_y < ball_y < paddle_y + paddle_height):
        ball_speed_y *= -1

    # 화면 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))

    # 화면에 공을 그립니다.
    # screen은 그릴 대상 화면, white는 원의 색상, (int(ball_x), int(ball_y))는 원의 중심 좌표, ball_radius는 원의 반지름
    pygame.draw.circle(screen, white, (int(ball_x), int(ball_y)), ball_radius) 

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 간 지연 시간을 설정.
    # pygame.time.delay(30)은 30밀리초 동안 프로그램 실행을 지연시킵니다. 이렇게 하면 게임 속도를 조절할 수 있습니다.
    pygame.time.delay(30) 
    
# Pygame 종료
pygame.quit()
sys.exit()