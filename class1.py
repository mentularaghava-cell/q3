class Pirate:
   def __init__(self,name,team):
      self.name = name
      self.team = team

   def __str__(self):
      return f"name {self.name},team {self.team}"
   
   @classmethod
   def get(cls):
      name = input("Name: ")
      team = input("Team: ")
      return cls(name,team)
   
def main():
   pirate = get_pirate()
  
   print(pirate)

def get_pirate():
    name = input("Name: ")
    team = input("Team: ")
    return Pirate(name,team)


if __name__ == "__main__":
   main()
