# barambot
바람의나라:연 자동사냥 챗봇 v0.1

1.사전준비

    1-1.바람의 나라 연 LD플레이어, 녹스 같은 시뮬레이터에서 동작.
    1280X720 크기로 실행 후 좌측상단에 옮겨두기 (화면검사영역)
    https://kr.bignox.com/
    https://kr.ldplayer.net/

    1-2.파이참 개발환경 구축
    https://steemit.com/kr-dev/@maanya/3ajlbo

    1-3. 챗봇 만들기
    https://steemit.com/kr-dev/@maanya/30

    => 여기서 만들어진 챗봇의 token를 복사하여 config.py의 token에 입력한 뒤, 해당 챗봇을 검색해서 아무말이나 걸고
    python3 init_gamebot.py 실행 후, 파이참 인터프리터 출력에 나오는 ID 부분을 config.py에 입력합니다.

2.실행

    python3 gamebot.py 실행합니다.

    챗봇상에서 명령어는 다음과 같습니다.

    /screen : 현재 스크린샷 전송
    /monitor : 사망, 내구도 하락상태 확인후 보고 (1초에 한번씩 동작)
    /exp : 현재 십억경 부분의 이미지 전송 

3.주의사항

    3-1. 개개인마다 화면 출력값이 다를수 있기 때문에 /monitor 아래에서 뜨는 값을 보고 config.py의 
    die_th =  61485224 , repair_th = 6500000 이 부분을 수정해야함 (해당 값보다 크면 죽었다 혹은 수리를 해야된다고 판단)
    => 직접 죽거나 내구도 부족한 이미지를 구해서 어느정도의 값이 나오는지 확인 필요.
    (출력예시)
    die 57095944.0 (971, 417)
    repair 9859148.0 (331, 284)


    3-2. 인식이 잘 되지 않는 경우에 imgs/ 아래의 파일 수정 필요, 직접 사용하는 환경에서 스크린샷을 만들어서 사용하는게 좋음
    EXP_GT = 'imgs/exp.png'
    DIE_GT = 'imgs/die2.png'
    REPAIR_GT = 'imgs/repair.png'

    3-3. 현재 화면인식 영역은 (0,0) ~ (1280,720) 해상도 영역입니다. 해당 영역에 게임화면이 위치하지않으면 동작하지 못합니다.
    바꾸고 싶으시면 baram.py의  pyautogui.screenshot 부분을 직접 수정하여야 합니다.



