#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name, knowledge=None):
        self.first_name = first_name
        self.last_name = last_name
        if knowledge is None:
            self.knowledge = []
        else:
            self.knowledge = knowledge

    pass