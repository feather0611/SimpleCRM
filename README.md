# Simple CRM - Backend

使用Python 3.10.6 + flask

### ENVs for Docker
```
ENV DB_USERNAME = test
ENV DB_PASSWORD = 12345678
ENV DB_URL = localhost
ENV DB_PORT = 3306
ENV DB_NAME = database
ENV APP_HOST=127.0.0.1
ENV APP_PORT=5000
```

### Database

使用MySQL，DB內容在 `db_content`

### local運行方式

Windows進到專案資料夾中
```
python -m venv venv
```
建立好虛擬環境後啟用
```
.\venv\Scripts\activate
```
出現(venv)開頭之後再執行
```
pip install -r requirements.txt
```
安裝完成後便可執行
```
python app.py
```
