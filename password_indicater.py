import re
def check_password(password):
    upper_case=any(char.isupper() for char in password)
    lower_case=any(char.islower() for char in password)
    digit=any(digi.isdigit() for digi in password)
    spl_char=bool(re.search(r'[!@#$%^&*()_+}{:?/<>]',password))

    if len(password)>= 8 and upper_case and lower_case and digit and spl_char:
        return "Strong"
    elif len(password)<=8 and len(password)>=6 :
        return "Medium"
    else:
        return "weak"
    
password=input("Enter your password: ")
#print(char.isupper() for char in password )
res1= check_password(password)
print(res1)