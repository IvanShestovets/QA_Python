

def valid_pas(password):
    if len(password) < 8:
        return False
    if password[0] == '+' or password[-1] == '+':
        for char in password:
            if char.isdigit():
                return True
            if char.isalpha():
                return True
    return False

print(valid_pas('+Qw78111fd')) #True
print(valid_pas('Qw78111fd+')) #False
print(valid_pas('er.!iku')) #False
print(valid_pas('eri3u')) #false
    
    
