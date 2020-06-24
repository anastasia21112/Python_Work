messages = ['Hey', 'How are you?', 'Miss you']
sent_messages = []

def send_messages(messages):
    while messages:
        message = messages.pop()
        print(message.title())
        sent_messages.append(message)

send_messages(messages[:])
print(messages)
print(sent_messages)
