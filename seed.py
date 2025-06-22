import csv
from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():
    # Clear existing data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    # Open and read the CSV file
    with open('lateshow.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Check for existing guest
            guest = Guest.query.filter_by(name=row['guest_name']).first()
            if not guest:
                guest = Guest(
                    name=row['guest_name'],
                    occupation=row['guest_occupation']
                )
                db.session.add(guest)

            # Check for existing episode
            episode = Episode.query.filter_by(number=row['episode_number']).first()
            if not episode:
                episode = Episode(
                    number=row['episode_number'],
                    date=row['episode_date']
                )
                db.session.add(episode)

            # Push new guest/episode so we can get their IDs
            db.session.flush()

            # Create appearance record
            appearance = Appearance(
                guest_id=guest.id,
                episode_id=episode.id,
                rating=int(row['rating'])
            )
            db.session.add(appearance)

        db.session.commit()
        print("Seeding complete!")
