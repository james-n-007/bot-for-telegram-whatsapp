from telegram import PhotoSize
from telegram import TelegramObject


class Animation(TelegramObject):
    
    def __init__(self,
                 file_id,
                 file_unique_id,
                 width,
                 height,
                 duration,
                 thumb=None,
                 file_name=None,
                 mime_type=None,
                 file_size=None,
                 bot=None,
                 **kwargs):
        # Required
        self.file_id = str(file_id)
        self.file_unique_id = str(file_unique_id)
        self.width = int(width)
        self.height = int(height)
        self.duration = duration
        # Optionals
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.bot = bot

        self._id_attrs = (self.file_unique_id,)

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        data = super().de_json(data, bot)

        data['thumb'] = PhotoSize.de_json(data.get('thumb'), bot)

        return cls(bot=bot, **data)

    def get_file(self, timeout=None, **kwargs):
        """Convenience wrapper over :attr:`telegram.Bot.get_file`
        Args:
            timeout (:obj:`int` | :obj:`float`, optional): If this value is specified, use it as
                the read timeout from the server (instead of the one specified during creation of
                the connection pool).
            **kwargs (:obj:`dict`): Arbitrary keyword arguments.
        Returns:
            :class:`telegram.File`
        Raises:
            :class:`telegram.TelegramError`
        """
        return self.bot.get_file(self.file_id, timeout=timeout, **kwargs)
