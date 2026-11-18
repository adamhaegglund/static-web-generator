# Building a Static Site Generator from Scratch

[< Back Home](/)

![Markdown flowing into HTML](/images/generator.svg)

> "What I cannot create, I do not understand."
>
> -- Richard Feynman

There are dozens of excellent static site generators out there. So naturally, I built my own. Not because the world needed another one, but because I wanted to understand what actually happens between writing a `.md` file and seeing a page in the browser.

_Spoiler: it's mostly string manipulation._

## The Big Picture

The whole thing is a pipeline. Markdown goes in one end, HTML comes out the other:

1. **Split into blocks**: Break the document on blank lines into paragraphs, headings, lists, quotes and code.
2. **Parse inline text**: Find the **bold**, _italic_, `code`, links and images inside each block.
3. **Build a tree**: Turn everything into HTML nodes with parents and children.
4. **Render**: Walk the tree and spit out a string of HTML.
5. **Template**: Drop the result into a page layout and write it to disk.

## The Tricky Parts

### Inline Parsing

Delimiters are deceptively simple until they aren't:

- **Nesting**: What happens with bold inside a link inside a list item?
- **Unclosed delimiters**: A stray underscore shouldn't explode the whole page.
- **Images vs. links**: They look almost identical, so order of operations matters.

### Recursion Everywhere

Copying the static directory, generating pages for every nested folder, rendering child nodes. Once recursion clicked, half the project wrote itself.

```
def copy_files(src, dest):
    for name in os.listdir(src):
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            copy_files(src_path, dest_path)
```

## Was It Worth It?

Absolutely. I'll probably still reach for an off-the-shelf tool for big projects, but now I know what's going on under the hood. And there's something deeply satisfying about publishing a blog with software you wrote yourself.
