#include <iostream>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

//Create Address class 
class Address {
private:
    //coordinates of the houses. x => i, j => y
    double x, y;
    //Last possible date for delivery
    string last_day_of_delivery;
public:
    //Default constructor
    Address() {};

    //Overload constructor to get information of (x, y)
    Address(double x_inputted, double y_inputted) {
        x = x_inputted;
        y = y_inputted;
    };

    //Overlaod Constructor with information about the last day for delivery
    Address(double x_inputted, double y_inputted, string date) {
        x = x_inputted;
        y = y_inputted;
        last_day_of_delivery = date;
    };

    //Destructor
    ~Address() {};

    //Methods that return the private members
    double getCoordinate_x() const {
        return x;
    };
    double getCoordinate_y() const {
        return y;
    };
    string getLastDayforDelivery() const {
        return last_day_of_delivery;
    }

    //Methods
        //Find the distance between the points
    double distance(Address addy2) {
        return sqrt(pow((addy2.y - y), 2) + pow((addy2.x - x), 2));
    };

    //Method that will print the specific address
    void print_out_address_coordinates() {
        cout << "( " << x << "," <<
            y << " )";
    };

};

//Create a new address called "AddressLists"
class AddressLists : public Address {
private: //data members
    //Vector of address that contain all the addresses
    vector<Address> list_of_address;

public: //methods
    //Default constructor 
    AddressLists() {};

    //Deconstructor
    ~AddressLists() {};

    //Methods that return private methods
    vector<Address> return_list_of_all_addresses() {
        return list_of_address;
    };

    //Methods
        //Adding addresses into the list vector
    void add_address(Address inputted_addy) {
        list_of_address.push_back(inputted_addy);
    };

    //Counting the number of address are in the list
    int num_of_address() {
        return list_of_address.size();
    };

    //Find the distance between the points
    double dis_btw_2_addys(Address addy1, Address addy2) {
        return sqrt(pow((addy2.getCoordinate_y() - addy1.getCoordinate_y()), 2)
            + pow((addy2.getCoordinate_x() - addy1.getCoordinate_x()), 2));
    };

    //The total distance that you need to travel
    double length() {
        //variables
        int size = list_of_address.size();
        double length = 0;

        //Loop through the list to find total distance 
        for (int i = 0; i < size - 1; i++) {
            int j = i + 1;
            length += dis_btw_2_addys(list_of_address[i], list_of_address[j]);
        }

        return length;
    };

    //Method that checks if the addresses are the same location
    bool same_address_location(Address addy1, Address addy2) {
        bool is_same_address = false;
        if (addy1.getCoordinate_x() == addy2.getCoordinate_x() &&
            addy1.getCoordinate_y() == addy2.getCoordinate_y()) {
            is_same_address = true;
        }
        return is_same_address;
    };

    //Method that will print the specift address
    void print_out_address_from_list(Address target) {
        cout << "( " << target.getCoordinate_x() << "," <<
            target.getCoordinate_y() << " )";
    };

    //Method that will print out all the addresses on the list in order
    void print_all_address_in_list() {
        int size = num_of_address();
        cout << "The whole list of address is: ";
        for (int i = 0; i < size; i++) {
            print_out_address_from_list(list_of_address[i]);
            cout << " ";
        }

        cout << endl << endl;
    };

    //Method to find the location of that address on the 'AddressLists'
    int index_address(Address target, bool looking_for_2nd_depot = false) {
        //size of vector
        int size = num_of_address(), i, j;
        int depot_count = 0;

        //WHen trying to find the index of the second depot we will use this method but we will add 'true' at end
        if (looking_for_2nd_depot) {
            for (j = 0; j < size; j++) {
                if (same_address_location(target, list_of_address[j])) {
                    depot_count++;
                    if (depot_count == 2) {
                        break;
                    }
                }
            }
        }
        else {
            //This is the index finder to an element that is not the second depot
            for (i = 0; i < size; i++) {
                if (same_address_location(target, list_of_address[i])) {
                    break;
                }
            }
        }

        if (looking_for_2nd_depot) {
            return j;
        }

        return i;
    };

    //Method that will swap the addresses of the list
    void swap_addresses(Address addy1, Address addy2, bool looking_for_2nd_depot = false) {
        //The driving force behind this method is to find the correct index of the elements we are talking about
        //But the problems we are facing is that when I use the index_address method for the 2nd depot element
        //The index_address method returns the index of the first depot on the list not the second depot.

        //This if statement will let us swap the second depot element with any other element on the list
        if (looking_for_2nd_depot) {
            int index_of_addy1 = index_address(addy1);
            int index_of_2nd_depot = index_address(addy2, true);

            Address temp = list_of_address[index_of_addy1];
            list_of_address[index_of_addy1] = list_of_address[index_of_2nd_depot];
            list_of_address[index_of_2nd_depot] = temp;
        }
        else {
            //This will allow us to swap any element in the list wiht another element
            int index_of_addy1 = index_address(addy1);
            int index_of_addy2 = index_address(addy2);

            Address temp = list_of_address[index_of_addy1];
            list_of_address[index_of_addy1] = list_of_address[index_of_addy2];
            list_of_address[index_of_addy2] = temp;
        }

    };

