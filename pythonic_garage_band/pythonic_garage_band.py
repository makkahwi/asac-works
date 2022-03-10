from abc import ABC,abstractmethod

class Band:
  instances = []

  def __init__(self,name,members):
    self.name = name
    self.members = members
    Band.instances.append(self)
  
  def play_solos(self):
    solos = []

    for member in self.members:
      solos.append(member.play_solo())

    return solos

  @classmethod
  def to_list(cls):
    return cls.instances

  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name

class Musician(ABC):
  def __init__(self,name) :
      self.name=name

  @abstractmethod
  def play_solo():
    pass

  def get_instrument():
    pass

class Guitarist(Musician):
  def get_instrument(self):
    return "guitar"

  def play_solo(self):
    return "face melting guitar solo"
    
  def __str__(self):
    return f'My name is {self.name} and I play {self.get_instrument()}'
    
  def __repr__(self):
    return f'{self.__class__.__name__} instance. Name = {self.name}'

class Bassist(Musician):
  def get_instrument(self):
    return "bass"

  def play_solo(self):
    return "bom bom buh bom"

  def __str__(self):
    return f'My name is {self.name} and I play {self.get_instrument()}'
    
  def __repr__(self):
    return f'{self.__class__.__name__} instance. Name = {self.name}'

class Drummer(Musician):
  def get_instrument(self):
    return "drums"

  def play_solo(self):
    return "rattle boom crash"

  def __str__(self):
    return f'My name is {self.name} and I play {self.get_instrument()}'
    
  def __repr__(self):
    return f'{self.__class__.__name__} instance. Name = {self.name}'