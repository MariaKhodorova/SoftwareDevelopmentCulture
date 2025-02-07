#!/bin/bash

# Define project name
PROJECT_NAME="fancy-convert"

# Define directories
DIRECTORIES=(
    "$PROJECT_NAME/$PROJECT_NAME/fancy_convert"
    "$PROJECT_NAME/$PROJECT_NAME/tests"
    "$PROJECT_NAME/$PROJECT_NAME/use_cases"
    "$PROJECT_NAME/$PROJECT_NAME-api/app"
    "$PROJECT_NAME/$PROJECT_NAME-api/tests"
    "$PROJECT_NAME/scripts"
)

# Define files
FILES=(
    "$PROJECT_NAME/$PROJECT_NAME/fancy_convert/__init__.py"
    "$PROJECT_NAME/$PROJECT_NAME/fancy_convert/converters.py"
    "$PROJECT_NAME/$PROJECT_NAME/fancy_convert/utils.py"
    "$PROJECT_NAME/$PROJECT_NAME/fancy_convert/config.py"
    "$PROJECT_NAME/$PROJECT_NAME/tests/__init__.py"
    "$PROJECT_NAME/$PROJECT_NAME/pyproject.toml"
    "$PROJECT_NAME/$PROJECT_NAME/README.md"
    "$PROJECT_NAME/$PROJECT_NAME/LICENSE"

    "$PROJECT_NAME/$PROJECT_NAME-api/app/__init__.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/app/main.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/app/routes.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/app/dependencies.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/app/cli.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/tests/__init__.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/.env.example"
    "$PROJECT_NAME/$PROJECT_NAME-api/pyproject.toml"
    "$PROJECT_NAME/$PROJECT_NAME-api/README.md"

    "$PROJECT_NAME/scripts/install.sh"
    "$PROJECT_NAME/scripts/run_local.sh"
    "$PROJECT_NAME/scripts/build_docker.sh"
    "$PROJECT_NAME/scripts/run_docker.sh"

    "$PROJECT_NAME/docker-compose.yml"
    "$PROJECT_NAME/.gitignore"
    "$PROJECT_NAME/LICENSE"
    "$PROJECT_NAME/README.md"
)

# Create directories
echo "Creating project directories..."
for dir in "${DIRECTORIES[@]}"; do
    mkdir -p "$dir"
done

# Create files
echo "Creating project files..."
for file in "${FILES[@]}"; do
    touch "$file"
done

# Add execute permissions to scripts
chmod +x "$PROJECT_NAME/scripts/"*.sh

echo "Project structure created successfully!"
