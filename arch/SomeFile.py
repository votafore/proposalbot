from arch.internal.DatabaseUtils import User, Notification
from sqlalchemy import create_engine, String, Integer
from sqlalchemy import select, MetaData, inspect
from sqlalchemy.orm import Session
from arch.internal.DatabaseUtils import Base
import config


engine = create_engine(f"sqlite:///{config.PROJECT_PATH}\\main.db", echo=True, pool_pre_ping=True)


class UsersManager:

    def find_user_by_chat_id(self, chat_id: Integer) -> User:
        with Session(engine) as session:
            try:
                statement = select(User).filter_by(chat_id=chat_id)
                user = session.scalars(statement).one()
                session.close()
            except:
                return None

        return user

    def find_user_by_id(self, id: Integer) -> User:
        with Session(engine) as session:
            try:
                statement = select(User).filter_by(id=id)
                user = session.scalars(statement).one()
                session.close()
            except:
                return None

        return user

    def find_user_by_phone(self, phone: String) -> User:
        with Session(engine) as session:
            statement = select(User).filter_by(phone=phone)
            user = session.scalars(statement).one_or_none()
            session.close()
        return user

    def save_user(self, chat_id: Integer, user_id: Integer, name: String, phone: String) -> bool:
        with Session(engine) as session:
            user = User(chat_id=chat_id, user_id=user_id, name=name, phone=phone)
            try:
                session.add(user)
                session.commit()
            except Exception as e:
                print(e)
                return False

        return True


class ProposalsManager:

    def get_proposal_by_user_id(self, user_id: Integer):
        with Session(engine) as session:
            statement = select(Notification).filter_by(user_id=user_id)
            proposal = session.scalars(statement).one_or_none()
            session.close()
        return proposal

    def get_proposal_by_id(self, message_id: Integer):
        with Session(engine) as session:
            statement = select(Notification).filter_by(message_id=message_id)
            proposal = session.scalars(statement).one_or_none()
            session.close()
        return proposal

    def get_proposal_by_guid(self, guid: String):
        with Session(engine) as session:
            statement = select(Notification).filter_by(id=guid)
            proposal = session.scalars(statement).one_or_none()
            session.close()
        return proposal


class NotificationManager:

    def save_notification(self, notification: Notification) -> bool:
        with Session(engine) as session:
            try:
                session.add(notification)
                session.commit()
            except Exception as e:
                print(e)
                return False
        return True

    def get_notification_by_guid(self, guid: String) -> Notification:
        with Session(engine) as session:
            statement = select(Notification).filter_by(guid=guid)
            notification = session.scalars(statement).one_or_none()
            session.close()
        return notification


users_manager = UsersManager()
proposals_manager = ProposalsManager()
notification_manager = NotificationManager()

if not inspect(engine).has_table("users"):
    Base().metadata.create_all(engine)
