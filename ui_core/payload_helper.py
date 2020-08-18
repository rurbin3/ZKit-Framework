from ui_core.coloring import Color
import os

path = '/'.join(__file__.replace("\\", '/').split("/")[:-2])


def search_for_payloads(where="/User/Payloads/") -> dict:
    "searches /User/Payloads/ for payloads to install or the place you say"
    payloads = {}
    place = where.replace("\\", "/")
    if place.startswith('/'):
        place = place[1:]
    for r, d, _ in os.walk(place):
        for payload in d:

            payloads[payload] = r + payload

    return payloads


def list_payloads(payloads=search_for_payloads()):
    "You can get the result form search_for_payloads or i will do it"
    col = Color
    for index, payload in enumerate(payloads.keys()):
        print(col().RandomColor() + "\n{%s} --> %s" % (str(index + 1), payload + ((15 - len(payload))  # Bug fix
              * " ") + " >>> " + payloads[payload].replace(path, '')) + col().GetColor('reset'))

    print("\n{000} --> Back To Main Menu")
    return payloads


def list_builtin_payloads(payload_type):
    path = "/lib/payloads/" + payload_type + "/"
    payloads = search_for_payloads(path)
    payloads = list_payloads(payloads)
    print("Please Choose One Of Them (Number Of It): ", end="")
    return payloads
