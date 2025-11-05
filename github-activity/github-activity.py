import http.client
import json
import sys

username = sys.argv[1]
host = "api.github.com"
endpoint = f"/users/{username}/events"

http_client = http.client.HTTPSConnection(host)
http_client.request(
    "GET",
    endpoint,
    headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "Python http.client",
    },
)

response = http_client.getresponse()
data = response.read().decode("utf-8")


# Try parsing as JSON
try:
    push_tracker = 0
    watch_tracker = 0
    create_tracker = 0
    json_data = json.loads(data)
    # print(json.dumps(json_data, indent=2))  # pretty print JSON

    if not isinstance(json_data, list):
        raise Exception(
            f"{json.dumps(json_data["status"])}: {json.dumps(json_data["message"])}"
        )

    print("------------Activity---------------------")
    for d in json_data:
        match d["type"]:
            case "CreateEvent":
                create_tracker += 1
                print(
                    f"- Created a new repository ({d["repo"]["name"]}) at {d["created_at"]}"
                )
            case "WatchEvent":
                watch_tracker += 1
                print(
                    f"- Watched a the repository {d["repo"]["name"]} at {d["created_at"]}"
                )
            case "PushEvent":
                push_tracker += 1
                print(f"- Pushed a commit to {d["repo"]["name"]} at {d["created_at"]}")

    print("------------Stats---------------------")
    print(f"Total CreateEvents: {create_tracker}")
    print(f"Total WatchEvents: {watch_tracker}")
    print(f"Total PushEvents: {push_tracker}")

except json.JSONDecodeError:
    print("Raw response:")
    print(data)
