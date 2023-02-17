import socket

# Define the URL of the page to scrape

url = "time.com"

port = 80

# Create a TCP socket and connect to the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((url, port))

# Send an HTTP request to the server and get the response

request = f"GET / HTTP/1.1\r\nHost: {url}\r\n\r\n"

s.sendall(request.encode())

response = s.recv(4096).decode()

# Extract the latest stories from the HTML response

start_tag = "<h2 class=\"title\">"

end_tag = "</h2>"

latest_stories = []

while True:

    start_index = response.find(start_tag)

    if start_index == -1:

        break

    end_index = response.find(end_tag, start_index)

    latest_stories.append(response[start_index + len(start_tag):end_index])

    response = response[end_index:]

latest_stories = latest_stories[:6]

# Print the titles of the latest stories

for i, story in enumerate(latest_stories):

    print(f"{i+1}. {story.strip()}")
