# Pip

> ❗: Commands should be executed inside this dir. Tip: `cd ./10-pip`.

## What is `pip`

Pip is the package manager of python ecosystem. Allows to install external python modules created by other developers.

To install pip, run this command:

```bash
python -m ensurepip --upgrade
```

After this, we can install packages, but will be installed in global dependencies. To avoid this, we can use `venv` to create a virtual python environment in this directory and install modules without compromising global pyhton environment.

To use `venv`, ejecute this commands:

```bash
python -m venv venv # Create virtual python environment in the dir where the command is executed
source source venv/bin/activate # In Linux/Mac, starts a virtual session.
```

After that commands, a dir `venv` is created and an isolated environment to run python commands will be started. To execute code using directory installed dependencies with `pip`, don't use global python global binary, use `venv` one:

```bash
./venv/bin/python3 <python-file>.py
```

## `pip` commands

```bash
pip install <package> # Install a package
pip uninstall <package> # Uninstall package
pip freeze > requirements.txt # Create a file with installed packages
pip install -r requirements.txt # Install packages from requirements.txt
```

## How to use dirs using `pip` and `venv`

1. Creates a virtual python environment to install packages in this dir:

```bash
python -m venv venv
```

2. Load `venv`:

   **Mac/Linux**:

   ```bash
   source venv/bin/activate
   ```

   **Windows**:

   ```
   .\venv\Scripts\activate
   ```

3. Install requirements:

```
pip install -r requirements.txt
```

5. Run script **using environment pyhton**:

```bash
./venv/bin/python3 . # Will execute __main__.py
./venv/bin/python3 __main__.py # Same result

# Will prompt: True
```
