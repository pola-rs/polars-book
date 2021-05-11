import re

# compile regexes
RE_START_FN = re.compile(r"%%%START FUNCTIONDEF.*\n")
RE_END_FN = re.compile(r"%%%END FUNCTIONDEF.*\n*")
RE_START_ANY = re.compile(r"%%%START.*")
RE_END_ANY = re.compile(r"%%%END.*")
RE_MODULE_FFI = re.compile(
    r"%%%BEGIN MODULE polars.ffi.*%%%END MODULE polars.ffi", flags=re.S
)


def encapsulate_funcs(md: str) -> str:
    md = RE_START_FN.sub("<raw><div class='function-wrap'></raw>\n", md)
    md = RE_END_FN.sub("<raw></div></raw>\n", md)

    # remove other start/ends
    md = RE_START_ANY.sub("\n", md)
    md = RE_END_ANY.sub("\n", md)
    return md


def remove_elements(md: str) -> str:
    md = remove("polars.ffi", "MODULE", md)
    md = remove("polars.utils", "MODULE", md)
    md = remove("polars.series.IdentityDict", "CLASSDEF", md)
    md = remove("polars.series.SeriesIter", "CLASSDEF", md)
    md = remove("polars.series.SeriesIter", "CLASSDEF", md)
    md = empty_module("polars.series", md)
    md = remove("polars.lazy.wrap_ldf", "FUNCTIONDEF", md)
    md = remove("polars.lazy.wrap_expr", "FUNCTIONDEF", md)
    md = remove("polars.lazy.expr_to_lit_or_expr", "FUNCTIONDEF", md)
    return md


def empty_module(name: str, md: str) -> str:
    """
    Empty the contents of the module, but keep the module file (for the SUMMARY.md)

    Parameters
    ----------
    name
        full path name of module
    md
        markdown content
    """
    return re.sub(
        rf"%%%BEGIN MODULE {name}.*%%%BEGIN",
        "%%%BEGIN MODULE polars.series\n%%%BEGIN",
        md,
        flags=re.S,
    )


def remove(name: str, type_: str, md: str) -> str:
    """
    Remove an element from the str blob.

    Parameters
    ----------
    name
        name: e.g. polars.ffi
    type_
        Any of
            - CLASSDEF
            - MODULE
            - FUNCTIONDEF

    md
        markdown source
    """

    if type_ == "FUNCTIONDEF":
        keyword = name.split(".")[-1]
        md = re.sub(rf"\* \[`{keyword}\(\)`\].*\)\n*", "", md)
        return re.sub(
            rf"%%%START {type_} {name}.*%%%END {type_} {name}", "", md, flags=re.S
        )

    return re.sub(
        rf"%%%BEGIN {type_} {name}.*%%%END {type_} {name}",
        "",
        md,
        flags=re.S,
    )
