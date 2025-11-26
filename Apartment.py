class Apartment:
    def __init__(self,location = None,size = 0,bedrooms = 0,rent = 0):
        self.location = location.upper()
        self.size = size
        self.bedrooms = bedrooms
        self.rent = rent

    def __gt__(self,rhs):
        if self.location != rhs.location:
            return self.location > rhs.location
        if self.size != rhs.size:
            return self.size > rhs.size
        if self.bedrooms != rhs.bedrooms:
            return self.bedrooms >rhs.bedrooms
        return self.rent > rhs.rent
    
    def __lt__(self,rhs):
        if self.location != rhs.location:
            return self.location < rhs.location
        if self.size != rhs.size:
            return self.size < rhs.size
        if self.bedrooms != rhs.bedrooms:
            return self.bedrooms <rhs.bedrooms
        return self.rent < rhs.rent
        


    def __eq__(self,rhs):
        return(
        self.location == rhs.location and
        self.size == rhs.size and 
        self.bedrooms == rhs.bedrooms and
        self.rent == rhs.rent
        )
            
    def __str__(self):
        return (
            f"Location: {self.location}, "
            f"Size: {self.size} sqft, "
            f"Bedrooms: {self.bedrooms}, "
            f"Rent: ${self.rent}"
        )
    
           