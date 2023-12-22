import sqlite3
import logging

logging.basicConfig(
#    level=logging.DEBUG,
    filename="demo.log",
    format="%(levelname)s %(name)s %(asctime)s %(message)s",
)

conn = None
cursor = None

#  .critical()
#  .error()
#  .warning()
#  .info()
#  .debug()

DB_NAME = 'BLARGH/wombats.db'

logging.info("program starting")

try:
    logging.debug("db name is %s", DB_NAME)
    conn = sqlite3.connect(DB_NAME)
except sqlite3.DatabaseError as err:
    logging.exception(err)
    exit()
else:
    cursor = conn.cursor()
    cursor.execute('select 5 - 4')
    logging.warning("unexpected result: ...")
    for row in cursor.fetchall():
        print(row)
finally:  # clean up r
    if cursor:
        cursor.close()
    if conn:
        conn.close()

logging.info("program ending")
