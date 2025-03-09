from toolbox import DFA
from toolbox import templates

templates.dfa_template_generator("config/new_dfa")
print("Template generat în config/new_dfa.cfg")

# # Inițializăm DFA-ul cu un fișier de configurare
# dfa = DFA("config/example.cfg")

# # Verificăm dacă automatul este valid
# if dfa.is_valid():
#     print("DFA-ul este valid")

#     # Testăm o intrare
#     result = dfa.run("abba")
#     print(f"Rezultatul pentru 'abba': {result}")  # True sau False
# else:
#     print("DFA-ul nu este valid")
