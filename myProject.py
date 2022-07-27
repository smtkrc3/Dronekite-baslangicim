from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import math
import pymavlink

class UAV():
    def __init__(self,connection_address):
        self.tb2=connect(connection_address,wait_ready=True)
        if self.tb2:
            print("Baglanti Basarili")
        
    def arm_and_takeoff(self):
        print("Basic pre-arm checks...")
        while not self.tb2.is_armable:
            print(" Waiting for vehicle to initialise...")
            time.sleep(1)
        self.tb2.arm(wait=True)
        self.tb2.mode    = VehicleMode("AUTO")
        print ("Taking off!")
        
    def takeCommands(self):
        cmds=self.tb2.commands
        cmds.download()
        cmds.wait_ready()
        if cmds:
            print("Commands were taken...")
            
    def distance_to_current_waypoint(self):
        nextwaypoint=self.tb2.commands.next
        if nextwaypoint ==0:
            return None
        missionitem=self.tb2.commands[nextwaypoint-1] #commands are zero indexed
        lat=missionitem.x
        lon=missionitem.y
        alt=missionitem.z
        targetWaypointLocation=LocationGlobalRelative(lat,lon,alt)
        distancetopoint = iha.getdistancemetres(self.tb2.location.global_frame, targetWaypointLocation)
        return distancetopoint

    def getdistancemetres(self,aLocation1, aLocation2):
        dlat = aLocation2.lat - aLocation1.lat
        dlong = aLocation2.lon - aLocation1.lon
        return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5
    
    def Location_and_relativeAltitude (self):
        return self.tb2.location.global_relative_frame
    
    def otherInfos(self):
        print("Velocity: %s" % self.tb2.velocity)
        print("GPS: %s" % self.tb2.gps_0)
        print("Airspeed: %s" % self.tb2.airspeed)
        print("Euler Angles: %s" % self.tb2.attitude)

        
iha=UAV('tcp:127.0.0.1:5762')
iha.takeCommands()
iha.arm_and_takeoff()
while 1:
    print(f"Distance to Waypoint {iha.tb2.commands.next} :{iha.distance_to_current_waypoint()}")
    print(iha.Location_and_relativeAltitude) 
    iha.otherInfos()
    time.sleep(1.5)


