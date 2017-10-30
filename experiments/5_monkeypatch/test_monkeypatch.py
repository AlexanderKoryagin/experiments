import os


def get_dir_content(dir_path):
    return os.listdir(dir_path)


def mock_listdir(path):
    return ['dir1', 'dir2', 'dir3']


def test_mytest1(monkeypatch):
    print get_dir_content('/home/')  # ['alex']
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    print get_dir_content('/home/')  # ['dir1', 'dir2', 'dir3']
    monkeypatch.undo()
    print get_dir_content('/home/')  # ['alex']


# --------------------------------------
import datetime
import pytest

FAKE_TIME = datetime.datetime(2020, 12, 25, 17, 05, 55)

@pytest.fixture
def patch_datetime_now(monkeypatch):

    class mydatetime:
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, 'datetime', mydatetime)


def test_patch_datetime(patch_datetime_now):
    assert datetime.datetime.now() == FAKE_TIME
