import string


class Suspect:
    Id : string
    Name : string
    Location : string 
    Image : string
    
    def __init__(self,id,name,location,image) -> None:
        self.Id=id
        self.Name=name
        self.Location=location
        self.Image=image
        