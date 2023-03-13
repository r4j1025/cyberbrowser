import mysql.connector
import Levenshtein

def check_url_similarity(url, table_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="url_database"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT url FROM {}".format(table_name))
    existing_urls = [row[0] for row in mycursor.fetchall()]

    similarities = []
    for existing_url in existing_urls:
        distance = Levenshtein.distance(url, existing_url)
        similarity = 100 - ((distance / len(existing_url)) * 100)
        similarities.append(similarity)

    max_similarity = max(similarities)
    print("Input URL :",url)
    if max_similarity >= 100:
        print("The input URL is similar to an existing URL",existing_url," in the table.\nSimilarity percentage: {:.2f}%".format(max_similarity))
    else:
        print("The input URL is not similar to any URL in the table.")

url1='http://example.com'
check_url_similarity(url1,'urls')


