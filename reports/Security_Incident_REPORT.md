# CyberSheild Security Incident Report
# Incident Summary
A review of web activity log identified a repeated '401 unauthorized' responses associated with IP Address '192.168.0.101'.The response occured during repeated to the  factory machine-status APIs.
# Evidence
- Source IP Address: '192.168.0.101'
- Total Unauthorized Request: '70'
- Repeated Request targeted factory machine-status API.
- The request returned '401 Unauthorized' repeatedly at hourly intervals.
- At '2021-06-26 16:04:00',the client accessed the login page and successfully authenticated.
- After Authentication, the factory machine-status request returned to 200 Success.
# Analysis
The repeated 401 Unauthorized reponses occoured at regurlar hourly intervals for the same factoory machine-status API four endpoint.
The pattern continued untill the user get accessed the login page and successfully authenticated.
After Authentication,the same API requested returned 200 SUCCESS.

This pattern is consist with an session authorization issue.
The available log  evidence does not confirm any malicious activity. 
# Conclusion
Repeated 401 Unauthorized request from 1982.168.0.101 were investigated.
Successfull re-authentication restored normal 200 success responses.
THe activity was assessed as an authentication/session issue , with no confirmed malicious activity.
