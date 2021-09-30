# 다중 예외 - except를 여러번 사용
try:
    data = [59, 0, 4, 116, 303]
    x = input("▶ 0~4까지의 인덱스를 입력해 주세요.(인덱스 값에 대응하는 값을 호출합니다) : ")
    num = int(x)
    print(data[num])
except IndexError as exception1:
    print("▶ 리스트 인덱스가 범위를 초과했습니다.")
except ValueError as exception2:
    print("▶ 정수가 아닌 잘못된 값이 입력되었습니다.")
