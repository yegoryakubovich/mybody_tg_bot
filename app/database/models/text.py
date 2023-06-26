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


from peewee import PrimaryKeyField

from app.database.db import BaseModel
from app.database.models import Account
from app.database.models import Language
from app.database.models import Translate


class Text(BaseModel):
    id = PrimaryKeyField()

    def default_create(self, value: str):
        translate = Translate(language=Language.get(Language.id == 2), text=self, value=value)
        translate.save()

    def value_get(self, account: Account):
        translate = Translate.get_or_none((Translate.language == account.language) & (Translate.text == self))
        if not translate:
            translate = Translate.get(Translate.text == self)
        return translate.value

    def value_set(self, account: Account, value: str):
        translate = Translate.get_or_none((Translate.language == account.language) & (Translate.text == self))
        if not translate:
            translate = Translate(language=account.language, text=self)
        translate.value = value
        translate.save()

    class Meta:
        db_table = 'texts'
