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


from peewee import PrimaryKeyField, ForeignKeyField

from app.database.db import BaseModel
from app.database.models import Account
from app.database.models import Text
from app.database.models import Translate


class TagParameter(BaseModel):
    id = PrimaryKeyField()
    name = ForeignKeyField(Text, to_field='id', on_delete='cascade')

    def get_by_name(self, account: Account, name: str):
        for tag_parameter in TagParameter.select():
            translate = Translate().get_by_value(account=account, value=name, text=tag_parameter.name)
            print(tag_parameter, translate)
            if translate:
                return tag_parameter

    def name_get(self, account: Account):
        translate = Translate.get_or_none((Translate.language == account.language) & (Translate.text == self.name))
        if not translate:
            translate = Translate.get(Translate.text == self.name)
        return translate.value

    class Meta:
        db_table = 'tags_parameters'
