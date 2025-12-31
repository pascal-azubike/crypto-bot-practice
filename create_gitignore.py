# Create proper .gitignore file
with open('.gitignore', 'w', encoding='utf-8') as f:
    f.write("""# Environment variables
.env
.env.local
.env.*.local

# Virtual Environment
venv/
env/
ENV/
.venv

# Python cache
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
desktop.ini

# Logs
*.log
logs/
data/

# Temporary files
*.tmp
*.bak
.cache/

# Distribution / packaging
build/
dist/
*.egg-info/
""")

print("✅ .gitignore created successfully!")
