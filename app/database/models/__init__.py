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


from app.database.models.account import Account
from app.database.models.account_parameter import AccountParameter
from app.database.models.admin import Admin
from app.database.models.article import Article
from app.database.models.article_item import ArticleItem
from app.database.models.item import Item
from app.database.models.language import Language
from app.database.models.parameter import Parameter
from app.database.models.teg_parameter import TagParameter
from app.database.models.text import Text
from app.database.models.translate import Translate

__all__ = (
    Account,
    Language,
    Admin,
    Text,
    Translate,
    Item,
    TagParameter,
    Article,
    ArticleItem,
    Parameter,
    AccountParameter
)


models = (
    Account,
    Language,
    Admin,
    Text,
    Translate,
    Item,
    TagParameter,
    Article,
    ArticleItem,
    Parameter,
    AccountParameter
)
