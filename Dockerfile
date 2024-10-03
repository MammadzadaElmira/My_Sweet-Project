FROM python:3.12

# Çıktının buffer'lanmamasını sağla
ENV PYTHONUNBUFFERED 1

# Çalışma dizinini ayarla
WORKDIR /code

# Gereksinim dosyasını kopyala
COPY requirements.txt /code/

# Sistem paketlerini güncelle
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Python paketlerini yükle
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Uygulamanın kodunu kopyala
COPY ./sweet /code/

# Dışarıya 8000 portunu aç
EXPOSE 8000

# Uygulamayı çalıştır
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]