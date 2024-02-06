from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column()
    user_id: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column(String(30))
    phone: Mapped[str] = mapped_column(String(13))

    def __repr__(self):
        return f"User (id={self.id!r}), {self.name!r} - {self.phone!r}"


class File(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column()
    notification_id: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column(String(80))
    data: Mapped[str] = mapped_column(String())     # base64 string

    def __repr__(self):
        return f"{self.name} (id: {self.id})"


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True)
    guid: Mapped[str] = mapped_column(String(40))

    # todo: определиться как хранить пользователя: по номеру или по ID
    receiver: Mapped[str] = mapped_column(String(13))   # phone
    user_id: Mapped[int] = mapped_column()              # ID

    text: Mapped[str] = mapped_column(String(350))
    message_id: Mapped[int] = mapped_column(nullable=True)

    mark: Mapped[bool] = mapped_column()

    def __repr__(self):
        return f"ID: {self.guid}"


class Host(Base):
    __tablename__ = "hosts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    user: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()

    def __repr__(self):
        return self.name
