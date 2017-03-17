import lcddriver
import socket
import time

lcd = lcddriver.lcd()



def displayMessage(tcpStatus, streamStatus):
  while True:
    lcd.lcd_clear()
    try:
      ipAddr = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

      lcd.lcd_display_string("IP Address:", 1)
      lcd.lcd_display_string(ipAddr, 2)
      if tcpStatus: lcd.lcd_display_string("TCP Connection: On", 3)
      else: lcd.lcd_display_string("TCP Connection: Off", 3)

      if streamStatus: lcd.lcd_display_string("Stream Server: On", 4)
      else: lcd.lcd_display_string("Stream Server: Off", 4)
      return
    except:
      lcd.lcd_display_string("Starting up wifi...", 0)
      time.sleep(1)
