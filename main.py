#LightCode
print("Circut is loading")
light.set_brightness(25)
light.set_pixel_color(0, color.rgb(255, 0, 0))
pause(150)
light.set_pixel_color(1, color.rgb(255, 0, 0))
pause(150)
light.set_pixel_color(2, color.rgb(255, 0, 0))
pause(150)
light.set_pixel_color(3, color.rgb(255, 0, 0))
pause(150)
light.set_pixel_color(4, color.rgb(255, 0, 0))
pause(150)
light.set_pixel_color(5, color.rgb(255, 0, 0))
pause(150)
light.set_pixel_color(6, color.rgb(255, 0, 0))
pause(150)
light.set_pixel_color(7, color.rgb(255, 0, 0))
pause(150)
light.set_pixel_color(8, color.rgb(255, 0, 0))
pause(150)
light.set_pixel_color(9, color.rgb(255, 0, 0))
pause(500)
light.clear()
#OvenTempCode
while True:
    if 200 < input.temperature(TemperatureUnit.Fahrenheit) < 250 :
        light.set_all(color.rgb(40, 40, 0))
        pause(250)
        light.clear()
        light.set_all(color.rgb(40, 40, 0))
        pause(250)
        light.clear()
        print ("The Temp is between 200 and 250")
    elif 250 < input.temperature(TemperatureUnit.Fahrenheit) < 300 :
        light.set_all(color.rgb(65, 105, 225))
        pause(250)
        light.clear()
        light.set_all(color.rgb(65, 105, 225))
        pause(250)
        light.clear()
        print ("The Temp is between 250 and 300")
    elif 300 < input.temperature(TemperatureUnit.Fahrenheit) < 350 :
        light.set_all(color.rgb(127, 255, 0))
        pause(250)
        light.clear()
        light.set_all(color.rgb(127, 255, 0))
        pause(250)
        light.clear()
        print ("The Temp is between 300 and 350")
    elif 350 < input.temperature(TemperatureUnit.Fahrenheit) < 400 :
        light.set_all(color.rgb(153, 50, 204))
        pause(250)
        light.clear()
        light.set_all(color.rgb(153, 50, 204))
        pause(250)
        light.clear
        print ("The Temp is between 350 and 400")
    elif 400 < input.temperature(TemperatureUnit.Fahrenheit) < 450 :
        light.set_all(color.rgb(216, 112, 147))
        pause(250)
        light.clear()
        light.set_all(color.rgb(216, 112, 147))
        pause(250)
        light.clear()
        print ("The Temp is between 400 and 450")
    elif 450 < input.temperature(TemperatureUnit.Fahrenheit) < 500 :
        light.set_all(color.rgb(255, 250, 250))
        pause(250)
        light.clear()
        light.set_all(color.rgb(255, 250, 250))
        pause(250)
        light.clear()
        print ("The Temp is between 450 and 500")

    

