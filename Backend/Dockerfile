FROM python:3.8.10

WORKDIR /backend/

RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /backend/

EXPOSE 8080

CMD [ "python", "app.py" ] 
