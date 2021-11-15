# -*- coding: utf-8 -*-

from model.add_contact import Add_contact



def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(Add_contact(name="Alex", lastname="Tyat", address="11 Nansen road"))
    app.session.logout()

