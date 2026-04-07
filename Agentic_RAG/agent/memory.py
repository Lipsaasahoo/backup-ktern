chat_history = []


def add_to_memory(user, bot):
    chat_history.append({"user": user, "bot": bot})


def get_memory():
    history_text = ""
    for item in chat_history[-5:]:
        history_text += f"User: {item['user']}\nBot: {item['bot']}\n"
    return history_text