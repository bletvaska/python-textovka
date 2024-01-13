import pytest

from adventure.items.features import MOVABLE
from adventure.items.map import Map


@pytest.mark.items
@pytest.mark.map
class TestSuiteMap:

    @pytest.fixture
    def item(self):
        yield Map()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'mapu'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == ('Je to mapa okolia tábora. [bold green]Oáza[/bold green] na [bold yellow]sever['
                                    '/bold yellow] od tábora je označená krížikom a nič nehovoriacim slovom "HIER".')

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'
