# import psycopg2

# conn = psycopg2.connect(
#     host="postgres",
#     port="5432",
#     database="postgres",
#     user="super_admin",
#     password="SomeSecretPassword"
# )

# cursor = conn.cursor()
# cursor.execute("SELECT")
# result = cursor.fetchone()
# print("success")

# cursor.close()
# conn.close()




import psycopg2
import logging

# Set up the logging configuration
logging.basicConfig(level=logging.INFO)

# Open a connection to the database
try:
    conn = psycopg2.connect(
        host="localhost",
        user="super_admin",
        password="SomeSecretPassword",
        dbname="postgres",
        sslmode="disable"


        # host=print(os.environ.get('DB_HOST')),
        # user=os.environ.get('DB_USER'),
        # password=os.environ.get('DB_PASSWD'),
        # dbname=os.environ.get('DB_DBNAME'),
        # sslmode=os.environ.get('DB_SSLMODE')
    )


    logging.info("Successfully connected to the PostgreSQL database")
except psycopg2.Error as e:
    logging.error("Error connecting to the PostgreSQL database")
    logging.error(e)
    exit()

# Close the connection
conn.close()

logging.info("success")


















# from http.server import BaseHTTPRequestHandler, HTTPServer

# class RequestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/plain; charset=utf-8")
#         self.end_headers()
#         self.wfile.write("Hello, World!".encode("utf-8"))

# def main():
#     server_address = ("", 8080)
#     httpd = HTTPServer(server_address, RequestHandler)
#     print("Server is running on http://localhost:8080")
#     httpd.serve_forever()

# if __name__ == "__main__":
#     main()

