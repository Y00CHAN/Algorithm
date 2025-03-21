'''

if __name__ == '__main__'

파이썬 소스코드에 많이 등장
참조 :
https://medium.com/@chullino/if-name-main-%EC%9D%80-%EC%99%9C-%ED%95%84%EC%9A%94%ED%95%A0%EA%B9%8C-bc48cba7f720

'''


# 한번 실행해보세용 ㅋ

def main():
    meow(3)

def meow(n):
    for i in range(n):
        print('meow')

main()  # 당연히 실행 됨

if __name__ == '__main__':  # 실행 됨
    main()

if __name__ == '__meow__':  # 실행 안됨
    meow(3)

if __name__ != '__main__':  # 실행 안됨
    main()

if not __name__ != '__main__':  # 실행 됨
    main()


