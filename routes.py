from flask import Blueprint, jsonify, request
from models import Episode, Guest, Appearance, db

episodes_bp = Blueprint('episodes_bp', __name__)

@episodes_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    episodes_list = [episode.to_dict(only=('id', 'date', 'number')) for episode in episodes]
    return jsonify(episodes_list), 200

@episodes_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode_by_id(id):
    episode = Episode.query.get(id)

    if episode:
        return jsonify(episode.to_dict()), 200
    else:
        return jsonify({"error": "Episode not found"}), 404
    
@episodes_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    guest_list = [guest.to_dict() for guest in guests]
    return jsonify(guest_list), 200

@episodes_bp.route('/appearances', methods=['POST'])
def create_appearance():
    try:
        data = request.get_json()
        rating = data.get('rating')
        episode_id = data.get('episode_id')
        guest_id = data.get('guest_id')

        # Validate episode and guest exist
        episode = Episode.query.get(episode_id)
        guest = Guest.query.get(guest_id)

        if not episode or not guest:
            return jsonify({"errors": ["Invalid episode_id or guest_id"]}), 422

        appearance = Appearance(
            rating=rating,
            episode=episode,
            guest=guest
        )

        db.session.add(appearance)
        db.session.commit()

        return jsonify(appearance.to_dict()), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 422
