# Copyright (c) 2022 Joseph Hale
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from typing import Dict


class MultiCounter:
    def __init__(self):
        self._counters = {}

    def __getattr__(self, name: str) -> int:
        if name not in self._counters.keys():
            self._counters[name] = 0
        return self._counters[name]

    def __setattr__(self, name: str, value: int) -> None:
        if name[0] == "_":
            super().__setattr__(name, value)
        else:
            self._counters[name] = value

    def get_counters(self) -> Dict[str, int]:
        return self._counters

    def __str__(self) -> str:
        return str(self._counters)
