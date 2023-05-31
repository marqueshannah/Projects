# Amazon Truck Driver Program
This program simulates a delivery route optimization for an Amazon truck driver. It calculates the optimal route for delivering packages based on the addresses provided. The program utilizes classes and methods to organize and manipulate the addresses effectively.

## Table of Contents
- Address Class
- AddressLists Class
- Main Function
- Address Class

### The Address class represents a single address. It has the following attributes:

x: x-coordinate of the address
y: y-coordinate of the address

last_day_of_delivery: last possible date for delivery

#### Methods
```
getCoordinate_x(): Returns the x-coordinate of the address.

getCoordinate_y(): Returns the y-coordinate of the address.

getLastDayforDelivery(): Returns the last possible date for delivery of the address.

distance(addy2): Calculates and returns the distance between two addresses.

print_out_address_coordinates(): Prints the coordinates of the address.
```
### AddressLists Class

The AddressLists class extends the Address class and represents a collection of addresses. It includes additional functionality for managing and manipulating the list of addresses.

#### Methods
```
return_list_of_all_addresses(): Returns the list of all addresses.

add_address(inputted_addy): Adds an address to the list.

num_of_address(): Returns the number of addresses in the list.

dis_btw_2_addys(addy1, addy2): Calculates and returns the distance between two addresses.

length(): Calculates and returns the total distance of the delivery route.

same_address_location(addy1, addy2): Checks if two addresses have the same location.

print_out_address_from_list(target): Prints the coordinates of a specific address in the list.

print_all_address_in_list(): Prints all addresses in the list in order.

index_address(target, looking_for_2nd_depot = false): Finds the index of an address in the list.

swap_addresses(addy1, addy2, looking_for_2nd_depot = false): Swaps the positions of two addresses in the list.

index_closest_to(target_address, is_it_second_iteration = false):

```
