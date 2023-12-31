# tweet

## Twitter keys and access tokens
To use tweet you'll need your Twitter account keys and access tokens. Complete the file "mykeys.py" with your personnal account informations (don't share them with anyone).

## Launch the program
Launch the program with python by typing `python tweet.py` in the program directory from the Terminal command line.

I personally use a shortcut with the short keyword `tweet` that launches the code from the right directory.

## How does it work ?
As you launch the program, you'll see the following interface in the Terminal command line. Enter some text after "Post:" then hit enter, and a blue message will confirm that you successfully tweeted ! Go check online and you should immediately see your new post.

<p align="center">
  <img src="img/newtweet.png" width=40% height=40%>
</p>

## Use Terminal alias (mac)
Open or create the shell configuration file by typing `open ~/.zprofile` in the user’s home directory.

Add the line: `alias tweet='python /pathtofile/tweet.py'` with the right path to your file.

Now you can type `tweet` in the Terminal command line to launch the program.

## Libraries
This program uses tweepy package.

## License
[MIT License](LICENSE)
