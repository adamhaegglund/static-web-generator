# My Terminal Setup in 2026

[< Back Home](/)

![A stylized terminal window](/images/terminal.svg)

> "The command line is the most powerful tool you're not using enough."

I spend most of my day in a terminal, so I've spent an unreasonable amount of time tweaking it. Here's where it's landed, at least until next week.

## The Essentials

### Shell

I use **zsh** with a minimal prompt. No twelve-segment powerline with the weather and my stock portfolio. Just the directory, the git branch, and whether the last command failed.

### Tools I Can't Live Without

- **fzf**: Fuzzy-find anything. Files, history, git branches. It changes how you navigate.
- **ripgrep**: Search code absurdly fast. I don't remember the last time I typed `grep -r`.
- **tmux**: Sessions that survive closing the window. Splits for days.
- **git**: Obviously. But with a _lot_ of aliases.

## Favorite Aliases

```
alias gs="git status"
alias gco="git checkout"
alias ll="ls -lah"
alias ..="cd .."
alias serve="python3 -m http.server 8888"
```

## Tips If You're Starting Out

1. **Learn the history shortcuts**: `Ctrl+R` alone will save you hours.
2. **Keep your dotfiles in git**: Future you, on a new laptop, will be grateful.
3. **Add things slowly**: Only adopt a tool when you feel the pain it solves.
4. **Read the man pages**: Seriously. They're better than you think.

## Wrapping Up

The best setup is the one you actually understand. Steal ideas freely, but make it yours.
