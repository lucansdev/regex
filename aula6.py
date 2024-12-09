# ^ -> comeca com
# $ -> termina com
# [^a-z] - negacao "qualquer coisa que nao seja entre a ate z
import re

cpf = "147.852.963-12"
print(re.findall(r"^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$",cpf))
print(re.findall(r"[^0-9a-zA-Z.-]",cpf))
