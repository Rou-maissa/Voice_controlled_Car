import pyfirmata

comport='COM8'

board=pyfirmata.Arduino(comport)

ENA=board.get_pin('d:9:p')
IN1=board.get_pin('d:8:o') 
IN2=board.get_pin('d:7:o')
ENB=board.get_pin('d:6:p')
IN3=board.get_pin('d:5:o')
IN4=board.get_pin('d:4:o')

speedA = 150 / 255  
speedTurn = 120 / 255

def move(text):
     if text=="forward":
        IN1.write(1)
        IN2.write(0)
        IN3.write(1)
        IN4.write(0)
        ENA.write(speedA)
        ENB.write(speedA)
     elif text=="backward":
        IN1.write(0)
        IN2.write(1)
        IN3.write(0)
        IN4.write(1)
        ENA.write(speedA)
        ENB.write(speedA)
     elif text=="right":
        IN1.write(0)
        IN2.write(0)
        IN3.write(1)
        IN4.write(0)
        ENA.write(speedTurn)
        ENB.write(speedTurn)
     elif text=="left":
        IN1.write(1)
        IN2.write(0)
        IN3.write(0)
        IN4.write(0)
        ENA.write(speedTurn)
        ENB.write(speedTurn)
     elif text=="stop":
        IN1.write(0)
        IN2.write(0)
        IN3.write(0)
        IN4.write(0)
        ENA.write(0)
        ENB.write(0)