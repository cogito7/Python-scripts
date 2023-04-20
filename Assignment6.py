import math

def find_adj_length(hypotenuse, adj_angle):
    return hypotenuse * math.cos(adj_angle)

def find_opp_length(hypotenuse, adj_angle):
    return hypotenuse * math.sin(adj_angle)

def find_adj_angle_sin(hypotenuse, opp_length):
    return math.degrees(math.asin(opp_length / hypotenuse))

def find_adj_angle_tan(adj_length, opp_length):
    return math.degrees(math.atan(opp_length / adj_length))


adj_length = float(input("Adjacent length: "))
opp_length = float(input("Opposite length: "))
hypotenuse = float(input("Hypotenuse: "))
adj_angle = math.radians(float(input("Adjacent angle: ")))

print("The calculated adjacent length is", round(find_adj_length(hypotenuse, adj_angle), 2))
print("The calculated opposite length is", round (find_opp_length(hypotenuse, adj_angle), 2))
print("The calculated adjacent angle using sine is", round(find_adj_angle_sin(hypotenuse, opp_length), 2))
print("The calculated adjacent angle using tangent is", round(find_adj_angle_tan(adj_length, opp_length), 2))

                                                              

                        
                         
