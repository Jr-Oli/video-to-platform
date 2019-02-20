import math

#currentX = float('.25')
#newX = float('-.5')

def find_x(currentX,newX):
    xMovement ='0'
    #determine which direction we need to go for X
    if currentX > newX: #We're going from bigger to smaller
        xMovement = currentX - newX
        xMovement = xMovement*-1
    if currentX < newX: #We're going from smaller to bigger.
        if currentX <= 0:
            currentX = currentX*-1
            xMovement = currentX+newX 
        else:
            xMovement = newX-currentX
    return xMovement

