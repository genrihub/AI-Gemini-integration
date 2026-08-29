def AI(msg):
    from google import genai
    from google.genai.errors import APIError

    API =  [
            "API REYS..."
            ]

    for i in range(len(API)):
        try:
            client = genai.Client(api_key=API[i])
            chat = client.chats.create(model='gemini-3.5-flash')
            otvet = chat.send_message(msg)
            return otvet.text
        except APIError:
            connect = False

    return 'Error'
