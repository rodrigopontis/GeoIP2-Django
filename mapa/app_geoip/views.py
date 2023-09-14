from django.shortcuts import render, HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
import geoip2.database
import folium



def criarMarcacao(request):
    # Sempre que houver uma conexão == Marcar ponto no mapa

    # Atualização de mapa por x periodo

    # Desmarcar ponto no mapa ao perder conexão com ponto
    return 0


def removerMarcacao(request):
    # Sempre que houver uma conexão == Marcar ponto no mapa

    # Atualização de mapa por x periodo

    # Desmarcar ponto no mapa ao perder conexão com ponto
    return 0

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    # Get all the IPLogs.
    ip_logs = IPLog.objects.filter(time__gt=timezone.now() - timedelta(minutes=1))

    # Render the template with the IPLogs.
    template = loader.get_template("index.html")
    context = {
        "ip_logs": ip_logs,
    }
    return HttpResponse(template.render(context, request))



def home2(request):

    # Pega metadados do request
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')

    m = folium.Map(location=[19, -12], zoom_start=2)
    mBrasil = folium.Map(location=[-20, -65], zoom_start=4)


    ip = '181.222.1.53'

    # Informações dispositivo
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

    #Dados do GeoIP2
    g = GeoIP2()
    location = g.city(ip)
    latitude = location["latitude"]
    longitude = location["longitude"]
    location_country = location["country_name"]
    location_city = location["city"]
    myAddress = [latitude, longitude]

    #Criando Marcações
    folium.CircleMarker(location=(myAddress), radius=30,
                        popup="Loc").add_to(m)
    folium.Marker(myAddress, popup="Loc").add_to(m)
    
    # Transformar mapa objeto em elemento html
    mBrasil = mBrasil._repr_html_()
    m = m._repr_html_()

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
        "m": m,
        "mBrasil": mBrasil
        # "state_name": state_name
    }
    return render(request, "site/index.html", context)
