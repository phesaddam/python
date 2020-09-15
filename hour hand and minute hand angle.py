# programing for the angle between minute and hour hand 
def printangle(hour,min):
     if hour==12:                           #hour 12 =0 because to cosider as starting point
       hour=0
     else:
       hour=hour
     hour_in_minute = hour*60+min          #conversion of hour in minute

     angle = 0.5*hour_in_minute-6*min      # formulation of angel between min hand and hour hand
     if angle<0:                           #when minute had lager value than hour_in_minute conversion we get negative value
      x=angle=360+angle                    #angle is added to 360 to get positive value  
      y=360-angle
     else:
      x=angle
      y=360-angle

     print(x,y)

h = int(input('enter hour ='))      #input in integer value of hour
m  = int(input('enter minute = '))  #input of minute in interger 
printangle(h,m)                     #function call for printing angle

