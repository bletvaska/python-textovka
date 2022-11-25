import pytest

from items.features import USABLE, MOVABLE
from items.whip import Whip


@pytest.fixture
def item():
    return Whip()


def test_when_created_then_expect_specific_name(item):
    assert item == 'bic'


def test_when_created_then_expect_specific_description(item):
    assert item.description == 'Tvoj neoceniteľný pomocník..!'


@pytest.mark.parametrize("feature", [MOVABLE, USABLE])
def test_when_created_then_expect_features_movable_and_usable(item, feature):
    assert feature in item.features
