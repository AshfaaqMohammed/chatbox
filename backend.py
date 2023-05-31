import openai


class Chatbot:

    def __init__(self):
        openai.organization = 'org-id'
        openai.api_key = "api_key" #use api key generated in your accound

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=2000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("name the biggest planet in our solar system")
    print(response)

