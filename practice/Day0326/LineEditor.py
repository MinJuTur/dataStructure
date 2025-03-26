from practice.Day0324.ListByClass import ArrayList

list = ArrayList()
while True:
    commmand = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=> ")

    if commmand == 'i': # 입력
        pos = int(input(" 입력행 번호: "))
        str = input(" 입력행 내용: ")
        list.insert(pos, str)
    elif commmand == 'd': # 삭제
        pos = int(input(" 삭제행 번호: "))
        list.delete(pos)
    elif commmand == 'r': # 변경
        pos = int(input(" 변경행 번호: "))
        str = input(" 변경행 내용: ")
        list.delete(pos)
        list.insert(pos, str)
    elif commmand == 'p': # 출력
        print("Line Editor")
        for i in range(list.size):
            print("[ %d] " % i, list.array[i])
    elif commmand == 'l': # 파일읽기
        with open("text.txt", "r", encoding="utf-8") as file:
            #list = ArrayList() 모르겠다..
            i = 0
            for line in [line.strip() for line in file.readlines()]: # 모든 줄을 리스트로 반환, 줄바꿈 제거
                list.insert(i, line)
                i += 1
            print("Line Editor")
            for i in range(list.size):
                print("[ %d] " % i, list.array[i])
    elif commmand == 's': # 저장
        with open("text.txt", "w", encoding="utf-8") as file:
            for i in range(list.size):
                file.writelines(list.array[i] + "\n")
    elif commmand == 'q': # 종료
        break


