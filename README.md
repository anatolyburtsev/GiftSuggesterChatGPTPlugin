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