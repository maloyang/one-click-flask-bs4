# one-click to Heroku

### 這是一個demo，示範如何一鍵佈署一個Flask+bootstrap的template網頁到Heroku去

- 可以按以下的按鈕進行自動佈署本App
- one-click button to auto deploy this demo

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


- 這一個App有幾個元素，是一個App最基本的三個檔案：
    - app.py: 主程式
    - Procfile: App類型，如何啟動
    - requirements.txt: 需要的套件
    
- 另外，在你的repo上根目錄下放一個 app.json 檔，格式如下，這邊我只放入了三個必要的項目(Heroku建議要有這三項)：
<code><pre>
{
    "name": "flask hello",
    "description": "a basic flask @ heroku demo",
    "repository": "https://github.com/maloyang/one-click-flask-hello"
}
</pre></code>

- 這邊要注意到你的「description有字數的限制」! 好像是40bytes，之前我一直失敗就是沒注意到不可寫太多說明…
- 下面的是Heroku說明網頁中的範例，也可以參考一下

<code><pre>
{
  "name": "Node.js Sample",
  "description": "A barebones Node.js app using Express 4",
  "repository": "https://github.com/heroku/node-js-sample",
  "logo": "https://node-js-sample.herokuapp.com/node.png",
  "keywords": ["node", "express", "static"]
}
</pre></code>

- 只要完成了以上的事，就可以做一個快速佈署按鈕分享你的專案給大家使用!!
