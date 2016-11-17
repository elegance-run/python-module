import types
'''def fn():
    pass

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

print('type(\'abc\')==str?', type('abc')==str)
'''

#attribution;

'''class MyObject(object):
    def __init__(self):
        self.x=9

    def power(self):
        return self.x*self.x

if __name__=='__main__':
    obj = MyObject()
    print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))
    print('hasattr(obj,\'y\')=',hasattr(obj,'y'))
    setattr(obj,'y',19)
    print('hasattr(obj,\'y\')=', hasattr(obj, 'y'))
    print('getattr(obj,\'y\')=',getattr(obj,'y'))
'''


#实例属性和类属性；
class Student(object):
    student_number='1120160685'

    def __init__(self,name):
        self.name=name

def register(name,**kw):
    a=Student(name)
    for k,v in kw.items():
        setattr(a,k,v)
    Student.student_number=+1
    return a

if __name__=='__main__':
    bos = register('Bos', score=90)
    lisa = register('Lisa', score=100)
    print('name of lisa is:',getattr(lisa,'name'))