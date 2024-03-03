
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def task():
	print('Hello world')
	return "{'message': 'Message from Raspberry Pi'}"

myMQTTClient = AWSIoTMQTTClient("MyClientID") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("###########.iot.us-east-1.amazonaws.com", 8883)

myMQTTClient.configureCredentials("/home/rasbpisom/aws-iot/connect_device_package/root-ca.pem", "/home/rasbpisom/aws-iot/connect_device_package/private.pem.key", "/home/rasbpisom/aws-iot/connect_device_package/certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()

myMQTTClient.publish(
	topic = '',
	QoS=1,
	payload = task
)
