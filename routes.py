from flask import Blueprint, jsonify
from models import Episode

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
