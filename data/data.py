import sqlalchemy
from .db_session import SqlAlchemyBase


class Data(SqlAlchemyBase):
    __tablename__ = 'data'
    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )
    text = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )

    def __repr__(self):
        return f'{self.id}) {self.name} {self.text}'
