# pylint: disable = W0223
"""Serializers for the Prototype API View.

Notes:
    W0223: Disable `Method is abstract in class but is not overridden(Pylint type
    checking)`.
"""
# 3rd Party Libraries
from rest_framework import serializers


class PrototypeSerializer(serializers.Serializer):
    """Proxy Serializer.

    Notes:
        Can be implemented/extended as per needs.
    """

    pass
