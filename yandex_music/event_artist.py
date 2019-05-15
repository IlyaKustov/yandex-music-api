from yandex_music import YandexMusicObject


class EventArtist(YandexMusicObject):
    def __init__(self,
                 artist,
                 tracks,
                 similar_to_artists_from_history,
                 client=None,
                 **kwargs):
        self.artist = artist
        self.tracks = tracks
        self.similar_to_artists_from_history = similar_to_artists_from_history

        self.client = client

    @classmethod
    def de_json(cls, data, client):
        if not data:
            return None

        data = super(EventArtist, cls).de_json(data, client)
        from yandex_music import Artist, Track
        data['artists'] = Artist.de_json(data.get('artist'), client)
        data['tracks'] = Track.de_list(data.get('tracks'), client)
        data['similar_to_artists_from_history'] = Artist.de_list(data.get('similar_to_artists_from_history'), client)

        return cls(client=client, **data)

    @classmethod
    def de_list(cls, data, client):
        if not data:
            return []

        event_artists = list()
        for event_artist in data:
            event_artists.append(cls.de_json(event_artist, client))

        return event_artists
