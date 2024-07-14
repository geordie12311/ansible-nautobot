import pynetbox
import urllib3

NAUTOBOT_SERVER = "add ip address here"
NAUTOBOT_API_KEY = "add api token here"

nb_conn = pynetbox.api(url=f"https://{NAUTOBOT_SERVER}", token=NAUTOBOT_API_KEY)
nb_conn.http_session.verify=False
urllib3.disable_warnings()

devices = nb_conn.dcim.devices.all()

for device in devices:
    print(f"DEVICE NAME: {device.name:^10} DEVICE IP: {device.primary_ip4}")
