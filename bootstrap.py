from ascender.core.database.provider import DatabaseProvider
from ascender.core.database.types.orm_enum import ORMEnum
from ascender.core.types import IBootstrap
from ascender.core.utils.controller_module import ProvideControllers
from aschttp.provider import ProvideHTTPClient
from controllers.controllers_module import ControllersModule
from settings import DATABASE_CONNECTION


appBootstrap: IBootstrap = {
    "providers": [
        DatabaseProvider(ORMEnum.SQLALCHEMY, DATABASE_CONNECTION), # type:ignore
        ProvideControllers([
            ControllersModule
        ]),
        ProvideHTTPClient()
    ]
}