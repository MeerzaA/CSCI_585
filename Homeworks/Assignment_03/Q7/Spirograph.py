# Use 'python -m pip install simplekml' if you get a ModuleNotFoundError
import math
import simplekml

kml = simplekml.Kml()

Tommyt_x = -118.285432
Tommyt_y = 34.020528

Ri = 36
r = 9
a = 30 

cos = math.cos
sin = math.sin
pi = math.pi
nRev = 8


t = 0.0
while(t<(pi*nRev)): 
    t += 0.01
    x = (Ri+r)*cos((r/Ri)*t) - a*cos((1+r/Ri)*t)
    y = (Ri+r)*sin((r/Ri)*t) - a*sin((1+r/Ri)*t)
    kml.newpoint(coords=[(Tommyt_x + (x / 20000),Tommyt_y + (y / 20000))])

kml.save('s:/Documents/GitHub/CSCI_585/Homeworks/Assignment_3/Q7/Spirograph.kml')
print("Done")


