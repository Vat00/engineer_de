import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Настройка подключения (берем данные из скрытого .env)
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

conn_str = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(conn_str)

# 2. EXTRACT: Получаем данные (например, из списка)
data = [
    {'product_name': ' Headphone ', 'price': 50.0, 'sale_date': '2026-05-04'},
    {'product_name': 'Webcam', 'price': 85.0, 'sale_date': '2026-05-04'},
    {'product_name': '  Mousepad', 'price': 15.0, 'sale_date': '2026-05-05'}
]
df = pd.DataFrame(data)

# 3. TRANSFORM: Очистка данных (убираем пробелы по краям)
# Это работа дата-инженера — делать данные качественными
df['product_name'] = df['product_name'].str.strip()

print("Данные готовы к загрузке:")
print(df)

# 4. LOAD: Загрузка в таблицу 'sales' в Postgres
# if_exists='append' значит, что мы добавляем данные к старым, а не удаляем их
df.to_sql('sales', engine, if_exists='append', index=False)

print("\nУспех! Данные улетели в Docker.")
