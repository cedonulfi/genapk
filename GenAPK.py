import os
import subprocess


def run_command(command):
    """
    Run a shell command and print the output in real-time.
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in process.stdout:
        print(line.decode(), end="")
    process.wait()


def create_project_structure(project_name, website_url, icon_path=None):
    """
    Create project folder, main.py, and optional icon file.
    """
    # Step 1: Create Project Folder
    if not os.path.exists(project_name):
        os.makedirs(project_name)
        print(f"Created project directory: {project_name}")

    # Step 2: Create main.py
    main_py_path = os.path.join(project_name, "main.py")
    with open(main_py_path, "w") as f:
        f.write(f"""
from kivy.app import App
from kivy.uix.webview import WebView

class WebApp(App):
    def build(self):
        webview = WebView(url="{website_url}")
        return webview

if __name__ == "__main__":
    WebApp().run()
        """)
    print("Created main.py with WebView code.")

    # Step 3: Copy icon if provided
    if icon_path:
        destination_icon = os.path.join(project_name, "icon.png")
        if os.path.exists(icon_path):
            with open(icon_path, "rb") as src, open(destination_icon, "wb") as dest:
                dest.write(src.read())
            print("Copied icon to project directory.")
        else:
            print("Icon file not found. Skipping...")


def initialize_buildozer(project_name):
    """
    Initialize Buildozer in the project directory.
    """
    os.chdir(project_name)
    if not os.path.exists("buildozer.spec"):
        print("Initializing Buildozer...")
        run_command("buildozer init")
    else:
        print("Buildozer already initialized.")


def update_buildozer_spec(project_name, title, package_name, package_domain):
    """
    Update buildozer.spec with custom configurations.
    """
    spec_file = os.path.join(project_name, "buildozer.spec")
    if os.path.exists(spec_file):
        with open(spec_file, "r") as file:
            lines = file.readlines()

        # Update specific configurations
        updated_lines = []
        for line in lines:
            if line.startswith("title ="):
                updated_lines.append(f"title = {title}\n")
            elif line.startswith("package.name ="):
                updated_lines.append(f"package.name = {package_name}\n")
            elif line.startswith("package.domain ="):
                updated_lines.append(f"package.domain = {package_domain}\n")
            elif line.startswith("# (str) Icon of the application"):
                updated_lines.append(line)
                updated_lines.append("icon.filename = icon.png\n")
            else:
                updated_lines.append(line)

        # Write updates back to buildozer.spec
        with open(spec_file, "w") as file:
            file.writelines(updated_lines)
        print("Updated buildozer.spec.")
    else:
        print("buildozer.spec not found. Please run 'buildozer init' first.")


def build_apk():
    """
    Build the APK using Buildozer.
    """
    print("Building APK...")
    run_command("buildozer -v android debug")


def main():
    # Configuration
    project_name = "my_webapp"
    website_url = "https://example.com"
    icon_path = "icon.png"  # Replace with your icon file path if any
    app_title = "My Web App"
    package_name = "webapp"
    package_domain = "com.mycompany"

    # Step 1: Create Project Structure
    create_project_structure(project_name, website_url, icon_path)

    # Step 2: Initialize Buildozer
    initialize_buildozer(project_name)

    # Step 3: Update Buildozer Configuration
    update_buildozer_spec(project_name, app_title, package_name, package_domain)

    # Step 4: Build APK
    build_apk()


if __name__ == "__main__":
    main()
