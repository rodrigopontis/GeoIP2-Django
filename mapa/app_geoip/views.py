from django.shortcuts import render, HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
import geoip2.database
import folium


# def home(request):
#     return render(request, 'mapamundi/teste.html')
def home2(request):

    # Pega metadados do request
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')

    m = folium.Map(location=[19, -12], zoom_start=2)

    m = m._repr_html_()

    ip = '179.83.85.15'
    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""

    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"

    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string

    g = GeoIP2()
    location = g.city(ip)

    latitude = location["latitude"]
    longitude = location["longitude"]
    # state_name = location.get("subdivisions", [])[1].get("name")

    location_country = location["country_name"]
    location_city = location["city"]

    context = {
        "ip": ip,
        "device_type": device_type,
        "browser_type": browser_type,
        "browser_version": browser_version,
        "os_type": os_type,
        "os_version": os_version,
        # "continente": continent,
        "location_country": location_country,
        "location_city": location_city,
        "latitude": latitude,
        "longitude": longitude,
        "m": m
        # "state_name": state_name


    }
    return render(request, "site/index.html", context)
