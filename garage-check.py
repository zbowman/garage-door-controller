import requests
import time
from pushbullet import Pushbullet

pb = Pushbullet('<push bullet api token>')

right = requests.get('http://<controller IP or url>/st?id=right')
time.sleep(2)
left = requests.get('http://<controller IP or url>/st?id=left')

if right.text == 'open':
        pushright = pb.push_note("Garage Info", "Right Closing")
        closeright = requests.get('http://<controller IP or url>/clk?id=right')
        time.sleep(4)
elif left.text == 'open':
        pushleft = pb.push_note("Garage Info", "Left Closing")
        closeleft = requests.get('http://<controller IP or url>/clk?id=left')
        time.sleep(15)

rightcheckup = requests.get('http://<controller IP or url>/st?id=right')
time.sleep(2)
leftcheckup = requests.get('http://<controller IP or url>/st?id=left')

if rightcheckup.text == 'open':
        pushright = pb.push_note("Garage Info", "Right Closing")
        closeright = requests.get('http://<controller IP or url>/clk?id=right')
        time.sleep(15)
elif leftcheckup.text == 'open':
        pushleft = pb.push_note("Garage Info", "Left Closing")
        closeleft = requests.get('http://<controller IP or url>/clk?id=left')
        time.sleep(15)

rightfinal = requests.get('http://<controller IP or url>/st?id=right')
time.sleep(2)
leftfinal = requests.get('http://<controller IP or url>/st?id=left')

if rightfinal.text == 'open':
        pushright = pb.push_note("Garage Info", "Right Door STUCK")
        time.sleep(8)
elif leftfinal.text == 'open':
        pushleft = pb.push_note("Garage Info", "Left Door STUCK")
        closeleft = requests.get('http://<controller IP or url>/clk?id=left')


if (rightfinal.text == 'closed' and leftfinal.text == 'closed'):
        pushfinal = pb.push_note("Garage Info", "Both doors closed.")

