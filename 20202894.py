print("갤러그 게임 시작")
print("적 비행기 발생")



for i in range(5):
    
    print("----------------------------------")
    print("1. 발사 2. 오른쪽이동 3. 왼쪽이동 ")
    print("----------------------------------")
    number = int(input("숫자를 입력하세요: "))


    player = ["총알 발사", "오른쪽", "왼쪽"]
    
    if number == 1:
        print(player[0])

    if number == 2:
        print(player[1])
        
    if number == 3:
        print(player[2])

print("----------------------------------")
print("            보스 등장")


for i in range(8):
    print("----------------------------------")
    print("1. 발사 2. 오른쪽이동 3. 왼쪽이동 ")
    print("----------------------------------")
    number = int(input("숫자를 입력하세요: "))

    player_1 = {"1" : "총알 발사", "2" : "오른쪽", "3" : "왼쪽"}
    
    if number == 1:
        print(player_1["1"])
        
    if number == 2: 
        print(player_1["2"])
        
    if number == 3:
        print(player_1["3"])

print("----------------------------------")
print("               실패")
print("----------------------------------")
