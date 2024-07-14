import pynetbox
import urllib3

NAUTOBOT_SERVER = "192.168.1.21"
NAUTOBOT_API_KEY = "2885e91b76f4530672c5173f6b03a6ecad8ada60"

nb_conn = pynetbox.api(url=f"https://{NAUTOBOT_SERVER}", token=NAUTOBOT_API_KEY)
nb_conn.http_session.verify=False
urllib3.disable_warnings()

devices = nb_conn.dcim.devices.all()

for device in devices:
    print(f"DEVICE NAME: {device.name:^10} DEVICE IP: {device.primary_ip4}")
