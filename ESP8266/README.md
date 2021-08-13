# ESP8266 WiFi Dongle 

## Setup
### For API Calls
If you want to use the ESP8266 to make API calls to ThingWorx, AirTable, etc. please go to the API folder, download the boot_API.py file, and upload that directly to your ESP8266 through the LabVIEW IDE or Terminal. The ESPClient.py file also gets saved on the ESP8266. Then soft reboot the ESP8266.

Then, update passwords.py with your credentials. Upload that code onto the SPIKE Prime using the IDE. Finally, also upload the Backpack_Code onto the SPIKE.

Dongle_Tests.py are tests used on the ESP8266 to make sure everything works. espTests.py is a sample code to access ThingWorx from SPIKE Prime.

### For MQTTX 
If you want to use the ESP8266 as a MQTT client, please download a broker on your desktop (eg. MQTTX). Then, update the sensitive_data.py file with your own credentials and upload it onto the ESP directly. Next, edit the boot_general.py file (lines 30-35) to include your MQTT broker's sub and pub topics. Upload the boot_general.py file onto your ESP directly. Run the main_general.py file to test everything!
