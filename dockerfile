# Használj egy könnyű Python-alapot, amiben van pip
FROM python:3.10-slim

# Telepítsük a Tkintert és szükséges X11 komponenseket
RUN apt-get update \
 && apt-get install -y python3-tk tk-dev \
 && rm -rf /var/lib/apt/lists/*

# Készítsük elő a munkakönyvtárat
WORKDIR /app

# Másoljuk be a requirements.txt-t, ha van
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Ha nincs requirements, közvetlenül installáld, amit kell:
# RUN pip install requests

# Másoljuk be az összes forrást
COPY . .

# Alapértelmezett indító parancs
CMD ["python", "main.py"]
