from Apartment import Apartment
from ApartmentListingNode import ApartmentListingNode
from ApartmentListing import ApartmentListing

def test_apartment_init_and_str():
    apt = Apartment("Downtown", 750, 2, 1500)
    assert apt.location == "DOWNTOWN"
    assert str(apt) == "Location: DOWNTOWN, Size: 750 sqft, Bedrooms: 2, Rent: $1500"
      
def test_apartment_eq_and_ne():
    a = Apartment("City", 700, 2, 2000)
    b = Apartment("City", 700, 2, 2000)
    c = Apartment("City", 700, 2, 2100)
    assert a == b
    assert a != c

def test_apartment_gt_hierarchy():
   
    a = Apartment("Alpha", 700, 2, 1500)
    b = Apartment("Beta",  700, 2, 1500)
    assert b > a and not (a > b)

 
    c = Apartment("City", 600, 2, 1500)
    d = Apartment("City", 800, 2, 1500)
    assert d > c


    e = Apartment("Town", 700, 1, 1500)
    f = Apartment("Town", 700, 3, 1500)
    assert f > e


    g = Apartment("Village", 700, 2, 1000)
    h = Apartment("Village", 700, 2, 2000)
    assert h > g

def test_node_left_right_parent_setters():
   
    root = ApartmentListingNode(Apartment("Root", 700, 2, 1500))
    left_child  = ApartmentListingNode(Apartment("Left", 600, 1, 1200))
    right_child = ApartmentListingNode(Apartment("Right", 800, 1, 1800))

    root.set_left(left_child)
    root.set_right(right_child)

    assert root.get_left()  is left_child
    assert root.get_right() is right_child


    assert left_child.get_parent()  is root
    assert right_child.get_parent() is root

def test_search_and_existence():
    listing, (dt1, _, _) = build_listing()
    assert listing.does_apartment_exist(dt1)

    missing = Apartment("Nowhere", 600, 1, 500)
    assert not listing.does_apartment_exist(missing)

    if hasattr(listing, "search_apartment"):
        assert listing.search_apartment("DOWNTOWN", 700) is not None
        assert listing.search_apartment("NOWHERE", 600) is None

def build_listing():
   
    listing = ApartmentListing()
    dt1 = Apartment("Downtown", 700, 2, 1200)
    dt2 = Apartment("Downtown", 700, 3, 2000)
    sb  = Apartment("Suburbs",  800, 1, 1500)

    for ap in (dt1, dt2, sb):
        listing.add_apartment(ap)

    return listing, (dt1, dt2, sb)

def test_insert_and_find_node():
    listing, (dt1, _, _) = build_listing()
    node = listing._find_node(listing.root, "DOWNTOWN", 700)
    assert node is not None
    assert any(ap == dt1 for ap in node.apartments)

def test_best_and_worst():
    listing, (dt1, dt2, _) = build_listing()
    best  = listing.get_best_apartment("downtown", 700)
    worst = listing.get_worst_apartment("Downtown", 700)

    assert best  == dt2   
    assert worst == dt1    

def test_total_price_and_traversals():
    listing, (dt1, dt2, sb) = build_listing()

    
    assert listing.get_total_listing_price() == dt1.rent + dt2.rent + sb.rent

    # inorder & preorder 
    inorder_lines  = listing.inorder().strip().split("\n")
    preorder_lines = listing.preorder().strip().split("\n")
    assert len(inorder_lines) == 3
    assert len(preorder_lines) == 3

    
    if hasattr(listing, "postorder"):
        postorder_lines = listing.postorder().strip().split("\n")
        assert len(postorder_lines) == 3

def test_apartment_lt_branching():
    
    smaller_size = Apartment("City", 600, 2, 1500)
    larger_size  = Apartment("City", 800, 2, 1500)
    assert smaller_size < larger_size and not (larger_size < smaller_size)

    
    fewer_beds = Apartment("City", 700, 1, 1500)
    more_beds = Apartment("City", 700, 3, 1500)
    assert fewer_beds < more_beds and not (more_beds < fewer_beds)

    
    cheaper = Apartment("City", 700, 2, 1200)
    pricier = Apartment("City", 700, 2, 1500)
    assert cheaper < pricier and not (pricier < cheaper)

def test_listingnode_getters_and_str():
    apt  = Apartment("Beach", 500, 1, 1000)
    node = ApartmentListingNode(apt)

    assert node.get_location() == "BEACH"
    assert node.get_size() == 500
    assert node.get_apartments() == [apt]
    
    assert str(node).strip() == str(apt)

def test_insert_and_traverse_complex_tree():
    lst = ApartmentListing()
    root = Apartment("M", 600, 2, 1500)   
    left = Apartment("L", 600, 2, 1500)   
    right = Apartment("Z", 600, 2, 1500)  
    left_deeper = Apartment("K", 600, 2, 1500)  

    
    for apt in (root, right, left, left_deeper):
         lst.add_apartment(apt)

    #assert lst.root.left.location == "L"
    #assert lst.root.left.left.location == "K"
    #assert lst.root.right.location == "Z"

    
    assert lst.root.left.parent is lst.root
    assert lst.root.right.parent is lst.root

    
    for traversal in (lst.inorder, lst.preorder, lst.postorder):
        assert len(traversal().strip().split("\n")) == 4

def test_best_and_worst_apartment_paths():
    lst = ApartmentListing()
    a1 = Apartment("Place", 500, 1, 1000)  
    a2 = Apartment("Place", 500, 3,  900)  
    a3 = Apartment("Place", 500, 2,  950)

    for apt in (a1, a2, a3):
        lst.add_apartment(apt)

    assert lst.get_best_apartment("Place", 500)  is a2
    assert lst.get_worst_apartment("Place", 500) is a1

    
    assert lst.get_best_apartment("Nowhere", 999)  is None
    assert lst.get_worst_apartment("Nowhere", 999) is None

def test_insert_right_recursion():
    lst = ApartmentListing()

    root = Apartment("M", 600, 2, 1500)   
    first_right = Apartment("Z", 600, 2, 1500)   
    second_right = Apartment("ZZ", 600, 2, 1500)  

    for apt in (root, first_right, second_right):
        lst.add_apartment(apt)

   
    assert lst.root.right.right is not None
    assert lst.root.right.right.parent is lst.root.right
    assert lst.root.right.right.location == "ZZ"
    
    #inorder_lines = lst.inorder().splitlines()
    #assert len(inorder_lines) == 3, "Incorrect inorder traversal"
    
def test_apartment_lt_location_comparison():
    """Covers Apartment.__lt__ branch where locations are different"""
    a = Apartment("Alpha", 700, 2, 1500)
    b = Apartment("Beta", 700, 2, 1500)
    assert a < b
    assert not (b < a)

def test_apartmentlisting_traverse_invalid_order():
    """Covers ApartmentListing._traverse branch where order is invalid"""
    listing = ApartmentListing()
    apt = Apartment("Test", 700, 2, 1500)
    listing.add_apartment(apt)
    result = listing._traverse(listing.root, "unknown_order")
    assert result == []  # should gracefully return empty list