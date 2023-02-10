from interface import Interface




interfaceInfo = Interface().get_interface()
if interfaceInfo['Hosted network status'] == 'Not available' and len(interfaceInfo) < 10:
    print("Unable to find a network adaptor on Wi-Fi. You either do not have one, or you are connected to ethernet.")
elif interfaceInfo['State'] == 'connected':
    print(f"You are currently connected to \"{interfaceInfo['SSID']}\" on channel {interfaceInfo['Channel']} with a signal strength {interfaceInfo['Signal']}.")
    print(f"You are using protocol \"{interfaceInfo['Radio type']}\" with \"{interfaceInfo['Authentication']}\" encryption.")
    print(f"You have an uplink of {interfaceInfo['Transmit rate (Mbps)']}mbps and a downlink of {interfaceInfo['Receive rate (Mbps)']}mbps.")
    print(f"Your {interfaceInfo['Name']} adapter is the {interfaceInfo['Description']}.")
elif interfaceInfo['State'] == 'disconnected':
    print(f"Disconnected from {interfaceInfo['Name']}")
else:
    print(interfaceInfo['State'])