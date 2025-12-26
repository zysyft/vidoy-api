from flask import Flask, request, redirect, abort
import requests, re, html

app = Flask(__name__)

@app.route("/vidoy")
def vidoy():
    vid = request.args.get("id")
    if not vid:
        abort(400)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://vidoy.com/",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }

    r = requests.get(
        "https://simemek.com/embed.php",
        params={"bucket": "vidoycdn", "id": vid},
        headers=headers,
        timeout=15
    )

    m = re.search(r'<source[^>]+src="([^"]+)"', r.text, re.I)
    if not m:
        abort(404)

    mp4 = html.unescape(m.group(1))
    return redirect(mp4, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
