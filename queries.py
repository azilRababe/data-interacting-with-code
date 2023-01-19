# pylint: disable=missing-docstring, C0103


def directors_count(db):
    # return the number of directors contained in the database
    query = "SELECT count(*) FROM directors "
    db.execute(query)
    results = db.fetchall()
    return results[0][0]

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = "select * from directors order by name"
    db.execute(query)
    results = db.fetchall()
    return [x[0] for x in results]

def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = "SELECT * from movies where upper(title) like '% LOVE %' ORDER by title"
    db.execute(query)
    results = db.fetchall()
    return results

def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = f"SELECT  count(*) from directors where upper(name) like '%{name}%'"
    db.execute(query)
    results = db.fetchall()
    return results[0][0]


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = f"select * from movies WHERE minutes > {min_length} ORDER by title"
    db.execute(query)
    results = db.fetchall()
    return [x[0] for x in results]
