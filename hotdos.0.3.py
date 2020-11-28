print("made in hotdog union version[0.3]")
hotdos_date = open("hotdos_date/name.txt", "r",)
hotdos_name = hotdos_date.readline()
hotdos_date.close()
print(hotdos_name, "실행 성공")
while True:
    if hotdos_name == "no date":
        print("당신의 이름은 무엇입니까?")
        console = input(">>>")
        hotdos_date = open("hotdos_date/name.txt", "w",)
        hotdos_date.write(console)
        hotdos_name = hotdos_date
        hotdos_date.close()
    console = input("---명령어---\nhtds name-내이름\nhtds r (file(first))\nfile - 파일 보기\nhtds w (file(first)) - 내용덮어쓰기\n>>>")
    if console == "htds name":
        print(hotdos_name)
    if console == "htds r first":
        hotdos_date = open("hotdos_date/first.txt", "r", encoding='UTF-8')
        while 1 :
            line = hotdos_date.readline()
            if not line:
                break
            
            print(line)
        hotdos_date.close()
    if console == "htds w first":
        hotdos_date = open("hotdos_date/first.txt", "w", encoding='UTF-8')
        hotdos_date.write(input("덮어쓸 내용을 적으십시오\n>>>"))
        hotdos_date.close()
        print("save")
        
