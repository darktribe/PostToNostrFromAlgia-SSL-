Linuxサーバー上でalgiaを使ってNostrにポストするWebhookを作るツールのSSL版です。 Pythonを使っています。

Linuxサーバー上にNostrにポストを投稿するためのSSLのWebhookを作ります。

前提としてalgia (https://github.com/mattn/algia)が動作している事が必要です。 Linuxサーバー上で動いているalgiaを起動させる仕組みになっています。 リポジトリのconfig.jsonはこのプロジェクト用ではなく、algiaのおすすめのコンフィグです。PrivateKeyを書き換えて使ってください。

また前提としてDockerのnginx-proxyを使ってSSL対応している事を前提にしています。
https://github.com/shipwebdotjp/nginx-proxy.git
からDockerでコンテナを作っている場合にのみ動作します。

PostToNostr-ssl.pyを実行すると、「https:[global address of your server machine]:5000/webhook」で起動するWebhookになります。

Webhookに対してPostアクションで { “id-key” : ”test-key”,”text” : “POSTしたい文字列" } というJSONを "Content-Type: application/json" とContent-Typeを指定してHTTPでPOSTすればNostrに投稿されます。

実際に使う際はPostToNostr.pyの「/webhook」を好きなアクセスURLに、ポートを変える際は「port:5000」を好きなポートに、アクセスキーを変えるには「"test-key”」を変えてください。

SSLで起動するため、起動にはroot権限が必要です。
「sudo su」コマンドでroot権限に移行し、Algiaのコンフィグファイルを「cp [YourLocalHost]/.config/algia/config.json /root/.config/algia/config.json」でルートにコピーをしておいて下さい。

ファイルには変数として書き換えなければならない部分があります。
[YourLocalHost]はrootから見たたあなたのフォルダ名に書き換えて下さい（例：/home/yourname）。
[YourDomainName]はあなたのドメイン名に書き換えてください（例：nostr.examle.com）。


起動方法としてはsudo suしてからforeverを使って起動する事を想定しています。具体的には”forever start -c python3 PostToNostr.py”で起動して下さい。起動している間Webhookとして動きます。
起動した後はsuからexitしてもforeverで動き続けます。
