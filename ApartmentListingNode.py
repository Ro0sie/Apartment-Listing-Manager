
from Apartment import Apartment

class ApartmentListingNode:
    def __init__(self,apartment):
        self.location = apartment.location
        self.size = apartment.size
        self.apartments = [apartment]

        self.parent = None
        self.left = None
        self.right = None

    def get_location(self):
        return self.location
    def get_size(self):
        return self.size
    def get_parent(self):
        return self.parent
    def set_parent(self, parent):
        self.parent = parent
    def get_left(self):
        return self.left 
    def set_left(self,left):
        
        self.left = left
        if left is not None:
            left.set_parent(self)
            
    def get_right(self):
        return self.right
    def set_right(self,right):
        
        self.right = right
        if right is not None:
            right.set_parent(self)
    def get_apartments(self):
        #apartment = []
        return self.apartments
    def __str__(self):
        return '\n'.join(str(apt) for apt in self.apartments) + "\n"
