# LESSON 32: COPYING AND MOVING FILES AND FOLDERS

import shutil

# The Shell Utilities module allows you to do it :)

# COPY FUNCTION
shutil.copy('SOURCE', 'DESTINATION')
Returns the string of the new file.

# COPY AND RENAME AT THE SAME TIME:
shutil.copy('SUORCE', 'DESTINATION WITH NEW NAME')

# COPY THE DIRECTORY (FOLDERS):
shutil.copytree('SOURCE', 'DESTINATION')

# MOVE FILE
shutil.move('SOURCE', 'DESTINATION')

# RENAME FILES
shutil.move('SOURCE', 'move it to the same folder, but with new name!')

