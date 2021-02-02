import base36
from random import randrange
from sqlalchemy import create_engine

from repository import ShortUrl, session


def create_short_url(full_url: str) -> ShortUrl:
    print(f'Creating new short url for {full_url}')
    short_url = ShortUrl()
    short_url.full_url = full_url
    short_url.short_url = base36.dumps(randrange(36 ** 8))

    session.add(short_url)
    session.commit()

    return short_url


def shorten(full_url: str) -> ShortUrl:
    url = session.query(ShortUrl).filter(ShortUrl.full_url == full_url).first()
    return url if url else create_short_url(full_url)


def lookup_url(short_url: str) -> ShortUrl:
    return session.query(ShortUrl).filter(ShortUrl.short_url == short_url).first()
