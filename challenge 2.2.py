# Python Program to depict multiple inheritance
# when method is overridden in both classes

class Class1:
  def m(self):
    print("In Class1") 

class Class2(Class1):
  def m(self):
    print("the blowers are bowling the batman are bating")

class Class3(Class1):
  def m(self):
    print("In Class3") 

class Class4(Class2, Class3):
  pass

obj = Class4()
obj.m()
