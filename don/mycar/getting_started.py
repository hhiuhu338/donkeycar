"""
A simple example of sending data from 1 nRF24L01 transceiver to another.
This example was written to be used on 2 devices acting as 'nodes'.
"""
import sys
import argparse
import time
import struct
from RF24 import RF24, RF24_PA_LOW





if __name__ == "__main__":
    radio = RF24(22, 0)
    payload = [0.0]
    if not radio.begin():
        raise RuntimeError("radio hardware is not responding")
    address = [b"1Node", b"2Node"]
    radio_number = bool(1)
    radio.setPALevel(RF24_PA_LOW)  # RF24_PA_MAX is default
    radio.openWritingPipe(address[radio_number])  # always uses pipe 0
    radio.openReadingPipe(1, address[not radio_number])  # using pipe 1
    radio.payloadSize = len(struct.pack("<f", payload[0]))
    radio.startListening()  # put radio in RX mode
    start_timer = time.monotonic()
    while (time.monotonic() - start_timer) < 10000:
        has_payload, pipe_number = radio.available_pipe()
        if has_payload:
            # fetch 1 payload from RX FIFO
            buffer = radio.read(radio.payloadSize)
            # use struct.unpack() to convert the buffer into usable data
            # expecting a little endian float, thus the format string "<f"
            # buffer[:4] truncates padded 0s in case payloadSize was not set
            payload[0] = struct.unpack("<f", buffer[:4])[0]
            # print details about the received packet
            print(
                "Received {} bytes on pipe {}: {}".format(
                    radio.payloadSize,
                    pipe_number,
                    payload[0]
                )
            )

            start_timer = time.monotonic()  # reset the timeout timer
            a=payload[0]
            print(type(a))
            if a>0.5 and a<1.5:
                a=1
            elif a<0.5:
                a=0
            elif a>1.5:
                a=2

            print(a,type(a))

