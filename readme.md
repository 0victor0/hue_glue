# Hue Glue

Hue Glue is another library to connect to the Phillips Hue API. At the moment, there is only support for the state of the lights i.e., brightness, color. It controls a single light per class instance.

##Requirements

+ json
+ requests

##Examples

Here's how to use Hue Glue:

###Create a class:

        import hue_glue as hue
        a = hue.api()

###Set the bridge ip, light:

        a.bridge = "10.0.1.5"           #change this to your Hue Bridge IP
        a.key = "salfp93jfnlw930fpaj"   #change the string to your key
        a.light = 8                     #change this to the light you're changing

or do it all in one call:

        a = hue.api(bridge="10.0.1.5", key="salfp93jfnlw930fpaj", light=8)

###Other light settings:

Alternatively, these can also be set during class instantiation:

        a.bri=255,
        a.ct = 500
        a.on= True
        a.sat= 100
        a.xy = [0.5,0.5]

The xy attribute must be passed as list of two floats. To fine tune color, reference the CIE Chromaticity Chart.

![CIE Chart](https://github.com/0victor0/hue_glue/blob/master/img/cie1931.svg "Credit: Wikipedia")

[Credit: Wikipedia](https://en.wikipedia.org/wiki/CIE_1931_color_space)

###Preview the API call:

        >>> a.show()
        ('bridge IP: ', '10.0.1.5')
        ('key: ', 'salfp93jfnlw930fpaj')
        ('on: ', True)
        ('light: ', 8)
        ('xy: ', [])
        ('bri: ', None)
        ('sat: ', None)

###Make the API call:

        >>>a.api_call()
        ('Payload: ', '{"on": true}')
        ('IP addy: ', 'http://10.0.1.5/api/salfp93jfnlw930fpaj/lights/8/state')

###Extra one liners:

####Turn off:

        a.turn_off()

####Turn on:

        a.turn_on()

####Change color:

        a.turn_color("blue")    #try different colors here

Before trying the one-liners, make sure you specify which light you want, either by the 'light' keyword argument when you instantiate the class, or by seeing the light attribute. Here's what I mean:

        a = hue.api(light=1)
        #or
        a.light = 1
