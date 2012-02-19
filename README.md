QuickerAuth 
============ 

QuickerAuth provides a way for your users to login to your mobile
application simply by scanning a QR-code. It is simple, secure and
easy to use. Instead of having to type in a long password the user
simply scans the QR code and gets signed in.

QuickerAuth is platform-agnostic and works just as well for mobile web
applications as for native ones.

How it works
-----------
When the user requests it the desktop app displays a QR code. The user
then scans this code either with a scanning app (e.g. RedLaser) or
with your application. Once the code is scanned the mobile app sends
an HTTP request to your backend. The backend then verifies the code
and replies with an authentication token, which the mobile app stores
and uses for all future API requests.

Why use QuickerAuth?
------------------
A good way to ensure user retention is using mobile apps. The problem
facing users is that the process of downloading and logging into your
application is tedious. QuickerAuth makes authentication super simple.

