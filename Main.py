# ---------------------------------------------------------- #
# Title: Listing 12
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KBosworth,12/3/2019,Modified script to get it working
# KBosworth,12/4/2019,Finished script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import sys
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Data -------------------------------------------------------------------- #
strFileName = "EmployeeData.txt"
lstFileData = [] # List of employees
lstOfEmployees = [] # Table of employee objects
# Data -------------------------------------------------------------------- #

# Main Body of Script ----------------------------------------------------- #
try:
    lstFileData = Fp.read_data_from_file(strFileName)  # read file data
    for row in lstFileData:
        lstOfEmployees.append(Emp(row[0], row[1], row[2].strip()))

    while True:
        # Show user a menu of options
        Eio.print_menu_items()
        # Get user's menu option choice
        strChoice = Eio.input_menu_options()
        if strChoice.strip() == '1':
            # Print Employees listed in the file (if any)
            Eio.print_current_list_items(lstOfEmployees)
            continue
        elif strChoice.strip() == '2':
            # Let user add data to the list of employee objects
            lstOfEmployees.append(Eio.input_employee_data())
            continue
        elif strChoice.strip() == '3':
            # Let user save current data to file
            Fp.save_data_to_file(strFileName, lstOfEmployees)
            continue
        elif strChoice.strip() == '4':
            # Let user exit program
            break
        else:  # Add a catch all for invalid entries
            print("That option is not valid. Please select 1-4")
            continue
except Exception as e:
    print("There was an error!")
    print(e, e.__doc__, type(e), sep='\n')
    sys.exit(1)
# Main Body of Script ----------------------------------------------------- #
