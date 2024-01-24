from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

base_psql = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'postgres',
          'USER': 'postgres',
          'PASSWORD': 'postgres',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }

base_sqlite = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}