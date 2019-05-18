FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "sh", "-c", "./run.py -c config.py"]