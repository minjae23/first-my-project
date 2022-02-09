names=["민재","태준","태현","동욱"]
i=0
while (i<4):
    file_name=open("C:/PYTHON/{0}.txt".format(names[i]),'w')
    a=("[메일 본문] \n 안녕하세요?{0} 님.\n 나도출판~~ 중입니다\
        {1}님의 유튜브~".format(names[i],names[i]))
    i +=1
    file_name.write(a)
file_name.close()   