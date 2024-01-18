FROM python:3.10.6

WORKDIR /backend

ENV DB_USERNAME=test
ENV DB_PASSWORD=12345678
ENV DB_URL=localhost
ENV DB_PORT=3306
ENV DB_NAME=database
ENV APP_HOST=127.0.0.1
ENV APP_PORT=5000

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]