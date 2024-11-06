import board
import busio
import displayio
from adafruit_display_text import label
import terminalio

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Create the display
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C, )#ok

init_sequence = (b"\xe1\x0f\x00\x0E\x14\x03\x11\x07\x31\xC1\x48\x08\x0F\x0C\x31\x36\x0F" # Set Gamma
                 b"\x11\x80\x78"# Exit Sleep then delay 0x78 (120ms)
                 b"\x29\x81\xaa\x78"# Display on then delay 0x78 (120ms)
                )

display = displayio.Display(display_bus,  init_sequence, width=128, height=128, rotation=0) #ok




# Create a group to hold the text
group = displayio.Group()



# Add text to the group
text = "Hello, World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=10, y=50)
group.append(text_area)

# Add the group to the display
display.show(group)

# Refresh the display
display.refresh()


# import board
# import busio
# import digitalio
# import displayio
# from adafruit_display_shapes.rect import Rect
# from adafruit_display_text import label
# import terminalio

# displayio.release_displays()

# # GPIO pin assignments
# i2c = busio.I2C(board.SCL, board.SDA)
# #reset = digitalio.DigitalInOut(board.D27)

# # Create the I2C display bus
# display_bus = displayio.I2CDisplay(i2c, reset=board.D27,device_address=0x3D)

# init_sequence = (b"\xe1\x0f\x00\x0E\x14\x03\x11\x07\x31\xC1\x48\x08\x0F\x0C\x31\x36\x0F" # Set Gamma
#                  b"\x11\x80\x78"# Exit Sleep then delay 0x78 (120ms)
#                  b"\x29\x81\xaa\x78"# Display on then delay 0x78 (120ms)
#                 )

# # Create the display
# display = displayio.Display(display_bus, init_sequence, width=128, height=128)

# # Create a group to hold the text and shapes
# group = displayio.Group()

# # Add a background rectangle
# background = Rect(0, 0, 128, 128, fill=0x000000)
# group.append(background)

# # Add some text
# text_area = label.Label(terminalio.FONT, text="Hello, World!", color=0xFFFFFF, x=10, y=10)
# group.append(text_area)

# # Show the group on the display
# display.show(group)
# display.refresh()