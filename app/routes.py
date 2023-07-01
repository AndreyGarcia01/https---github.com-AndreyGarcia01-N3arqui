from flask import request, jsonify, redirect
from app import app, db, cache
from app.models import URL

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('url')
    
    if not original_url:
        return jsonify({'error': 'Missing URL parameter.'}), 400
    
    url = URL.query.filter_by(original_url=original_url).first()
    if url:
        return jsonify({'short_url': url.short_url}), 200
    
    new_url = URL(original_url=original_url)
    db.session.add(new_url)
    db.session.commit()
    
    return jsonify({'short_url': new_url.short_url}), 201

@app.route('/<string:short_url>')
def redirect_to_url(short_url):
    url = cache.get(short_url)
    
    if not url:
        url = URL.query.filter_by(short_url=short_url).first()
        if not url:
            return jsonify({'error': 'Invalid short URL.'}), 404
        cache.set(url.short_url, url.original_url, timeout=app.config['CACHE_TTL'])
    
    return redirect(url)

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Page not found.'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error.'
