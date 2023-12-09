import peewee
import datetime
import json
import os
import config

database = peewee.SqliteDatabase(".game.db")


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Setting(BaseModel):
    theme = peewee.CharField(max_length=2, default="s")
    difficulty = peewee.CharField(max_length=1, default="m")
    spaceship_speed = peewee.IntegerField(default=config.spaceship_default_speed)


class Record(BaseModel):
    name = peewee.CharField(max_length=25)
    score = peewee.IntegerField(default=0)
    created_time = peewee.DateTimeField(
        default=datetime.datetime.now(), formats="%Y-%m-%d %H:%M:%S"
    )


class Statistic(BaseModel):
    coin_count = peewee.IntegerField(default=0)
    score = peewee.IntegerField(default=0)
    lose = peewee.IntegerField(default=0)
    game_count = peewee.IntegerField(default=0)


def database_init():
    if not os.path.isfile(".game.db"):
        with database:
            database.create_tables([Setting, Record, Statistic])
            Setting.create()
            Statistic.create()
