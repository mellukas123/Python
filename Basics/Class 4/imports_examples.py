# Option 1 - the best
import main_functions

main_functions.get_action()

# Option 2 - basically the same as the 1st one, but with renaming the file
import main_functions as fns

fns.get_action()

# Option 3 - good, but only if you are not using all the functions
from main_functions import get_action, greet

greet("Merlyn")
get_action()

# Option 4 - not good if the file is big
from main_functions import * # * - is everything

get_action()
greet()
get_entry_details()
