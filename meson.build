project('freesteamapi', ['cpp', 'c'])

gen_types = find_program('gen/gen_types.py')
gen_iface = find_program('gen/gen_iface.py')

steam_types = custom_target(
    'steam_types.h',
    output : 'steam_types.h',
    input : 'steamapi.xml',
    command : [gen_types, '@INPUT@', '@OUTPUT@'],
)

ifaces = custom_target(
    'steam_interfaces.h',
    output : 'steam_interfaces.h',
    input : 'steamapi.xml',
    command : [gen_iface, '@INPUT@', '@OUTPUT@'],
)

steam_api_srcs = [
    'src/steam_api.cc',
    steam_types,
    ifaces,
    'src/UGC.cc',
    'src/User.cc',
    'src/Utils.cc',
    'src/UserStats.cc',
]

inih_srcs = [
    'inih/ini.c',
    'inih/cpp/INIReader.cpp',
]

shared_library('steam_api', [steam_api_srcs, inih_srcs])
