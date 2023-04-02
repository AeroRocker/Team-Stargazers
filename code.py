import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a Game designer"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "MAXZ")

demo.launch(share=True)