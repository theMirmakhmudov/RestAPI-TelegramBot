FROM python:3.11

WORKDIR /apps


COPY . /apps

# Kerakli kutubxonalarni o‘rnatamiz
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Asosiy bot faylini ishga tushiramiz
CMD ["python", "main.py"]
