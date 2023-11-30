"""Test for __init__.py system version check"""
import sys


def test_sys_version_log(caplog, monkeypatch) -> None:
    """Testing if message logged when system version is too low is correct"""
    monkeypatch.setattr(sys, "version_info", (2, 6, 0))
    import python_ta

    assert caplog.records[0].levelname == "WARNING"
    assert "You need Python 3.7 or later to run PythonTA." in caplog.text
