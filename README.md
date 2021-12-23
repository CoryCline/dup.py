# dup.py
An application intended to simplify printing to terminal and outputting to a file at the same time for tools that do not support this

## How to install
To install this application, perform the following:
```
$ chmod +x ./dup.py
$ sudo mv ./dup.py /usr/local/bin/dup.py
```

## Problem that gets solved
```
$ ./HackerTool > OutputFile # A tool that doesn't have native file output
$ # This sucks because now you see nothing while you wait
```

## How to use it
Pipe the output of a command into dup.py with a filename as parameter one.
```
$ ./HackerTool | dup.py OutputFile
$ 1337 output
$ cat ./OutputFile
$ 1336 output
```

## Ideas for growth
- Handle STDIN
- Handle STDERR
