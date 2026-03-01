import math
co = float(input('cateto oposto:'))
ca = float(input('cateto adjasente'))
h = math.hypot (co,ca)
rad = math.atan2(co,ca)
grau = math.degrees(rad)
print (f'co{co:.2f},ca{ca:.2f},hip{h:.2f},rad{rad:.2f},grau{grau:.2f}')