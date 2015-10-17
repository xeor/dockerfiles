This container takes away the pain of compiling one of those "one-off" plugins for an Atlassian product.
When all you need is a tiny change, like an authentication plugin (the example).

* `/data` is the workdir for this container
  * Where your pom-file should live
* `/opt/atlassian-plugin-sdk/bin/atlas-run` is the default CMD, and will create a .jar file for you.


# Examples

## Create a jira-plugin template
* docker run -i -t -v $PWD/jira-plugin:/data xeor/atlassian-dev /opt/atlassian-plugin-sdk/bin/atlas-create-jira-plugin

## Use the RemoteUserJira plugin
* IMPORTANT! Only use this if you know what you are doing, or people will be able to login with whoever they want.
* It logs you in if the http header `user` is sat to a user that is valid inside Jira.
* You dont haveto use Javas `AJP` protocoll, this works over `HTTP`.
  * Which means, you can use other web-servers in front than `Apache httpd`.
  * You wont need to recompile nginx with AJP support
    * Even tho that wont work either, since it still doesnt support those "magic" apache>tomcat headers...
* You are in charge to make sure the browser cant set the `user` variable. Example with the use of `wwwhisper` in front.
* You need to replace the `authenticator` stanza in `seraph-config.xml` to something like `<authenticator class="datt.jira.RemoteUserJira"/>`.
* The compiled `RemoteUserJira-1.0.jar` needs to be located somewhere like `/opt/atlassian/jira/atlassian-jira/WEB-INF/lib/RemoteUserJira-1.0.jar`

To compile it, clone this repo, go into the `RemoteUserJira` folder, and run `docker run -i -t -v $PWD:/data xeor/atlassian-dev`. When it sais it have started jira, kill it, and your .jar will be in the `./target` directory.

PS: There is probably a better way to compile atlassian plugins using some of the `atlas-` commands. Please share, I'm nor a java-developer, and just wanted a quick way of doing this, and a quick plugin (which I coulnt find). Lots of the code is from https://github.com/glorang/RemoteUserConfluenceAuth / https://wiki.warren.bz/pages/viewpage.action?pageId=9338886

## Use the RemoteUserConfluence plugin
* See the notes about the Jira plugin. Its basicly the same :)
* I got an error `java.lang.ClassCastException: com.atlassian.confluence.security.seraph.ConfluenceUserPrincipal cannot be cast to com.atlassian.user.User` suddenly after I had setup confluence using this plugin once. It went away after I got to the home-page. It happened when I pressed "furter configuration" after the setup.
