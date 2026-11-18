# Lessons from Shipping Side Projects

[< Back Home](/)

![A rocket launching from a laptop](/images/launch.svg)

> "Done is better than perfect."

I have a graveyard of unfinished side projects. Half-built apps, abandoned repos, domains I'm still paying for. But a few of them actually shipped, and those taught me more than anything else.

_Here's what I wish I'd known earlier._

## Start Smaller Than You Think

Every project starts as a grand vision. The ones that ship are the ones that got cut down to something I could finish in a weekend:

1. **Pick one feature**: The one thing that makes the project worth existing.
2. **Build only that**: Accounts, settings and dark mode can wait.
3. **Ship it**: Put it somewhere people can see it, even if it's rough.

## Choose Boring Technology

### Novelty Is Expensive

Learning a new framework is fun, but it's a separate project. If the goal is to ship, use the tools you already know:

- **Fewer surprises**: You already know where the sharp edges are.
- **Faster debugging**: You recognize the error messages.
- **More momentum**: Progress you can see keeps you going.

## Make It Easy to Deploy

If deploying takes more than one command, you won't do it often. Automate it early:

```
#!/bin/sh
python3 src/main.py "/my-site/"
git add docs
git commit -m "publish"
git push
```

## Finish Things

The hardest part isn't starting. It's the last 10%: the README, the bug you've been ignoring, the deploy. Push through it. A finished small thing beats an unfinished big thing every time.

Now go ship something.
