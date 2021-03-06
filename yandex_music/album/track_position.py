from typing import TYPE_CHECKING, Optional

from yandex_music import YandexMusicObject

if TYPE_CHECKING:
    from yandex_music import Client


class TrackPosition(YandexMusicObject):
    """Класс, представляющий .

    Attributes:
        client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

    Args:
        client (:obj:`yandex_music.Client`, optional): Объект класса :class:`yandex_music.Client`, представляющий клиент
            Yandex Music.
        **kwargs: Произвольные ключевые аргументы полученные от API.
    """

    def __init__(self,
                 volume: int,
                 index: int,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.volume = volume
        self.index = index

        self.client = client
        self._id_attrs = (self.volume, self.index)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['TrackPosition']:
        """Десериализация объекта.

        Args:
            data (:obj:`dict`): Поля и значения десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`yandex_music.TrackPosition`: Объект класса :class:`yandex_music.TrackPosition`.
        """
        if not data:
            return None

        data = super(TrackPosition, cls).de_json(data, client)

        return cls(client=client, **data)
