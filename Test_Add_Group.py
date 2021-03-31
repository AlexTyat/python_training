# -*- coding: utf-8 -*-

# import unittest
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    wd = self.wd
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test3333", header="test test", footer="test for test"))
    app.logout()


def test_addempty_group(app):
    wd = self.wd
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
