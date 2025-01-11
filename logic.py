import random as r, string as s

def password(length):
    elements = s.ascii_letters+s.ascii_uppercase+s.digits+s.punctuation
    password = ""
    for i in range(length):
        password += r.choice(elements)
    return password

def roll(dice):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        return ('Format has to be in NdN!')
        

    result = ', '.join(str(r.randint(1, limit)) for r in range(rolls))
    return(result)