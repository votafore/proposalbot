import utils
import main

from arch.SomeFile import notification_manager, Notification, users_manager

# todo: implement for notifications which get error while saving in database
queue = None


async def show_notification(data: dict) -> {bool, str}:

    valid, error = validate_show_notification(data)

    if not valid:
        return False, "not valid data"

    guid = data["id"]
    receiver = utils.get_phone_number(data["phone"])
    text = data["text"]

    user = users_manager.find_user_by_phone(receiver)
    if user is None:
        return False, "user not found"

    notification = Notification(
        guid=guid,
        receiver=receiver,
        user_id=user.id,
        text=text,
        mark=False
    )

    if notification_manager.save_notification(notification):
        msg = await main.bot.send_message(user.chat_id, text)
        notification.message_id = msg.message_id
        notification_manager.save_notification(notification)
    else:
         return False, "just error"

    return True, ""  # "notification going to be showed"


async def delete_notification(data: dict) -> {bool, str}:
    valid, error = validata_delete_notification(data)
    if not valid:
        return False, "data are not valid"
    notification = notification_manager.get_notification_by_guid(data["id"])
    if notification is None:
        return False, "notification not found"
    user = users_manager.find_user_by_id(notification.user_id)
    if user is None:
        return False
    try:
        await main.bot.delete_message(chat_id=user.chat_id, message_id=notification.message_id)
        notification.mark = True
        notification_manager.save_notification(notification)
    except Exception as e:
        print(e)
        return False, "just error"

    return True, ""  # "notification going to be deleted"


async def get_list() -> str:
    return "notifications by user (phone)"


def validate_show_notification(data: dict) -> {bool, str}:
    result = True
    error = [""]
    guid = data["id"]
    if guid is None or guid == "":
        result = False
        error.append(f"no ''id'' field")

    receiver = data["phone"]
    if receiver is None or receiver == "":
        result = False
        error.append(f", no ''phone'' field")

    text = data["text"]
    if text is None or text == "":
        result = False
        error.append(f", no ''text'' field")

    return result, ', '.join(map(str, error))


def validata_delete_notification(data: dict) -> {bool, str}:
    result = True
    error = ""
    guid = data["id"]
    if guid is None or guid == "":
        result = False
        error = "no ''id'' field"
    return result, error
