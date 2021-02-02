from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class ShortUrl(BaseModel):
    __tablename__ = 'short_urls'

    id = Column(Integer, primary_key=True)
    short_url = Column(String, nullable=False, unique=True)
    full_url = Column(String, nullable=False, unique=True)
    created = Column(DateTime, nullable=False, default=datetime.now())
