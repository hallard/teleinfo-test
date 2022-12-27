#!/usr/bin/env python
import sys
import getopt
import serial
import serial.tools.list_ports

ps_name = sys.argv[0]
argv = sys.argv[1:]

standard = False
baudrate = 1200
port = None

def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

def find_serial_ports():
    ti = None
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        if "SER=TINFO" in hwid:
            ti = port
        elif "ttyAMA0" in desc and ti==None:
            ti = port
    return ti

def usage():
    print("{} -p|--port <serial_port>".format(ps_name))
    print("{} -s|--standard".format(ps_name))
    print("{} -l|--list".format(ps_name))
    print("{} [-h|--help]".format(ps_name))
    print("")


# Main progrram start here
# ========================
try:
    opts, args = getopt.getopt(argv, "hlsp:", ["help", "list", "standard", "port="])
except getopt.GetoptError:
    usage()
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h", "--help"):
        usage()
        sys.exit()
    elif opt in ("-l", "--list"):
        list_serial_ports()
        sys.exit()
    elif opt in ("-p", "--port"):
        port = arg
    elif opt in ("-s", "standard"):
        standard = True
        mode = "Standard"
        baudrate = 9600
if port is None:
    print("Missing serial port argument trying to find Teleinfo")
    port = find_serial_ports()
    if port is None:
        print("Unable to find serial port for Teleinfo please use one of the following")
        list_serial_ports()
        usage()
        sys.exit(2)

if standard == True:
	mode = "Standard"
else:
	mode = "Historique"

print("Teleinfo : Mode {}".format(mode))
print("Port     : {}".format(port))
print("Vitesse  : {}".format(baudrate))
print("\r\n")

tinfo = serial.Serial( port=port,
                       baudrate=baudrate,
                       parity=serial.PARITY_EVEN,
                       stopbits=serial.STOPBITS_ONE,
                       bytesize=serial.SEVENBITS )

while True:
	c = tinfo.read(1)
	#print(c, end='');
	sys.stdout.write(c)
