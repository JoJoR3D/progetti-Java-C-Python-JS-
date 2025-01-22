
# LINK: https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments


def function(x, y= "doctor", z= "player_soccer", w= "driver"):
    if x == 5 and (y == "doctor" or z == "player_soccer" or w == "driver"):
        print(y,z,w)
        return 1
    else:
        return 2 
    





x=5

print(function(x,z= "Doctorrrr"))