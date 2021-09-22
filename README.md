# csshi
ClusterSSH (cssh) for [iTerm2](https://iterm2.com/).

# Install
Install the latest iTerm2 however you like.  
Install python3 e.g. with [homebrew](https://brew.sh/):  
```$ brew install python3```  
Install the python iterm2 libs through pip:  
```$ pip3 install iterm2```  
Clone this repo.

# Usage
Enable the Python API in iTerm2 -> Preferences... -> General -> Magic  
Run like:  
```$ ./csshi --help```  
```$ ./csshi host user@host2 otherhost:2222 user2@[2100:1234::1000]:1022```  
```$ cat list-of-hosts | grep prd | xargs ./csshi```

# Contribute
Throw a PR over, raise an issue, sliiiide into my DMs.  
Email in the git log.
