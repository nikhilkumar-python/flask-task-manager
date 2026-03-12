class Config:
    SECRET_KEY = "mysecretkey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///tasks.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False