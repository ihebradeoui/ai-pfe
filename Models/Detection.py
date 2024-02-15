from datetime import datetime
import string

from Models.Suspect import Suspect


class Detection:
    Id : string
    Time : datetime    
    def __init__(self,id,time) -> None:
        self.Id=id
        self.Time=time