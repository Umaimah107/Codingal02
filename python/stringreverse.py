class String:
    def __init__(self,string1):
        self.string1 = string1

    def reverse_string(self): 
        return self.string1[::-1]

s = String(" I love to code")
print("Original text: ",s.string1)
print("Reversed:", s.reverse_string())
