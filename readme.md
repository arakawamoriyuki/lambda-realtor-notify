# lambda-realtor-notify

lambdaで不動産新着物件を通知する

## ローカル実行

パッケージインストール

```
$ docker run --rm \
  -v "$PWD":/var/task \
  lambci/lambda:build-python3.7 \
  pip install -r requirements.txt -t src
```

実行

```
$ docker run --rm \
  -v "$PWD/src":/var/task:ro,delegated \
  -e REALTOR_SEARCH_ENDPOINT=https://xxxxx.xxxxx/async/getcount \
  -e IFTTT_EVENT=realtor-search \
  -e IFTTT_KEY=xxxxxxxxxxxxxxxxxxxx \
  -e AWS_REGION=ap-northeast-1 \
  lambci/lambda:python3.7 \
  lambda_function.lambda_handler
```

## deploy

deploy_package.zipの作成

```
$ rm -f deploy_package.zip \
  && cd src \
  && zip -r deploy_package.zip . \
  && cd .. \
  && mv src/deploy_package.zip .
```

update lambda

```
$ aws lambda update-function-code \
    --profile {profile} \
    --region ap-northeast-1 \
    --function-name {function name} \
    --zip-file fileb://$PWD/deploy_package.zip \
    --publish
```
