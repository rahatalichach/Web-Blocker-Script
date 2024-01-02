Web Blocker Script

This Python script is designed to block access to specific websites by modifying the hosts file on a Windows system.
The script allows you to specify a list of websites to block and a time when the blocking should be activated. 
After the specified time, the script will remove the block from the hosts file.

Usage:

Edit the site_block list to include the websites you want to block.
Set the block_time variable to the date and time when the blocking should start.
Run the script as an administrator.
Important:

Modifying the hosts file requires administrator privileges.
Use this script responsibly and ensure compliance with ethical and legal standards.
The script uses a sleep time of 5 seconds between iterations; adjust as needed based on your requirements.
Example:

python
Copy code
python web_blocker.py
Note:
Please be aware that this script is intended for educational purposes and ethical use. Blocking access to websites without consent may violate terms of service and legal agreements.
