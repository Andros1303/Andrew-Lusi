def is_uppercase(inp):
    if any(a.islower() == True for a in inp):
        return False
    else:
        return True
#Create a method is_uppercase() to see whether the string is ALL CAPS. 