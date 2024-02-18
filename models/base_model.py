#!/usr/bin/python3
"""this module represent base class"""
import uuid
import datetime
import json
import models


class BaseModel:

    """Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):

        """Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs:
            kwargs.pop("__class__")
            for key, v in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    obj = datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, obj)
                else:
                    setattr(self, key, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".format(__class__.__name__, self.id, vars(self))

    def save(self):
        """update the update_At attribute"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dictionary of the instance"""
        self.__dict__['__class__'] = __class__.__name__
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
        return vars(self)
