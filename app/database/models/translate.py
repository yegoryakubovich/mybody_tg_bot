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


from peewee import PrimaryKeyField, ForeignKeyField, CharField

from app.database.db import BaseModel
from app.database.models import Language
from app.database.models import Text


class Translate(BaseModel):
    id = PrimaryKeyField()
    language = ForeignKeyField(Language, to_field='id')
    text = ForeignKeyField(Text, to_field='id')
    value = CharField()

    def get_by_value(self, account: Account, value: str, text: Text):
        translate = Translate.get_or_none((Translate.value == value) & (Translate.language == account.language) &
                                          (Translate.text == text))

        if not translate:
            translate = Translate.get_or_none((Translate.value == value) & (Translate.text == text))
        return translate

    class Meta:
        db_table = 'translates'
