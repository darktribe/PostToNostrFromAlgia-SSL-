This is an SSL version of a tool to create a webhook that posts to Nostr using algia on a Linux server. It uses Python.　　
I have uploaded the file "PostToNostr-ssl.py" in error, but please use "PostToNostr-SSL.py".　　

Create an SSL webhook on your Linux server to post to Nostr.　　

The prerequisite is that [algia](https://github.com/mattn/algia) is running. The system is designed to start algia running on a Linux server. The config.json file in the repository is not for this project, but is the recommended config for algia.　　

Also, it is assumed that you are using Docker's nginx-proxy to support SSL.　　
[https://github.com/shipwebdotjp/nginx-proxy.git](https://github.com/shipwebdotjp/nginx-proxy.git)
This will only work if you have created a container in Docker from　　

Running PostToNostr-SSL.py will result in a webhook that starts with "https:[global address of your server machine]:5000/webhook".　　

In the Post action for the webhook, { "id-key" : "test-key", "text" : "string to be POSTed". JSON { "id-key" : "test-key", "text" : "string to be POSTed" } in the Post action to the webhook with the Content-Type "Content-Type: application/json" and HTTPS.　　

To actually use it, change "/webhook" in PostToNostr.py to your favorite access URL, "port:5000" to your favorite port to change the port, and ""test-key"" to change the access key.　　

To start with SSL, root privileges are required to start.　　
Use the "sudo su" command to switch to root privileges and copy the Algia config file to the root with "cp /home/[yourname]/.config/algia/config.json /root/.config/algia/config.json". The file must be rewritten as a variable.　　

Some parts of the file must be rewritten as variables.　　
[Yourname] should be replaced with your user name as seen by root.　　
[YourDomainName] should be your domain name (e.g. nostr.examle.com).　　

It is assumed that you will use "sudo su" and then use "forever" to start up the server. Specifically, start it with "forever start -c python3 PostToNostr-SSL.py". It will work as a webhook while it is running.　　
After it is started, it will continue to work as "forever" even if you exit from su.
