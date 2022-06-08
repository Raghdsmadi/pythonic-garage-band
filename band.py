from abc import abstractmethod

class Musician:
    def __init__(self):
        self.name = ""
        self.instrument = ""
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def playsolo(self):
        pass

class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "guitar"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return 'face melting guitar solo'



class Drummer(Musician):
    def __init__(self , name):
        self.name = name
        self.instrument = "drums"

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "rattle boom crash"


class Bassist(Musician):
    """
    It is a sub class that creates a musician that can play bass
    """

    def __init__(self, name):
        self.name = name
        self.instrument = "bass"

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "bom bom buh bom"

class Band:

    name, members, instances = "" ,[] ,[]
    def __init__(self, name , members):
        # name, members = "", []
        self.name = name
        self.members= members
        Band.instances.append(self)

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


    def play_solos(self):
        return[member.play_solo() for member in self.members]

    @classmethod
    def to_list(cls):
        return cls.instances


  # return "metal solo? bom buh bom buh"



