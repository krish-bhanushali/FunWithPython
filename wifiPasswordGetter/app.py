import subprocess 

#pip install -r requirements.txt
#improve qr code for different authentications example wpa2psk , wep. Hint: Just extract Authentication
#fails on iPhoneNames i.e krish's iPhone Hint:Command line parameter

import pyqrcode
import png
from pyqrcode import QRCode

def getCurrentWifiSSID():
    x = subprocess.check_output("netsh wlan show interfaces")
    data = x.decode('utf-8', errors ="backslashreplace")
 
    # spliting data by line by line
    data = data.split('\n')
    

    for i in data:
        if " SSID" in i :
             i = i.split(":")
             
             i = i[1]
             
             return i[1:-1];

def getCurrentWifiPassword(wifiName):

    command1= "netsh wlan show profile name=\"";
    
    command2 =  wifiName
    command3 = "\" key=clear"
    command = command1 + command2 + command3
   
    x = subprocess.check_output(command);

    data = x.decode('utf-8', errors ="backslashreplace")
 
    # spliting data by line by line
    data = data.split('\n')


    for i in data:
        if "Key Content" in i :
             i = i.split(":")
             
             i = i[1]
             
             return i.split(" ")[1].split("\r")[0]

def getAllWifiPasswordsSaved():
    x = subprocess.check_output('netsh wlan show profiles')
    data = x.decode('utf-8', errors ="backslashreplace")
 
    
    data = data.split('\n')
 

    ssids = []

    for i in data:
        if "All User Profile" in i :   
            i = i.split(":")[1]
            #since space and \r are not required
            
            i = i[1:-1] 
            
            ssids.append(i)
            
    print(ssids)  
    
    #just a heading
    print("{:<25}| {:<}".format("Wi-Fi Name", "Password"))
    print("----------------------------------------------")
    for ssid in ssids:
        try:
       
            x = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'])
            data = x.decode('utf-8', errors ="backslashreplace")
            data = data.split('\n')
            
            for pw in data:
                if "Key Content" in pw:
                    pw = pw.split(":")
             
                    pw = pw[1]
                    
                    pw =  pw.split(" ")[1].split("\r")[0]
                    try:
                        print("{:<25}| {:<}".format(ssid, pw))
                    except:
                        print("{:<25}| {:<}".format(ssid, ""))




        except:
            print("Error Occured")


def generateQrCode(wifiString):
    url = pyqrcode.create(wifiString)
      
    # Create and save the png file naming "myqr.png"
    url.png('myqr1.png', scale = 6)

def returnWifiString(wifiName,wifiPassword):

    wifiUrl = f"WIFI:S:{wifiName};T:WPA/WPA2;P:{wifiPassword};;"
    print(wifiUrl)
    return wifiUrl

if __name__=="__main__":
    myWifiName = getCurrentWifiSSID()
    myWifiPassword = getCurrentWifiPassword(myWifiName);
    print(f"Your password of connected wifi {myWifiName} is {myWifiPassword}")

    # Uncomment bellow to generate qr code of current wifi
    # generateQrCode(returnWifiString(myWifiName,myWifiPassword))
    
    #uncomment bellow to all wifi passwords
    # getAllWifiPasswordsSaved()

