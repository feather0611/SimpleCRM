# Simple CRM - Backend

使用Python 3.10.6 + flask

### Database

使用MySQL，DB內容在 `db_content`

### local運行方式

請將 `app/config.py`的DB連線資訊更改成local DB連線資訊

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
