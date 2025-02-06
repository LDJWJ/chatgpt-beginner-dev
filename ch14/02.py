import pygame
import sys

# Pygame 초기화
pygame.init()

# 게임 화면 설정
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 루프
# True로 초기화, 게임 루프를 제어하는데 사용.
running = True

# 발생된 모든 이벤트를 가져옵니다. 
while running:   # running가 True인 동안 계속 실행.
    for event in pygame.event.get():

        # 창 닫기 이벤트를 감지하여 이 경우에 running을 False로 설정하여 게임 루프 종료
        if event.type == pygame.QUIT:
            running = False

    # 화면 그리기
    # 게임 화면을 검은색(RGB 값 0, 0, 0)으로 채웁니다. 이렇게 하면 이전 프레임의 내용을 지웁니다.
    screen.fill((0, 0, 0))

    # 화면 업데이트
    # pygame.display.flip()은 렌더링된 내용을 실제 화면에 업데이트합니다. 
    # 이 함수를 호출하지 않으면 화면이 업데이트되지 않습니다.
    pygame.display.flip()

# Pygame 종료
pygame.quit()   # pygame 라이브러리를 정상적으로 종료합니다.
sys.exit()      # Python 인터프리터 자체를 종료합니다.

