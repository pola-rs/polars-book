from collections import OrderedDict
import os
from typing import List, Optional, Union
import yaml
import logging


# Supported Languages and there metadata
LANGUAGES = OrderedDict(
    python={
        "extension": ".py",
        "display_name": "Python",
        "icon_name": "python",
        "code_name": "python",
    },
    rust={
        "extension": ".rs",
        "display_name": "Rust",
        "icon_name": "rust",
        "code_name": "rust",
    },
    node={
        "extension": ".js",
        "display_name": "NodeJS",
        "icon_name": "node-js",
        "code_name": "javascript",
    },
)

# Load all links to reference docs
with open("API_REFERENCE_LINKS.yaml", "r") as f:
    API_REFERENCE_LINKS = yaml.load(f, Loader=yaml.CLoader)


def create_api_function_link(language: str, function_key: str) -> Optional[str]:
    """Create an API link in markdown with an icon of the YAML file

    Args:
        language (str): programming language
        function_key (str): Key to the specific function

    Returns:
        str: If the function is found than the link else None
    """
    info = API_REFERENCE_LINKS.get(language, {}).get(function_key)

    if info is None:
        logging.warning(f"Could not find {function_key} for language {language}")
        return None
    else:
        # Either be a direct link
        if type(info) == str:
            return f"[:material-api:  `{function_key}`]({info})"
        else:
            function_name = info["name"]
            link = info["link"]
            return f"[:material-api:  `{function_name}`]({link})"


def code_tab(
    base_path: str,
    section: str,
    language_info: Union[str, dict],
    api_functions: List[str],
) -> str:
    """
    Return a code tab in Markdown based on:
    - Filepath of the code
    - Optional Section within the path
    - Additional links to API functions dependent on the language (lookup of e.g. reference_links/python.yaml)
    """
    language = language_info["code_name"]

    # Create API Links if they are defined in the YAML
    api_functions_template = " ·".join(
        link for f in api_functions if (link := create_api_function_link(language, f))
    )

    # Create path for Snippets extension
    snippets_file_name = f"{base_path}:{section}" if section else f"{base_path}"

    # See Content Tabs for details https://squidfunk.github.io/mkdocs-material/reference/content-tabs/
    return f"""=== \":fontawesome-brands-{language_info['icon_name']}: {language_info['display_name']}\"
    {api_functions_template}
    ```{language}   
    --8<-- \"{snippets_file_name}\"
    ```
    """


def define_env(env):
    @env.macro
    def code_block(path, section=None, api_functions=None):
        """
        Loop over all languages:
        - Check if the file defined by path parameter exist
        - If yes, then create a content tab with code for it
        """
        result = []

        for language, info in LANGUAGES.items():
            base_path = f"{language}/{path}{info['extension']}"
            full_path = "docs/src/" + base_path
            if os.path.exists(full_path):
                result.append(code_tab(base_path, section, info, api_functions))

        return "\n".join(result)
