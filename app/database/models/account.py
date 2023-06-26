#
# (c) 2023, Yegor Yakubovich, yegoryakubovich.com, personal@yegoryakybovich.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from peewee import PrimaryKeyField, IntegerField, ForeignKeyField, CharField

from app.database.db import BaseModel
from app.database.models import Translate
from app.database.models import Text
from app.database.models import Language
from config import SETTINGS_TEXT_404


class Account(BaseModel):
    id = PrimaryKeyField()
    adecty_account_id = IntegerField()
    language = ForeignKeyField(Language, to_field='id')
    first_name = CharField()
    last_name = CharField()
    middle_name = CharField(null=True)
    gender = CharField()
    telegram = CharField(null=True)
    timezone = CharField()

    def text_get(self, key):
        text = Text.get_or_none(Text.key == key)
        if not text:
            return SETTINGS_TEXT_404

        translate = Translate.get_or_none((Translate.text == text) & (Translate.language == self.language))
        if not translate:
            translate = Translate.get(Translate.text == text)

        return translate.value

    class Meta:
        db_table = 'accounts'
