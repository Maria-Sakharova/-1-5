import sys
sys.path.insert(0, 'lib/postgresql/src/interfaces/python')

try:
    import psycopg2
except ImportError:
    print('PostgreSQL library not yet configured')
    print('This is a mock for the practical work')
