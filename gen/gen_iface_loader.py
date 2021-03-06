#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET

iface_names = [
    "Apps",
    "AppList",
    "AppTicket",
    "Client",
    "Controller",
    "Friends",
    "HTMLSurface",
    "HTTP",
    "Inventory",
    "Matchmaking",
    "MatchmakingServers",
    "Music",
    "MusicRemote",
    "Networking",
    "RemoteStorage",
    "Screenshots",
    "UGC",
    "User",
    "UserStats",
    "Utils",
    "Video",
    "GameServer",
    "GameServerStats",
    "GameCoordinator",
    "ParentalSettings"
]

if len(sys.argv) < 3:
    print("arguments missing")
    exit(-1)

steam_api_xml = sys.argv[1]
output_h = sys.argv[2]

steam_api_tree = ET.parse(steam_api_xml)
steam_api = steam_api_tree.getroot()

with open(output_h, 'w') as o:
    for iface_name in iface_names:
        o.write("#ifdef STEAMAPI_ENABLE_" + iface_name + "\n")
        o.write("if (interfaces.has(\"Steam" + iface_name + "\")) {\n")
        o.write("    do {\n")
        o.write("    auto value = interfaces.get(\"Steam" + iface_name + "\", \"\");\n")
        for iface in steam_api.findall("interface[@name='" + iface_name + "']"):
            iface_version = iface.get("version")
            o.write("    if (value == \"" + iface_version + "\") {\n")
            o.write("        sapi" + iface_name + " = reinterpret_cast<ISteam" + iface_name + " *>(new " + iface_name + "_" + iface_version + "());\n")
            o.write("        TRACE(\"loaded interface " + iface_version + "\");\n")
            o.write("        break;\n")
            o.write("    }\n")
        o.write("    ERR(value << \" not implemented\");\n")
        o.write("    std::abort();\n")
        o.write("    } while(0);\n")
        o.write("}\n")
        o.write("#endif\n")

