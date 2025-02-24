# HHTP/2 VS HTTP/3

1. Faster connection
   • TCP in HHTP/2 connections require multiple steps (three-way handshakes) before data is sent
   • QUIC in HHTP/3 uses UDP internet connection and combines everything in a single step reducing delays
2. No head-of-line blocking
   • In TCP in HHTP/2, if one data packet is lost, all other packets wait until it is resent
   • QUIC HHTP/3 allows packets to arrive independently, so one lost packet does not slow everything down
3. Network Connectivity
   • If your Wi-Fi switches to mobile data a TCP in HHTP/2 connection breaks and must restart
   • QUIC HHTP/3 keeps the connection even when switching networks
   HTTP/3 uses UDP, which is more efficient for modern networks and devices. As a result, browsers including Chrome, Firefox, and Safari support HTTP/3.
