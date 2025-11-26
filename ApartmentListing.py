from ApartmentListingNode import ApartmentListingNode
from Apartment import Apartment


class ApartmentListing:
    def __init__(self):
        self.root = None  # empty BST

    def add_apartment(self, apartment: Apartment):
        if self.root is None:
            self.root = ApartmentListingNode(apartment)
        else:
            self._insert(self.root, apartment)

    def _insert(self, node: ApartmentListingNode, apartment: Apartment):
        
        if apartment.location.upper() == node.location and apartment.size == node.size:
            node.apartments.append(apartment)
            return

        
        if (apartment.location.upper(), apartment.size) < (node.location, node.size):
            if node.left is None:
                node.left = ApartmentListingNode(apartment)
                node.left.set_parent(node)  # ensure parent linkage
            else:
                self._insert(node.left, apartment)
        else:
            if node.right is None:
                node.right = ApartmentListingNode(apartment)
                node.right.set_parent(node)
            else:
                self._insert(node.right, apartment)

    def does_apartment_exist(self, apartment: Apartment) -> bool:
        node = self._find_node(self.root, apartment.location, apartment.size)
        if node is None:
            return False
        return any(apartment == a for a in node.apartments)

    
    def _find_node(self, node: ApartmentListingNode | None, location: str, size: int):
        if node is None:
            return None
        if location.upper() == node.location and size == node.size:
            return node
        if (location.upper(), size) < (node.location, node.size):
            return self._find_node(node.left, location, size)
        return self._find_node(node.right, location, size)

    
    def _traverse(self, node, order: str) -> list[str]:
        
        if node is None:
            return []

        left  = self._traverse(node.left,  order)
        mid   = [str(ap) for ap in node.apartments]   # already 1‑line each
        right = self._traverse(node.right, order)

        if order == "inorder":
            return left + mid + right
        if order == "preorder":
            return mid + left + right
        if order == "postorder":
            return left + right + mid
        return []
    
    def inorder(self) -> str:
        result = self._traverse(self.root, "inorder")
        return "\n".join(result) + ("\n" if result else "")

    def preorder(self) -> str:
        result = self._traverse(self.root, "preorder")
        return "\n".join(result) + ("\n" if result else "")

    def postorder(self) -> str:
        result = self._traverse(self.root, "postorder")
        return "\n".join(result) + ("\n" if result else "")



    
    def get_best_apartment(self, location: str, size: int):
        node = self._find_node(self.root, location, size)
        if node is None:
            return None
        return max(node.apartments, key=lambda a: (a.bedrooms, a.rent))

    def get_worst_apartment(self, location: str, size: int):
        node = self._find_node(self.root, location, size)
        if node is None:
            return None
        return min(node.apartments, key=lambda a: (a.bedrooms, a.rent))

    
    def get_total_listing_price(self):
        return self._sum_rent(self.root)

    def _sum_rent(self, node: ApartmentListingNode | None) -> int:
        if node is None:
            return 0
        total_here = sum(a.rent for a in node.apartments)
        return total_here + self._sum_rent(node.left) + self._sum_rent(node.right)
