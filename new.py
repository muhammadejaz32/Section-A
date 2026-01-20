list1  =[ 1,3,4]
string  = "ahmad"

print(len(list1))
print(len(string))


class student:
    def marks(self, sub1, sub2):
        self.sub1  = sub1
        self.sub2  =sub2
        print(self.sub1+self.sub2)
        print("parent class")

class stude(student):
    def marks(self, sub1, sub2):
        super().marks(10,12)
        self.sub1  = sub1
        self.sub2  =sub2
        print(self.sub1+self.sub2)
        print("child class")

st2  =stude()
st2.marks(10,34)