from datetime import datetime

from assertpy import assert_that
from hamcrest import (
    has_property,
    has_properties,
    equal_to,
    all_of,
    starts_with,
    instance_of,
)


class PostV1Acccount:

    @classmethod
    def check_response_values(
            cls,
            response
    ):
        assert_that(
            response, all_of(
                has_property('resource', has_property('login', starts_with('nikita'))),
                has_property('resource', has_property('registration', instance_of(datetime))),
                has_property(
                    'resource', has_properties(
                        {
                            'rating': has_properties(
                                {
                                    "enabled": equal_to(True),
                                    "quality": equal_to(0),
                                    "quantity": equal_to(0)
                                }
                            )
                        }
                    )
                )
            )
        )
