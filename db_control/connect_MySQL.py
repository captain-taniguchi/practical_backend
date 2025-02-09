from sqlalchemy import create_engine

import os
from dotenv import load_dotenv #.envファイルを読み込むためのライブラリ

# 環境変数の読み込み
load_dotenv()

# データベース接続情報
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# .envの疎通確認
print("DB_USER:", os.getenv("DB_USER")) 
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
print("DB_NAME:", os.getenv("DB_NAME"))

# SSL証明書のパス
ssl_cert=str('DigiCertGlobalRootCA.crt.pem')
print("ssl_cert:", ssl_cert)

# MySQLのURL構築
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?ssl_ca=DigiCertGlobalRootCA.crt.pem&ssl_verify_cert=true" #0208SSL追加

# エンジンの作成
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_recycle=3600
)
