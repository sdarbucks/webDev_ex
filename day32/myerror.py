# 예외 클래스 (Writing Exception Classes) - 파이썬 내장 클래스

class MyError(Exception):
    def __str__(self):  # 문자로 리턴해줌
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == "바보":
        raise MyError() # raise 에러 - 일부러 에러를 발생시켜야 하는 경우
    print(nick)

"""
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
"""
try:
    say_nick('Hero')
    say_nick('angel')
    say_nick('바보')
except MyError as e:    # e - exception
    print(e)
