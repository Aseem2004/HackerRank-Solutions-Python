regex_pattern =r"^(?=[MDCLXVI])M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"	

import re
print(str(bool(re.match(regex_pattern, input()))))