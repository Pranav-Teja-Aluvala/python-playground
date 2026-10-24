# Python Playground

Four small command-line projects for practicing Python: arithmetic, game logic, classes and text-file storage. They use only the standard library.

## Projects

| Project | What it does | Run from the repository root |
| --- | --- | --- |
| [Calculator](calculator/) | Arithmetic and powers using a `Calculator` class | `python calculator/calc.py` |
| [Rock Paper Scissors](rock-paper-scissors/) | Play against a random computer choice | `python rock-paper-scissors/rock_paper.py` |
| [Task Manager](task-manager/) | Add, remove, view and save tasks | `python task-manager/to-do.py` |
| [File Handling](file-handling/) | A smaller add-and-view task list | `python file-handling/files.py` |

## Run

Requires Python 3. No packages need to be installed.

```bash
git clone https://github.com/Pranav-Teja-Aluvala/python-playground.git
cd python-playground
python calculator/calc.py
```

The two task-list programs use `data/tasks.txt` relative to your current folder. Running both from the repository root makes them share that file. Task Manager also writes `data/saved_tasks.txt`; its Load action displays the saved copy.

These are learning exercises. Input handling is still uneven: the calculator expects numeric inputs, and Rock Paper Scissors restarts through recursive calls after a loss or tie.

