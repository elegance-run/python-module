#面向对象编程过程：

class Student(object):#括号内是该被定义类的所继承的类；
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_name_score(self):#得到对象的姓名和分数；
        print('%s:%s' %(self.name,self.score))

    def get_grade(self):#获取对象的分数所属的等级；
        if self.score>=90 and self.score<=100:
            return 'A'
        elif self.score>=60 and self.score<90:
            return 'B'
        else:
            return 'C'



if __name__=='__main__':
    bart = Student('Bart Tompson', 59)
    lisa = Student('Lisa Tompson', 87)

    bart.print_name_score()
    print('Grade of bart:',bart.get_grade())
    lisa.print_name_score()
    print('Grade of lisa:',lisa.get_grade())
    print(bart.name)