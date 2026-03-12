"""
| Import Form | Code Example | Call Method | Example Usage |
|-------------|-------------|-------------|--------------|
| import module_name | import random, os | module_name.function_name | random.randint(10, 100) |
| import module_name as alias | import random as rd | alias.function_name | rd.randint(10, 100) |
| from module_name import function_name | from random import randint, choice | function_name | randint(10, 100) |
| from module_name import function_name as alias | from random import randint as rint | alias | rint(10, 100) |
| from module_name import * | from random import * | function_name | randint(10, 100) |

"""
#import functions_demo
from functions_demo import sum_num
import string_utils as su


print(sum_num(1,4,5))

print(su.to_lower("DJKAHJDJD"))


"""
# package
# A package is a folder that contains multiple modules. It needs an __init__.py file to indicate that it is a package.


| Import Form | Code Example | Call Method | Example Usage |
|-------------|-------------|-------------|--------------|
| import package.module | import utils.my_fun | package.module.function | utils.my_fun.log_separator1() |
| from package import module | from utils import my_fun | module.function | my_fun.log_separator1() |
| from package import * | from utils import * | module.function | my_fun.log_separator1() |
| from package.module import function | from utils.my_fun import log_separator1 | function | log_separator1() |
| from package.module import * | from utils.my_fun import * | function | log_separator1() |
"""