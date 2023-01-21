![](https://github.com/rizwanbutt314/telegram-bot/rbtalks.gif)

### Description:
This telegram chat bot contains the usage of GUI & commands based actions.

### PreReqs:
* Python: 3.6+

### Setup:
* create a virtual environment: `virtualenv -p /usr/bin/python3 env` (Optional)
* activate the environemnt: `source ./env/bin/activate` (Optional when you don't need first step)
* install requirements: `pip install -r requirements.txt`
* Edit `constants.py` file to update the bot token
* Run `python main.py` to start the bot listener


### Folders:
* `commands/`:
    * This folder contains the folders with name as command name and have specific
    structure of files which will be dynamically loaded on bot start.

* `filters/`:
    * This folder contains the custom filters which will be used to limit the scope of command/handler. For example, `/start` command should only work in private-chat.


### Specific command file structure:
* `start/` (folder name as command)
    * main.py:
        * Required - This file should have function `executor(message, bot)`
    * handlers.py:
        * Optional - If this file is present then it should have functions:
            `query_handler(call, bot)` and `query_handler_filter(call)`
    * menu.py:
        * Optional - This contains the logic to generate the menu buttons for a command
    * messages.py:
        * Optional - This contains the messages constants for a specific command

### To add new command:
* Create a new folder inside `commands/` folder 
* Name of the folder should be the command name like `start: folder-name` and it's command will be automatically `/start`
* Create `main.py` file inside this new folder and it should contain the following function as follow:
    ```
    def executor(message, bot):
        pass
    ```
* Otherwise the dynamically loading commands process will fail because of invalid structure.

### To add new callback query handler for a command:
* Create `handlers.py` file inside the specific command folder and it should contain the following functions as follow:
    ```
    def query_handler_filter(call):
        pass

    def query_handler(call, bot):
        pass
    ```
* Otherwise the dynamically loading handlers process will fail because of invalid structure.

