#LESSON 33 - DELETING FILES

THREE FUNCTIONS

1. os module.
os.unlink('RELATIVE PATH\FILE') # removes a file

os.rmdir(ABSOLUTE PATH) # removes a folder
# FOLDER MUST BE EMPTY!!!!!!!!!

import shutil
shutil.rmtree() # REMOVE TREE FROM SHELL UTILITIES MODULE
# removes EVERYTHING IN A FOLDER
'''
 these functions PERMANENTELY DELETE FILES
 THEY REQUIRE NO CONFIRMATION!

 To avoid this while testing
 DO A TRY RUN

TO DO A DRY RUN, COMMENT OUT (#) THE DELETE COMMAND. 
'''
# ------------------------

Instead of Deleting, please use
SEND2TRASH MODULE - INSTALL USING PIP

Use function:
    send2trash.send2trash(ABSOLUTE FILEPATH NAME)

# ------------------------
