import requests
from pyfiglet import Figlet
import folium
def get_info_by_ip(ip):
    try:
        response = requests.get(url = f"https://ipinfo.io/{ip}/json").json()
        loc = response.get('loc', '0,0').split(',')
        data = {
            '[ip]' : response.get('ip', 'N/A'),
            '[internet Service Provider]' : response.get('isp'),
            '[organization]' : response.get('org'),
            '[city]' : response.get('city'),
            '[region]' : response.get('region'),
            '[zip]' : response.get('postal'),
            '[country]' : response.get('country'),
            '[lat]' : float(loc[0]),
            '[lon]' : float(loc[1]),
        }
        
        for k , v in data.items():
            print(f"{k} : {v}")
            
        area = folium.Map(location=[data['[lat]'], data['[lon]']])
                          #this function  disabled     #area.save(f"{response.get('ip')}_{response.get('city')}.html")
            
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
        
def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IPD'))
    ip = input("Enter an IP address: ")
    get_info_by_ip(ip=ip)
if __name__ == "__main__":
    main()