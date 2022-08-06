# omtool
**omtool** is a Linux operation and manage customized software. Its purpose is to support some environment with cluttered commands or the action needed multiple steps. For the most important, with **omtool** we can customize the commands in the system. THAT'S FUN!

# Quickly start

## Install

## Customize our first command

Now there is a requirement that **How many files and directories are in current path?**. Utilizing the "shell command" is a good choice.

Count the number of files:

```shell
ls -l |grep "^-"|wc -l
```

Count the number of directories:

```shell
ls -l |grep "^d"|wc -l
```

OK, now the requirement is met. We took two steps in total. But is there a better way to do this thing? I mean, if this requirement takes dozens of steps and hundreds of steps.

**omtool** can do this thing. It can define these operations with a single command.



# Development plan

- Develop some common output format to render the result of  command;
- Support for using configuration files to define commands (CDC,Configuration Define Command);