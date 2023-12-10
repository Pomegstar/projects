class person:
 def __init__(self, first_name, last_name, gender, address):
    self.firstname = first_name
    self.lastname = last_name
    self.gen = gender
    self.add = address
 def describe_user(self):
   print(f"{self.firstname} {self.lastname} lives in {self.add}")
p1 = person( "abul", "hasan", "male", "dhaka")
p3 = person("jhsk", "sjhd", "jlk", "jx")
p1.describe_user()
p3.describe_user()
if p1 == p3:
  print("they are the same person")
else:
  print("they are not the same person")