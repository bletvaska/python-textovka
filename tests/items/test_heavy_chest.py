import pytest

from items.heavy_chest import HeavyChest


@pytest.mark.items
@pytest.mark.heavy_chest
class TestSuiteHeavyChest:

    @pytest.fixture(scope='class')
    def item(self):
        yield HeavyChest()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'tazka okovana truhlica'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Je vybavená masívnym zámkom...'

    def test_when_created_then_expect_no_features(self, item):
        assert item.features == [], 'Features should be empty'
