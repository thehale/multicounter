# Copyright (c) 2022 Joseph Hale
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import pytest

from multicounter import __version__
from multicounter import MultiCounter


@pytest.fixture
def mc():
    return MultiCounter()


def test_version():
    assert __version__ == "0.1.0"


def test_new_multicounter_has_no_counters(mc):
    assert mc.get_counters() == {}


def test_can_initialize_new_counter(mc):
    mc.cookies
    assert mc.get_counters() == {"cookies": 0}


def test_can_initialize_new_counter_to_specific_value(mc):
    mc.cookies = 42
    assert mc.cookies == 42


def test_can_initialize_multiple_counters(mc):
    mc.cookies = 42
    mc.pies = 3
    assert mc.get_counters() == {"cookies": 42, "pies": 3}


def test_can_increment_counter(mc):
    mc.cookies = 0
    assert mc.cookies == 0
    mc.cookies += 1
    assert mc.cookies == 1


def test_can_increment_new_counter(mc):
    mc.cookies += 1
    assert mc.cookies == 1


def test_incrementing_one_counter_does_not_increment_other_counters(mc):
    mc.cookies = 0
    mc.pies = 0
    mc.cookies += 1
    assert mc.get_counters() == {"cookies": 1, "pies": 0}


def test_can_stringify_multicounter(mc):
    mc.cookies = 42
    mc.pies = 3
    assert "'cookies': 42" in str(mc)
    assert "'pies': 3" in str(mc)


def test_can_count_backwards(mc):
    mc.cookies -= 1
    assert mc.cookies == -1
