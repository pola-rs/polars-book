/* Implement tabbed code blocks for mdBook. */
/* Credit to Rob Moss who provided this code
 * to another mdbook project.  The original
 * commit is available here https://github.com/robmoss/git-is-my-lab-book/pull/13
 */

(function() {
    "use strict";
    
    // The CSS selector used to identify groups of tabbed code blocks.
    const blocks_selector = "div.tabbed-blocks";
    
    // The CSS class used to identify the active tab.
    const class_active = "active";
    
    // NOTE: the order in which we define the names is important, because we
    // iterate over the names in the *insertion order*.
    const tab_names = new Map();
    tab_names.set("language-python", "Python");
    tab_names.set("language-py", "Python");
    tab_names.set("language-R", "R");
    tab_names.set("language-cpp", "C++");
    tab_names.set("language-sh", "Shell");
    tab_names.set("language-shell", "Shell");
    tab_names.set("language-shell-python", "Python");
    tab_names.set("language-shell-rust", "Rust");
    tab_names.set("language-md", "Markdown");
    tab_names.set("language-text", "Text");
    tab_names.set("language-diff", "Diff");
    tab_names.set("language-rust", "Rust");
    tab_names.set("language-js", "JavaScript");
    
    // The tab name to use when none of the above names apply.
    const default_tab_name = "Unknown";
    
    function addTabsToGroup(group) {
        // Create the container for the tab buttons.
        const tab_bar = document.createElement("ul");
        tab_bar.className = "tab-bar";
        group.prepend(tab_bar);
    
        // Add a tab for each code block, and hide all but the first block.
        const pre_elements = group.querySelectorAll("pre");
        pre_elements.forEach((pre_elt, ix) => {
            const tab_elt = addTabForCodeBlock(tab_bar, pre_elements, pre_elt);
            if (ix > 0) {
                pre_elt.style.display = "none";
            } else {
                tab_elt.classList.add(class_active);
            }
        });
    }
    
    function addTabForCodeBlock(tab_bar, pre_elts, pre_elt) {
        // Find the code element, from which we can identify the language.
        const code_elt = pre_elt.querySelector("code");
        // Identify the code block language.
        const tab_text = document.createTextNode(getTabTextForCode(code_elt));
    
        // Create the button for this tab.
        const tab_elt = document.createElement("li");
        tab_elt.appendChild(tab_text);
        tab_bar.appendChild(tab_elt);
    
        // Add an event handler for switching between tabs.
        addTabEventHandler(tab_elt, tab_bar, pre_elts, pre_elt);
    
        return tab_elt;
    }
    
    function getTabTextForCode(code_elt) {
        // Identify the language based on the code element's class.
        for (const [class_name, tab_text] of tab_names) {
            if (code_elt.classList.contains(class_name)) {
                return tab_text;
            }
        }
        return default_tab_name;
    }
    
    function addTabEventHandler(tab_elt, tab_bar, pre_elts, pre_elt) {
        tab_elt.addEventListener("click", () => {
            // Hide all code blocks.
            pre_elts.forEach((pre_elt) => {
                pre_elt.style.display = "none";
            });
            // Show this code block.
            pre_elt.style.display = "block";
    
            // Mark this button as the active tab.
            tab_bar.querySelectorAll("li").forEach((elt) => {
                elt.classList.remove(class_active);
            });
            tab_elt.classList.add(class_active);
        });
    }
    
    // Create a tab bar for each group of code blocks.
    window.addEventListener("DOMContentLoaded", (event) => {
        const tab_groups = document.querySelectorAll(blocks_selector);
        tab_groups.forEach(addTabsToGroup);
    });
    
    })();
    