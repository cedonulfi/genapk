# GenAPK

**GenAPK** is a Python-based automation tool for converting websites or Python applications into APK files using **Kivy** and **Buildozer**. It simplifies the process from project setup to APK generation, allowing you to quickly transform your web-based ideas or Python apps into Android applications with minimal effort.

---

## Features

- **Convert Websites to APK**: Easily turn any website into an Android app using a WebView in Kivy.
- **Convert Python Apps to APK**: Quickly package your Python-based applications into APKs.
- **Automated Setup**: Automatically creates project structure, generates `main.py`, and configures `buildozer.spec`.
- **Icon Integration**: Easily add an app icon to your APK.
- **Customizable Settings**: Modify package name, title, domain, and other Buildozer configurations automatically.
- **Cross-Platform**: Build APKs for Android directly from Python code.

---

## Technologies Used

- **Python**: Programming language for scripting and automation.
- **Kivy**: Python library for building cross-platform applications, including Android.
- **Buildozer**: A tool for compiling Python apps into Android packages (APK).
- **WebView**: Used in Kivy to display websites inside the Android application.

---

## Requirements

Before using **GenAPK**, ensure that the following are installed on your system:

- **Python 3.8–3.10**: Required to run the automation script.
- **Kivy**: Install using `pip install kivy`.
- **Buildozer**: Install using `pip install buildozer`.
- **Android SDK** and **NDK**: Required for building APKs (can be installed via Buildozer or manually).
- **Java JDK**: Required for Android development.
  
---

## Installation

### Step 1: Install Dependencies

Make sure Python 3.8–3.10 is installed on your system. Then, install Kivy and Buildozer:

```bash
pip install kivy buildozer
```

### Step 2: Install Android SDK, NDK, and Java

You can install these tools manually or allow **Buildozer** to download them for you when building the APK.

---

## How to Use

### Step 1: Prepare the Script

1. Clone the repository or download the `GenAPK` script:

```bash
git clone https://github.com/cedonulfi/genapk.git
cd genapk
```

2. Edit the `GenAPK.py` script to set your desired configurations:
   - **Website URL**: Set the website you want to convert to an APK (or the path to your Python app).
   - **Icon**: Optionally, set the path to an icon image (e.g., `icon.png`).
   - **Project Name**: Set the name of your project.

### Step 2: Run the Script

Execute the `GenAPK.py` script:

```bash
python GenAPK.py
```

This will:
- Create a project folder.
- Generate a `main.py` file with Kivy code to display the website (or Python app).
- Initialize **Buildozer** and create a `buildozer.spec` file.
- Update the `buildozer.spec` file with the project settings like title, package name, and icon.
- Automatically build the APK using **Buildozer**.

### Step 3: Locate the APK

After the script runs successfully, you can find the generated APK in the `bin` folder of your project:

```plaintext
my_webapp/bin/mywebapp-0.1-debug.apk
```

---

## Contributing

We welcome contributions! Whether you have ideas to improve **GenAPK** or want to help with bug fixes, please feel free to contribute.

### How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License

**GenAPK** is licensed under the [MIT License](LICENSE).

---

## Let's Learn and Share Knowledge Together!

Feel free to open issues or discussions. Whether you're a beginner or an expert, we're here to learn and grow together in the world of automation and Python development. Happy coding! 🚀

