# ChatGPT Plugin for generating gift ideas
Backend for ChatGPT plugin. Middleware is [LangDock](https://langdock.com)
## Local development
```shell
cd src
docker build -t gptpluginimage . 
docker run -e "OPENAI_API_KEY=FILLME" -e "GOOGLE_CSE_ID=FILLME" -e "GOOGLE_API_KEY=FILLME" --rm -p 80:80 -it gptpluginimage
```

## Deploy
```shell
export AWS_ACCOUNT=FILLME
cdk deploy --all
```


<img width="677" alt="Screenshot 2023-05-22 at 5 16 05 PM" src="https://github.com/anatolyburtsev/GiftSuggesterChatGPTPlugin/assets/905276/8b9d8570-1a7a-4d9b-9ff8-de6a7416e493">
<img width="674" alt="Screenshot 2023-05-22 at 5 16 16 PM" src="https://github.com/anatolyburtsev/GiftSuggesterChatGPTPlugin/assets/905276/fc695573-b597-4a71-9671-306afa4395cb">
