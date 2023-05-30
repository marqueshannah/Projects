# Inventory Report
## Description:
This project is a Java program that processes inventory data and generates an inventory report. The program reads data from two input files: items.txt and activity.txt. It performs various operations based on the activity records and updates the inventory accordingly. Finally, it creates an inventory report file containing the updated inventory information.

### How to Use:
1. Clone the repository to your local machine:

`git clone https://github.com/<username>/<repository>.git`

2. Compile the Java source code:
`javac HMProjectThree.java`

3. Run the program:

`java HMProjectThree`

4. Follow the prompts to enter the file paths for items.txt, activity.txt, and the desired path for the report file.

5. The program will process the input files, update the inventory, and generate the inventory report.

6. The inventory report will be saved to the specified report file path.

## Sample Output:

```
Enter items file path: 
[Local Machine Path]\...\items.txt
15 inventory items have been created
Enter activity file path:
[Local Machine Path]\...\activity.txt
Bad Transaction Code: X in record 5
insert path for report:
[Local Machine Path]\...\report.txt
14 records processed; 1 records skipped
7 inventory item quantity transactions
Total Inventory Value is $10,944.13
```
# Sample report.txt

```
								John Smith for the Ragnarok Company, Inc.
							Prepared On : Friday, June 25, 2021 15:52:09

							 I N V E N T O R Y   R E P O R T

Item Inventory
Number                    Description                            Quantity          Unit Price                    Value
90000      4 inch by 1/2 inch Spring                                  55                6.25                    343.75
20001      6 inch by 1/2 inch Spring                                  15                8.95                    134.25
20000                  Torque Wrench                                  37                29.5                   1,091.5
28967                     Hex Wrench                                  70               19.98                   1,398.6
90909                Wide Paintbrush                                 107               17.45                  1,867.15
56789           Phillips Screwdriver                                 120               10.95                     1,314
66908                  14 inch Level                                  23               16.89                    388.47
24680                    Claw Hammer                                  55               15.98                     878.9
29037              1 inch Paintbrush                                  73                2.95                    215.35
89999                       Fly Trap                                  10                5.95                      59.5
12345                Ballpeen Hammer                                  55               18.75                  1,031.25
44021                  3 inch Trowel                                  38               10.74                    408.12
30127                 1/4 inch Drill                                  16               34.89                    558.24
32678                  Clorox Wipes                                  35                7.95                    278.25
13579                     Box Wrench                                  48               20.35                     976.8
                                                                                                       Total: 10,944.13
```
