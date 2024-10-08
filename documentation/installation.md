# Installation Guide for MML (Modern Markup Language)

Welcome to the installation guide for Modern Markup Language (MML). This document covers how to install the compiler and set up the development environment for working with MML files.

## Prerequisites

Ensure that you have the following installed on your system before proceeding:
- [Node.js](https://nodejs.org/) (for the JavaScript version of the compiler)
- [Python 3](https://www.python.org/downloads/) (for the Python version of the compiler)
- [Visual Studio Code](https://code.visualstudio.com/) (for the MML VSCode extension)

---

## 1. Install the Python or JavaScript Compiler

### Python Compiler

1. Clone the repository containing the MML Python compiler:
   ```bash
   git clone https://github.com/your-username/mml-compiler-python.git
   cd mml-compiler-python
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the compiler to convert `.mml` files to `.html`:
   ```bash
   python mml_compiler.py path_to_mml_file.mml
   ```

   The compiled HTML file will be generated in the same directory as the input `.mml` file.

### JavaScript Compiler (Node.js)

1. Clone the repository containing the MML JavaScript compiler:
   ```bash
   git clone https://github.com/your-username/mml-compiler-js.git
   cd mml-compiler-js
   ```

2. Install the necessary packages:
   ```bash
   npm install
   ```

3. Use the compiler to convert `.mml` files to `.html`:
   ```bash
   node mml_compiler.js path_to_mml_file.mml
   ```

   The output HTML file will be created in the same directory as the input `.mml` file.

---

## 2. Install the VSCode Extension

To make your MML development easier, we provide a VSCode extension that adds syntax highlighting and basic support for `.mml` files.

1. Open Visual Studio Code.
2. Go to the Extensions tab (or press `Ctrl+Shift+X`).
3. Search for `MML Lang Support` in the marketplace.
4. Click **Install** on the `MML Lang Support` extension by `your-username`.

Once installed, you can open `.mml` files in VSCode, and they will have proper syntax highlighting.

---

## 3. Install via NPM (WIP)

We are currently working on providing a package for MML that can be installed via NPM. This package will allow you to easily install and use the MML compiler in JavaScript projects.

Once released, you will be able to install the package with the following command:

```bash
npm install mml-compiler
```

Stay tuned for updates on the NPM package release!

---

That's it! You're now ready to start developing with Modern Markup Language (MML). For more details on MML syntax and usage, please refer to the full documentation.