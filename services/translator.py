# I'm not super happy with how I organized this. Instead of creating a nice service layer, it seems I ended up creating
# a junk-drawer module. I'm sure I'll know exactly what went sideways here in the morning.
import base36
from random import randrange
from sqlalchemy import create_engine # <- Look, ma! An import with no use!

from repository import ShortUrl, session


# There is exactly zero data validation going on here. There should be a check that the URL being created is, in fact,
# a valid URL.
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
