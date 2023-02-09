from microbit import*
#we make an infinite loop
while True:
    #we make a variable
    times = 0
    #we check if button a is pressed then we make the variable increases by 25.5 which is the light level
    if button_a.is_pressed():
        pin0.write_analog(times+25.5)
        #we check if the variable reach it's max we make it go back to zero
        if times == 255:
            times = times - times
    else:
        #we check if the button b is pressed the light turns off
        if button_b.is_pressed():
            pin0.write_analog(0)

