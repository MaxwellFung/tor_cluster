from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def fetch_url():
    target_url = request.args.get("url")
    if not target_url:
        return "Please provide a 'url' query parameter.", 400

    headers = {"User-Agent": "Mozilla/5.0"}
    proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050",
    }

    try:
        response = requests.get(target_url, headers=headers, proxies=proxies, timeout=10)
        return Response(response.text, content_type=response.headers.get("Content-Type", "text/html"))
    except requests.exceptions.RequestException as e:
        return f"Error occurred: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)