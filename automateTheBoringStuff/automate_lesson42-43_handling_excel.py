# LESSON 42 - READING EXCEL SPREADSHEATS

# Important:
''' First import openpyxl module from pip.
Remember: access pip through cmd console and 'pip install openpyxl'
'''
The OPEN command in OpenpyXL is:
VARIABLE = openpyxl.load_workbook('example.xlsx') # loads an existing workbook

THE CREATE A NEW WORKBOOK
VARIABLE = openpyxl.Workbook() # UPPER W!!!!

# OPENING SHEETS BY NAME:
'''
SHEET_OBJECT (VARIABLE) = VARIABLE.get_sheet_by_name('Sheet1')

If you don't know the names:
VARIABLE.get_sheet_names()'''
# returns a list of strings with the sheet names

OPenpyXL uses the same method as lists to access cells in the Excel file:
    for example:
        >>> workbook.get_sheet_names()
        >>> prints: ['Sheet1', 'Sheet2'] # these are sheet names
        >>> sheet = get_sheet_by_name('Sheet1') # 'sheet' is now Sheet1
        >>> sheet['A1']
        Returns a cell object I can add in a variable.
        >>> cell = sheet['A1']
        cell.value = returns the content of the cell.
        datetime.datetime(2015, 4, 5, 13, 34, 2) # it's in "datetime' module format
                                                 # to make it a string:
        str(cell.value)
        OR
        str(sheet['A1'])
        
 # ---------------------------------
 
        I dont need to use the ['A1'] method, and I can also use:
            sheet.cell(row=1, column=2) # use this method. STARTS AT 1, not ZERO

        EXAMPLE:

                >>> sheet1.cell(row=1, column=2)
                <Cell 'Sheet1'.B1>
                >>> for i in range(1,8):
                        print(i, sheet1.cell(row=i, column=2).value)

                        
                1 Apples
                2 Cherries
                3 Pears
                4 Oranges
                5 Apples
                6 Bananas
                7 Strawberries



# I CAN SEE THE CONTENTS IN A CELL BY USING:
sheet['LETTERNUMBER'] # the 'sheet' is a variable, and LETTERNUMBER can be A10, or C16, whatever

The contents can be in several forms: datetime module format, strings, ints.


# --------------------------------
# --------------------------------

# LESSON 43 - EDITING EXCEL SPREADSHEETS

# making a new excel spreadsheet:

THE CREATE A NEW WORKBOOK
>>> VARIABLE = openpyxl.Workbook() # UPPER W!!!!

This creates a blank workbook with 1 sheet.
I can access that sheet by using:
>>> SHEET_VARIABLE = VARIABLE.get_sheet_by_name('Sheet')

I can assign content to a cell in a sheet in a simple way:

    sheet['A1'] = 'string'
    sheet['B1'] = int
    sheet['C1'] = float


# FOR NOW IT'LL ONLY EXISTS IN PYTHON'S MEMORY
# TO SAVE ON HARDDRIVE:

>>> VARIABLE.save('new_file_name.xlsx') # remember: 'VARIABLE' is the NAME!

# adding worksheet to your workbook:

>>> NEW_SHEET_VARIABLE = VARIABLE.create_sheet()
Adds to name 'Sheet1'

If we dont like the name, just call the title variable:

>>> sheet2.title # shows the name of sheet2
sheet2.title = 'NEW NAME'


# TO SPECIFY THE LOCATION OF A SHEET:

>> VARIABLE.create_sheet(index=0, title='Sheet1') # adds "Sheet1' in the first sheet.




