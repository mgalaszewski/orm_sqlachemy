from datetime import date, datetime
from base import Session, engine, Base
from model import Domains, Offers

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 define add data
OtoDom = Domains(datetime(2021, 4, 17, 15, 25), 'OtoDom', '{OtoDom,www.otodom.pl,otodom.pl}', True)
Morizon = Domains(datetime(2021, 5, 17, 14, 33), 'Morizon', '{Morizon,www.morizon.pl}', True)


# 5 - persists data
session.add(OtoDom)
session.add(Morizon)

# 10 - commit and close session
session.commit()
session.close()