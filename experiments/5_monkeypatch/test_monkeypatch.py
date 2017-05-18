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
