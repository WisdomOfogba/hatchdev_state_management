import sys

def remove_react_import(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Just remove the exact line if it exists
    content = content.replace("import React from 'react'\n", "")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

remove_react_import('src/components/Navbar.tsx')
remove_react_import('src/components/UserPage.tsx')
remove_react_import('src/components/UserProfile.tsx')
print("Removed unused React imports!")
