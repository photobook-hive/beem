import unittest
import mock
from steem import Steem
from steem.message import Message
from steem.instance import set_shared_steem_instance

wif = "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"
core_unit = "PPY"


class Testcases(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bts = Steem(
            nobroadcast=True,
            wif=[wif]
        )
        set_shared_steem_instance(self.bts)

    def test_sign_message(self):
        def new_refresh(self):
            dict.__init__(
                self, {
                    "name": "test",
                    "options": {
                        "memo_key": "STM6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"
                    }})

        with mock.patch(
            "steem.account.Account.refresh",
            new=new_refresh
        ):
            p = Message("message foobar").sign()
            Message(p).verify()

    def test_verify_message(self):
        def new_refresh(self):
            dict.__init__(
                self, {
                    "name": "test",
                    "options": {
                        "memo_key": "STM6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"
                    }})

        with mock.patch(
            "steem.account.Account.refresh",
            new=new_refresh
        ):
            Message(
                "-----BEGIN STEEM SIGNED MESSAGE-----\n"
                "message foobar\n"
                "-----BEGIN META-----\n"
                "account=test\n"
                "memokey=STM6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV\n"
                "block=23814223\n"
                "timestamp=2018-01-24T11:42:33\n"
                "-----BEGIN SIGNATURE-----\n"
                "2034f601e175a25cf9f60a828650301f57c9efab53929b6a82fb413feb8a786fcb3ba4238dd8bece03aee38526ee363324d43944d4a3f9dc624fbe53ef5f0c9a5e\n"
                "-----END STEEM SIGNED MESSAGE-----\n"
            ).verify()

            Message(
                "-----BEGIN STEEM SIGNED MESSAGE-----"
                "message foobar\n"
                "-----BEGIN META-----"
                "account=test\n"
                "memokey=STM6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV\n"
                "block=23814223\n"
                "timestamp=2018-01-24T11:42:33"
                "-----BEGIN SIGNATURE-----"
                "2034f601e175a25cf9f60a828650301f57c9efab53929b6a82fb413feb8a786fcb3ba4238dd8bece03aee38526ee363324d43944d4a3f9dc624fbe53ef5f0c9a5e\n"
                "-----END STEEM SIGNED MESSAGE-----"
            ).verify()