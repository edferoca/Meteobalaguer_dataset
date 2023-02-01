# -*- coding: utf-8 -*-
import os # libreria de manejo del sistema operativo

print("Install JAVA 8")
os.system(f"apt-get install openjdk-8-jdk-headless -qq > /dev/null")
os.system(f"pip install wget")

print("Obtaining last version of spark")

from bs4 import BeautifulSoup
import requests, wget

#Obtener las versiones de spark la pagina web
url = 'https://downloads.apache.org/spark/' 
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)

# leer la pagina web y obtener las versiones de spark disponibles
link_files = []
for link in soup.find_all('a'):
  link_files.append(link.get('href'))
spark_link = [x for x in link_files if 'spark' in x]  

ver_spark = spark_link[-1][:-1] # obtener la version y eliminar el caracter '/' del final
print(f"Getting version {ver_spark}")

#instalar automaticamente la version deseadda de spark
download_spark = f"https://downloads.apache.org/spark/{ver_spark}/{ver_spark}-bin-hadoop2.tgz"
print(f"Downloading {download_spark}")
file_name = wget.download(download_spark)
os.system(f"tar xf {ver_spark}-bin-hadoop2.tgz")
# instalar pyspark
print("Installing PySpark")
os.system(f"pip install -q pyspark")

"""## Definir variables de entorno"""
print("Setting environment variables for JAVA_HOME and SPARK_HOME")
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = f"/content/{ver_spark}-bin-hadoop2.7"

