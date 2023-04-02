import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are my girl bestfriend"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "JENNY")

demo.launch(share=True)