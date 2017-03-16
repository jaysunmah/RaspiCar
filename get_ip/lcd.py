import lcddriver
import socket
import time

lcd = lcddriver.lcd()



while True:
  try:
    ipAddr = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

    lcd.lcd_display_string(ipAddr, 0)
    print(ipAddr)
  except:
    lcd.lcd_display_string("Starting up wifi...", 0)
  time.sleep(5)
  lcd.lcd_clear()


