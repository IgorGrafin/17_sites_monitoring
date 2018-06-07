# Sites Monitoring Utility
This script will help you to monitor web-sites. It shows actual status code and days to expiration of the domain.  
## Installation
Install requirements.
```pip install -r requirements.txt```

## How to use
Put a text file which contains web-sites' ulrs you want to monitor as a parameter. Each url on a new line.
See the example below. 
```python.exe E:/GitHub/devman/17_sites_monitoring/check_sites_health.py sites.txt
1) https://devman.org/
Status code - 200
Days to expiration - 81
2) https://www.youtube.com/
Status code - 200
Days to expiration - 252
3) https://www.rbc8.ru/
Status code - No response!
4) https://rbc.ru
Status code - 200
Days to expiration - 53
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
