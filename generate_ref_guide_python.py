"""Generate the `Markdown` source for `mdBook`.

This makes use of [`astdocs`](https://github.com/carnarez/astdocs), a very opinionated
docstring fetcher.

This is one nasty piece of script.
"""

import os
import re

import astdocs

# BRACE FOR THE PATH JUGGLING MATE
# all unix paths, ftw
OUT = "reference_guide_python/src".rstrip("/")  # where do we want the markdown
PKG = "polars".rstrip("/")  # package (folder) to process
SRC = ".venv/lib/python3.8/site-packages".rstrip("/")  # where it that package

# make them absolute
cwd = os.getcwd()
OUT = f"{cwd}/{OUT}"
SRC = f"{cwd}/{SRC}"


def mdbook_includes(md: str) -> str:
    """Convert the `reStructuredText` to `mdBook` syntax.

    `.. include:: ...` becomes `{{#include ...}}`.
    """
    # two passes to make it cleaner, if not clearer
    # would break if those markers are in the code, but...
    return re.sub(
        r"\n\.\. include:: (.*)", r"\n{{#include %%%SRCPKG%%%\1}}", md
    ).replace("include %%%SRCPKG%%%", f"include {SRC}/{PKG}/")


def mdbook_raw_includes(md: str) -> str:
    """Convert the `%%%SOURCE` markers to home-tweaked `mdBook` syntax.

    The following lines in the source `Markdown`:

    ```text
    %%%SOURCE ...
    ```

    become:

    ````html
    <raw>
    <details>
      <summary style="text-align:right">source</summary>
    </raw>
    ```python
    {{#include ...}}
    ```
    <raw>
    </details>
    </raw>
    ````

    to be understood by a custom `mdBook` executable (accepting raw `HTML` code in
    between the `<raw></raw>` tags.
    """
    # several passes to make it cleaner, if not clearer
    # would break if those markers are in the code, but...
    return (
        re.sub(
            r"\n%%%SOURCE (.*)",
            r"\n%%%PREFIX%%%{{#include %%%SRC%%%\1}}\n%%%SUFFIX%%%",
            md,
        )
        .replace(
            "%%%PREFIX%%%",
            (
                "<raw>\n"
                "<details>\n"
                '  <summary style="text-align:right">source</summary>\n'
                "</raw>\n"
                "```python\n"
            ),
        )
        .replace("include %%%SRC%%%", f"include {SRC}/")
        .replace(
            "%%%SUFFIX%%%",
            ("```\n" "<raw>\n" "</details>\n" "</raw>\n"),
        )
    )


def path_cleanup(md: str) -> str:
    """Remove included path mishaps and clumsiness."""
    return md.replace("/./", "/").replace("//", "/")


@astdocs.postrender(mdbook_includes)
@astdocs.postrender(mdbook_raw_includes)
@astdocs.postrender(path_cleanup)
def render():
    """Simple wrapper funtion to allow decorators."""
    return astdocs.render_recursively(f"{SRC}/{PKG}", f"{SRC}/")


if __name__ == "__main__":

    # going to write the summary as we go
    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/SUMMARY.md", "w") as summary:
        summary.write("# Summary\n\n")

        for line in render().split("\n"):

            # fetch the marker indicating the end of an object (by indicating the
            # beginning of the next one)
            if line.startswith("%%%BEGIN"):

                try:
                    output.close()
                except NameError:
                    pass

                # relative path for internal linking
                bookpath = f'{line.split()[2].replace(".", "/")}.md'
                print(bookpath)  # here's some logging"

                # absolute path to write the file
                filepath = f"{OUT}/{bookpath}"

                if "/" in filepath:
                    dirpath, filename = filepath.rsplit("/", 1)

                    # make sure we get access to the folder (create it if necessary)
                    os.makedirs(dirpath, exist_ok=True)

                    # define how many indentation is needed by parsing the absolute path
                    # but removing the part that is not relevant
                    # -3 due to the three / in .../reference_guide/src/
                    indent = "  " * (dirpath.count("/") - (cwd.count("/") + 3))

                else:
                    filename = filepath
                    indent = ""

                summary.write(f'{indent}- [`{filename.split(".")[0]}`]({bookpath})\n')
                output = open(filepath, "w")

            # write to the open stream
            else:
                output.write(f"{line}\n")

        summary.close()
        try:
            output.close()
        except NameError:
            pass
