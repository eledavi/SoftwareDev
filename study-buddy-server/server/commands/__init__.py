"""

Dragonfly
Cyrille Gindreau
2017

__init__.py

Sets up commands that are run from run.py

"""
import loadfixtures


class Command:
    @staticmethod
    def LoadFixtures():
        loadfixtures.loadfixtures()
