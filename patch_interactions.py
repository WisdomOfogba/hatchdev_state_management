import sys

def patch_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add cursor-pointer and active:scale-95 to buttons
    # In Login.tsx: className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2.5 px-4 rounded-lg transition-colors duration-200 shadow-sm mt-2"
    # In Sidebar.tsx: className="w-full bg-slate-900 hover:bg-slate-800 text-white font-medium py-2.5 px-4 rounded-lg transition-colors duration-200 shadow-sm"

    content = content.replace(
        'transition-colors duration-200',
        'transition-all duration-200 cursor-pointer active:scale-[0.98]'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

patch_file('src/components/Login.tsx')
patch_file('src/components/Sidebar.tsx')
print("Patched interactions!")
