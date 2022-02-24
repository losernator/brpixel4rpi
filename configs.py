import board
# color preset
RED = (255,  0,  0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 250, 250)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
GREY = (30, 30, 30)
WHITE = (250, 250, 250) # better not to use

config = {
   # 4way Joystick pins
   # You can set NeoPixel LED index number with "~_led" parameter / comment out anything if you don't need LED
   # Default mk_arcade_joystick_rpi 1p pinmap - up:D4,down:D17,left:D27,right:D22,A:D25,B:D24,X:D15,Y:D18,TL:D14,TR:D23,start:D10,select:D9
   # 방향키 핀 및 LED 번호(순서)지정
   "UP":board.D4,
   #"UP_led": 0,
   "DOWN":board.D22,
   #"DOWN_led": 0,
   "LEFT":board.D17,
   #"LEFT_led": 0,
   "RIGHT":board.D27,
   #"RIGHT_led": 0,

   # Buttons
   # You can set NeoPixel LED index number with "~_led" parameter :
   #   5-4-3-
   #   0-1-2-
   # comment out anything if you don't need
   # 사용할 버튼 항목만 주석 삭제 후 설정
   # LED가 있을시 "버튼_led"값으로 번호 설정, 없을시 주석처리하거나 생략
   "A":board.D25,
   "A_led": 0,
   "B":board.D24,
   "B_led": 1,
   "X":board.D15,
   "X_led": 5,
   "Y":board.D18,
   "Y_led": 4,
   "TL":board.D14,
   "TR_led": 3,
   "TR":board.D23,
   "TR_led": 2,
   "START":board.D10,
   #"START_led": 6,
   "SELECT":board.D9,
   #"SELECT_led": 7,
 
   # NeoPixel - WS2812 : D10, D12, D18, D21 pin only
   # 네오픽셀 ws2812b 핀 설정
   # D10, D12, D18, D21만 가능
   "neopixel_pin": board.D21,
   # RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, GREY, WHITE
   # RGB LED Color, must set as many as LED lights you have
   # 버튼 별 기본 색상 설정 *LED 개수 만큼 지정할 것
   "led_color": [GREEN, RED, CYAN, CYAN, YELLOW, BLUE ],
   # Default color for buttons with no assigned color
   "default_color":GREY,
   # LED 밝기 1이 최대
   "led_brightness": 1, # 1 is maximum value
   # 버튼 디밍 단계 (0~255), 높을수록 빨리 꺼짐
   "fadingstep" : 10, # Dimming speed - higher, faster
   # 대기모드 진입 시간 (초)
   "activetime" : 5, # Standby mode entry time(sec)

   # joystick mode - 'axis' or 'hat'
   # 조이스틱 모드 설정 'axis' 또는 'hat'
   "dpad_mode": "hat",
   # Turbo button speed (sec)
   "turbo_speed": 0.04,

}