    //Returns an address on the list closests to another address
    Address index_closest_to(Address target_address, bool is_it_second_iteration = false) {
        //variables
        if (is_it_second_iteration) {
            int size = num_of_address(), index_of_adress_closest_to_target = 1;
            double distance = dis_btw_2_addys(target_address, list_of_address[1]);

            //Cycle through the list for find the address that is closer to the target address
            for (int j = 2; j < size - 1; j++) {
                if (dis_btw_2_addys(target_address, list_of_address[j]) < distance) {
                    distance = dis_btw_2_addys(target_address, list_of_address[j]);
                    index_of_adress_closest_to_target = j;
                }
            }

            Address closer_address(list_of_address[index_of_adress_closest_to_target]);

            return closer_address;

        }
        else {
            int size = num_of_address();
            int index_of_target = index_address(target_address), index_of_adress_closest_to_target = 1;

            //Swapping the 'target address' with the first element
            if (index_of_target != 0) {
                swap_addresses(target_address, list_of_address[0]);
            }

            //Distance variable 
            double distance = dis_btw_2_addys(list_of_address[0], list_of_address[1]);

            //Cycle through the list to find the address that is closer to the target address
            for (int j = 2; j < size - 1; j++) {
                if (dis_btw_2_addys(list_of_address[0], list_of_address[j]) < distance) {
                    distance = dis_btw_2_addys(list_of_address[0], list_of_address[j]);
                    index_of_adress_closest_to_target = j;
                }
            }
            Address closer_address(list_of_address[index_of_adress_closest_to_target]);

            return closer_address;
        }
    };

    //Method to get rid of the common address
    void get_rid_of_address(Address address_to_be_deleted) {
        int size = num_of_address();
        for (int i = 1; i < size - 1; i++) {
            if (same_address_location(address_to_be_deleted, list_of_address[i])) {
                swap_addresses(list_of_address[i], list_of_address[size - 1], true);
                list_of_address.pop_back();

                // switching back the second depot to the end of the list
                size = num_of_address();
                swap_addresses(list_of_address[size - 1], list_of_address[i], true);
            }
        }
    }

    //Method to get the fastest route starting at the depot and ending at the depot.
    vector<Address> greddy_route() {
        //Varibles
        vector<Address> answer;
        Address depot = list_of_address[0], index_closest;
        Address point_of_reference = depot;
        int size = num_of_address(), i = 0;

        //Starts at the depot
        answer.push_back(depot);

        //Since we dont know the actual size since it is changing in length
        for (int i = 1; i < size - 1; i++) {
            if (i > 1) {
                point_of_reference = index_closest;
                index_closest = index_closest_to(point_of_reference, true);
                answer.push_back(index_closest);


            }
            else {
                index_closest = index_closest_to(point_of_reference);
                answer.push_back(index_closest);

            }
            get_rid_of_address(index_closest);
            point_of_reference = index_closest;
        }

        //goes back to the depot
        answer.push_back(depot);

        //Returning the answer    
        return answer;
    };

};

int main() {
    //Creating object of class 'Address'
    Address depot(0., 0.), one(0., 5.), two(5., 0.), three(5., 5.), temp;

    //Creating a vector of addresses
    vector<Address> list1, list2;
    list1 = { depot, one, two, three, depot };
    int size1 = list1.size();


    //Create an object of 'AddressLists'
    AddressLists list;
    AddressLists greedy_route;

    //loop through 'list1' of address and adding them to 'list'
    for (int i = 0; i < size1; i++) {
        list.add_address(list1[i]);
    }

    //The list order
    cout << "The coordinates of the list is: ";
    list.print_all_address_in_list();


    //The total distance following the route order
    cout << "The total distance following the route order from above is: "
        << list.length() << endl << endl;

    //This is to find the greedy_route
        //List 2 contains the greddy route
    list2 = list.greddy_route();
    int size2 = list2.size();
    for (int i = 0; i < size2; i++) {
        greedy_route.add_address(list2[i]);
    }
    cout << "The optimal route to deliver is: ";
    greedy_route.print_all_address_in_list();

    cout << "The total distance following the route order from above is: "
        << greedy_route.length() << endl << endl;


    return 0;
}
