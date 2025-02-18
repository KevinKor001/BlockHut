from tqdm import tqdm
import requests
import venv


VENV_DIR = "BlockHut_venv"

print("RUNS")
chunk_size = 1024
url = "http://kevinblog.sytes.net/wp-content/uploads/2025/02/teacherClean-1536x960.png"



def Download(ch_Size = chunk_size, URL = url, FileName = "NN"):
    if FileName == "NN":
        print("WARNING , NO FILE NAME PARAMETER")
        return("NN")
    print("Begin Download")
    r = requests.get(URL, stream=True)
    total_size = int(r.headers['content-length'])

    with open(FileName, "wb") as file:
        for data in tqdm(r.iter_content(chunk_size= chunk_size), total= total_size/chunk_size, unit= 'KB'):
            file.write(data)


#Download()