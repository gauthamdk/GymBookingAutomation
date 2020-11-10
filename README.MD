# Gym Booking Automation

Created to solve the problem of running out of fitness center slots before I wake up. The fitness center is essential to my health during this pandemic where physical activity is limited and all day is spent sitting in front of the computer. 

This automation tool was created using selenium. This is a python library for web automation.
In order to make it completely automated, the MFA for the NYU portal login is accepted using Macro-Droid which is a phone interaction automation app on the Google Play Store.  

The script is run automatically using a cronjob 2 days before the day for booking since that is when the slots open on the portal. 

## Steps

* Selenium opens up Chrome browser. 
* Navigate to fitness website.
* Log in from NYU SSO.
* Move 2 days in advance from portal, select given time and confirm.

## Lessons

* Web Automation
* MFA Automation
* Cronjobs

## Challenges

* Computer needs to be on for script to run. 
* Sometimes web element is not detected. 
