class CGPA:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __gt__(self, other):
        self_mag = ((self.x) + (self.y))/2
        other_mag = ((other.x) + (other.y))/2
        return self_mag > other_mag

s1 = CGPA(10,10)
s2 = CGPA(9.5,10)
s3 = CGPA(9.9,9.9)
print(s1>s2)
print(s2>s3)
print(s1>s3)
