print("made in hotdog union version(0.2b)")
hotdos_date = open("hotdos_date/name.txt", "r")
hotdos_name = hotdos_date.readline()
hotdos_date.close()
print(hotdos_name, "실행 성공")
while True:
    if hotdos_name == "no date":
        print("당신의 이름은 무엇입니까?")
        console = input(">>>")
        hotdos_date = open("hotdos_date/name.txt", "w")
        hotdos_date.write(console)
        hotdos_name = hotdos_date
        hotdos_date.close()
    console = input("---명령어---\nhtds name-내이름\nhtds see (file)\nfirst\nfile - 파일 보기\n>>>")
    if console == "htds name":
        print(hotdos_name)
    if console == "htds see first":
        hotdos_date = open("hotdos_date/first.txt", "r")
        print(hotdos_date.readline(1), "\n입니다")
        
