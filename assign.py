class information:
    def __init__(self,name,number,sex):
        self.name=name
        self.number = number
        if sex=="male" or sex=="female":
            self.sex = sex
        else:
            self.sex = "unknown"
     
    def result(self):
     
        return "이름은 %s, "%self.name + "전화번호는%s, "%self.number+ "성별은%s. "%self.sex
dic ={}
i=1
while(True):
    name = input("이름을 입력하세요 : ")
    if name != "그만" :
        number =input("전화번호를 입력하세요 : ") 
        sex = input("성별을 입력하세요 : ") 
        person = information(name,number,sex)
        dic[i] = person.result()
        i=i+1
        for val in dic.values():
            print(val) 
       
    else:
        for val in dic.values():
            print(val) 
        break