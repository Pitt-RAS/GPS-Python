import serial
import pynmea2

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)

while True:
    try:
        reader = pynmea2.NMEAStreamReader(ser)
        sentence = reader.next()
        for item in sentence:
            print(type(item))
            #if type(item) is pynmea2.types.talker.GGA:
            #    print("Satellites: ", item.num_sats)
            #    print("Fix type: ", item.gps_qual)
            #    print("Latitude: ", item.lat, item.lat_dir)
            #    print("Longitude: ", item.lon, item.lon_dir)
    except pynmea2.ParseError:
        print("bad sentence")
