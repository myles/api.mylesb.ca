# -*- coding: utf-8 -*-
"""Schema unit tests."""
from api.schema import schema


class TestAbout:
    """Schema tests."""

    def test_get_first_name(self):
        r = schema.execute("""
            query Myles {
                about {
                    fullName
                    age
                }
            }
        """)

        assert r.data == {'about': {'fullName': 'Myles Braithwaite',
                                    'age': 30}}
