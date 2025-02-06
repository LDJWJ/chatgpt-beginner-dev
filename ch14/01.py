import pygame
import sys

pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))


# 위 코드는 파이게임과 시스템 라이브러리를 import합니다.

- pygame: 게임 개발을 위한 다양한 기능을 제공하는 라이브러리
- sys: 시스템 관련 기능을 제공하는 라이브러리 (예: 종료)

- pygame.init() 
# 함수는 파이게임을 초기화합니다. 게임 실행전에 이 함수를 호출해야 파이게임 기능을 사용할 수 있습니다.

# 위 코드는 화면 크기와 화면 객체를 설정합니다.

- screen_width: 화면 너비 (픽셀 단위)
- screen_height: 화면 높이 (픽셀 단위)
- screen: 게임 화면을 나타내는 객체
- pygame.display.set_mode() 
# pygame의 원도우를 생성합니다. 함수는 화면 크기를 지정하여 화면 객체를 생성합니다.
# 현재는 게임 창은 생성되지만, 아무것도 표시되지 않습니다.
