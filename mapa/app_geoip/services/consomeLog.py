from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import io
file_path=''

def consume_ip_log(file_path):
 #começa a ler pela ultima linha
    with open("my_log.log", "r", newline='') as f:
        f.seek(0, 2)

        while True:
            line = f.readline()
            if line:
                print(line)
            else:
                time.sleep(0.1)

    # ou
    with open(file_path,"r") as f:
        for line in f:
            # Parse the line and create an IPLog object.
            ip_log = IPLog.objects.create(
                ip=line.split(",")[0],
                country=line.split(",")[1],
                city=line.split(",")[2],
                state=line.split(",")[3],
                time=datetime.datetime.now(),
            )