import uuid
import json
from pprint import pprint


class Poll(object):
    def __init__(self, question, options, _id=None):
        self.queston = question
        self.options = options
        self._id = uuid.uuid4().hex if _id is None else _id


    @staticmethod
    def emoji_dict(num):
        emoji_dict = {1: ":one:",
                     2: ":two:",
                     3: ":three:",
                     4: ":four:",
                     5: ":five:",
                     6: ":six:",
                     7: ":seven:",
                     8: ":eight:",
                     9: ":nine:",
                     10: ":keycap_ten:"}
        return emoji_dict[num]

    @classmethod
    def create_poll(cls, poll):
        question = poll[0]
        options = poll[1:]
        formated_options = ""
        actions = list()
        count = 0
        for option in options:
            count += 1
            option_stg = "{} {}\n".format(cls.emoji_dict(count), options[count - 1])
            formated_options = formated_options + option_stg
            actions.append({"name": "game",
                            "text": "{}".format(cls.emoji_dict(count)),
                            "type": "button",
                            "value": "{}".format(cls.emoji_dict(count))})
        poll_head = {
                    "text": question,
                    "response_type": "in_channel",
                    "attachments": [
                                        {
                                            "text": formated_options,
                                            "fallback": "You are unable to choose a game",
                                            "callback_id": "wopr_game",
                                            "color": "#3AA3E3",
                                            "attachment_type": "default",
                                            "actions": actions
                                        }
                                   ]
                    }
        return poll_head



