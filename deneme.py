from dronekit import connect,Vehicle
import time

iha=connect('tcp:127.0.0.1:5762',wait_ready=True)
if iha:
    print("baglandim")

cmds=iha.commands
cmds.download()
cmds.wait_ready()
if cmds:
    print("commands takip")

iha.arm(wait=True)

if iha.armed==True:
    while 1:
        print(f"GPS:{iha.gps_0}")
        print(f"Battery:{iha.battery}")
        print(f"is armable?:{iha.is_armable}")
        print(f"System status:{iha.system_status.state}")
        time.sleep(2)