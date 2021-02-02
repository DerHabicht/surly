from flask import Flask, jsonify, make_response, redirect, request

from services.translator import shorten, lookup_url


app = Flask(__name__)


# Ideally, this route would return 201 if it actually created a new URL, and 200 only if it didn't create a new one.
@app.route('/', methods=['POST'])
def create_short_url():
    try:
        u = shorten(request.json['url'])
    except (TypeError, KeyError):
        return make_response(jsonify({
            'error': 'Request body malformed',
            }),
            400,
        )

    return jsonify({
        'full_url': u.full_url,
        'short_url': u.short_url,
        'created': u.created,
    })


@app.route('/<short_url>', methods=['GET'])
def get_full_url(short_url):
    u = lookup_url(short_url)
    if u:
        # I use a temporary redirect here because I don't want to pollute my browser cache. Whether this should be
        # temporary or permanent depends on exactly why we'd be deploying a URL shortener and how durable we want
        # the shortened links to actually be.
        return redirect(u.full_url, 307)
    else:
        return make_response(
            jsonify({'error': f'{short_url} does not map to a full url'}),
            404,
        )


if __name__ == '__main__':
    app.run()
