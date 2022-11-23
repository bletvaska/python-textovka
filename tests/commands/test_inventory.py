import pytest

from commands import Inventory


@pytest.fixture
def cmd():
    return Inventory()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'inventar'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'zobrazí obsah hráčovho batohu'


def test_when_backpack_is_empty_then_expect_specific_message_on_stdout(cmd, capsys):
    cmd.exec([])
    captured = capsys.readouterr()

    assert captured.out == 'Batoh je prázdny.\n'


def test_when_backpack_has_items_then_print_its_content_on_stdout(cmd, capsys):
    backpack = ['revolver', 'bic']
    cmd.exec(backpack)
    captured = capsys.readouterr()

    assert captured.out == 'V batohu máš:\nrevolver\nbic\n'
