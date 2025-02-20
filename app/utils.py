from flask import jsonify


def method_unavailable(method):
    return jsonify({
        'error': f'Method {method} not available',
    }), 405
