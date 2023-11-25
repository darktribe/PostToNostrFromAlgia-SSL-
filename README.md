This is an SSL version of a tool to create a webhook that posts to Nostr using algia on a Linux server. It uses Python.

Create an SSL webhook to post to Nostr on a Linux server.

The prerequisite is that you have algia (https://github.com/mattn/algia) running. The system is designed to start algia running on a Linux server. The config.json in the repository is not for this project, but is the recommended config for algia.

It is also assumed that you have SSL support using Docker's nginx-proxy.
https://github.com/shipwebdotjp/nginx-proxy.git
This will only work if you have created a container with Docker from

Running PostToNostr-ssl.py will result in a webhook that starts with "https:[global address of your server machine]:5000/webhook".

In the Post action for the webhook, { "id-key" : "test-key", "text" : "text" : "string to be POSTed JSON { "id-key" : "test-key", "text" : "string to be POSTed" } in the Post action to the webhook, specifying "Content-Type: application/json" and Content-Type in the HTTPS POST action, and the string will be posted to Nostr.

To actually use it, change "/webhook" in PostToNostr.py to your favorite access URL, "port:5000" to your favorite port to change the port, and ""test-key"" to change the access key.

To start the application over SSL, root privileges are required to start it.
Use the "sudo su" command to switch to root privileges and copy the Algia config file to the root with "cp [YourLocalHost]/.config/algia/config.json /root/.config/algia/config.json". Please copy it to the root.

Some parts of the file must be rewritten as variables.
[YourLocalHost] should be replaced with your folder name as seen from root (e.g. /home/yourname).
[YourDomainName] should be your domain name (e.g. nostr.examle.com).


It is assumed that the startup method is to sudo su and then start using "forever". Specifically, start it with "forever start -c python3 PostToNostr.py". It will work as a Webhook while it is running.
After it is started, it will continue to run "forever" even if you exit from "su".
