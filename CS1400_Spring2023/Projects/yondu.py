'''
Project Name: Yondu Udonta
Author: Zachary Peterson
Due Date: 01/20/2023
Course: CS1400-x01

Calculation of loot shares for each crew member under Yondu Udonta from data requested and input by the user.

This set of code shows the understanding of integer arithmetic, conditionals and use of variables
and their correlating values.

For this program to run, you need only run and supply integers as requested from the terminal.
Detailed errors will appear to point out any unusable entries.
'''


def main():
    '''
    Program starts here.
    '''
    try:
        # retrieving data from user for units of loot and crew size and checking it against conditionals
        crew_size = int(input())
        units = int(input())

    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if crew_size < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if crew_size < 3:
        print("Not enough crew.")
        return

    if units <= 3 * crew_size:
        print("Not enough units.")
        return

    # 3 units to each pirate for a night on the town, except Yondu and Peter
    diversion_units = (crew_size - 2) * 3
    units -= diversion_units

    # Yondu skims 13% of the units off the top
    skim_yondu = int(units * .13)
    units -= skim_yondu

    # Peter Skims 11% off the remaining units
    skim_peter = int(units * .11)
    units -= skim_peter

    # Remaining loot is divvied up to entire crew after skimming
    share_crew = units // crew_size
    share_yondu = skim_yondu + share_crew
    share_peter = skim_peter + share_crew

    # Remaining units cannot be share equally and are given to the Reaver’s Benevolent Fund (RBF)
    share_rbf = units % crew_size

    # Printing shares to screen
    print_string = f"Yondu's share: {str(share_yondu)}\n" \
                   f"Peter's share: {str(share_peter)}\n" \
                   f"Crew: {str(share_crew)}\n" \
                   f"RBF: {str(share_rbf)}"

    print(print_string)


if __name__ == "__main__":
    main()
