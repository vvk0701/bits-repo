import json
import subprocess
service = 'applmgmt'

def toWrite(file, str):
  with open (file, 'w') as fileobject:
    fileobject.write(json.dumps(str))

def restartService(service):
    cmd = 'service-control --restart %s' %(service)
    response = subprocess.call(cmd, shell=true)
    return response

def main():
  envJson = {"env": {"managed_by": "VMWARE",
            "deployed_by": "VMWARE",
            "provider": "AWS"},}
  file = '/etc/applmgmt/appliance/environment.conf'
  toWrite(file, envJson)
  response = restartService(service)
  if response != 0:
      print ('Could not restart service:'), (service)
  vc = 'onPrem'
  addIdentitySource(vc)
  

def addIdentitySource(vc):
	pass

def getCloudPermissionUtilJar():
	pass

def executeCloudPermission():
	pass

def updateLookup():
	pass

def LinkOnPrem():
	pass
	
if __name__ == '__main__':
  main()
