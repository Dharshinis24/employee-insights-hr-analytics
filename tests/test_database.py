from database import DBConnection

def test_database_connection():
    db = DBConnection()
    conn = db.get_connection()
    assert conn is not None