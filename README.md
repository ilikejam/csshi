# csshi
A ClusterSSH utility (like [cssh](https://github.com/duncs/clusterssh)) for [iTerm2](https://iterm2.com/).

The command opens an iTerm2 Window and connects over ssh to each specified host in a [split pane](https://iterm2.com/features.html) session, with any text typed or pasted replicated to all panes through iTerm2's 'broadcast' feature. iTerm2's split pane controls are available as normal, so broadcast input can be toggled per-pane, sessions can be restarted, etc.

# Install
Install the latest iTerm2 however you like.  
Install python3 e.g. with [homebrew](https://brew.sh/):  
```$ brew install python3```  
Install the python iterm2 libs through pip:  
```$ pip3 install iterm2```  
Clone this repo and optionally copy csshi to your PATH.

# Usage
Enable the iTerm2 Python API at:  
`iTerm2` -> `Preferences...` -> `General` -> `Magic`  

```text
usage: cssh [-h] [-l USERNAME] [-p PORT] [-J JUMPHOST] [-o OPTIONS]
            [-C COLUMNS]
            destination [destination ...]

Run multiple ssh connections concurrently in an iTerm2 terminal.

positional arguments:
  destination           [user@]host[:port] ssh server specification. Use square
                        brackets around IPv6 IP adresses.

optional arguments:
  -h, --help            show this help message and exit
  -l USERNAME, --username USERNAME
                        Login username, overridden per-host by specifying
                        'user@host'
  -p PORT, --port PORT  ssh server port, overridden per-host by specifying
                        'host:port
  -J JUMPHOST, --jump JUMPHOST
                        ProxyJump host specification, like
                        [user@]jumphost[:port]
  -o OPTIONS, --options OPTIONS
                        Raw ssh options string, e.g. '-i ~/.ssh/id_ansible'
  -C COLUMNS, --columns COLUMNS
                        Maximum number of columns.
```

# Tips
Some preferences to optimise for shell density if you find yourself opening a lot of terminals in one csshi session:
1) Use a small font, like the original [misc-fixed 6x13](https://monkey.org/~marius/beautiful-fixed-width-fonts-for-osx.html), and disable antialiasing:  
`iTerm2` -> `Preferences...` -> `Profiles` -> `Text` -> `Anti-aliased`
1) Disable pane menubars:  
`iTerm2` -> `Preferences...` -> `Appearance` -> `Panes` -> `Show per-pane title bar with split panes`  
You can still access the menu for each pane with Ctrl-click instead of the menubar burger icon
1) Decrease the 'Side' and 'Top & bottom' margins:  
`iTerm2` -> `Preferences...` -> `Appearance` -> `Panes`

# Contribute
Throw a PR over, raise an issue, send me an email.
