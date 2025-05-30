<strong>Проект предназначен для ознакомления с возможностью создания приложения по технологии REST API, реализующий методы CRUD (создание, чтение, обновление, удаление)</strong> 
через сетевые HTTP запросы.

<b>Для запуска проекта необходимо:</b>

- Cоздать виртуальное окружение проекта.
  - Сделать это можно при создании нового проекта в программе PyCharm выбрав папку виртуального окружения
    и пакетный менеджер из предложенных. Или же виртуальное окружение можно установить через командную строку. Для примера я буду использовать пакетный 
    менеджер 'UV' с установкой через командную строку.
  - Для установки UV в командной строке нужно ввести команду pip install uv
    создаем виртуальное окружение и переходим в его директорию uv init venv и cd venv. После создания в директории проекта появится файл pyproject.toml который будет 
    содержать установленные зависимости после установки пакетов.
  - Установить пакет flasck командой uv add flask
- <b>Наконец запустить сервер командой uv run main.py</b>
  - После запуска сервера в командной строке появится надпись Running on http://127.0.0.1:5000, данная строка нам говорит что сервер успешно запустился.
  - Для тестов нашего сервера будем использовать программу POSTMAN, для этого создадим новый WORKSPACES.

- Запрос на создание твита будет выглядеть следующим образом http://127.0.0.1:5000/twit c установленным методом "POST", а в теле запроса установив на вкладку "RAW" 
  выбрать тип данных "json" ввести запись в виде словаря {'body': 'Hello World', 'author': 'Pavel'}
- Для чтения твитов необходимо передать тот же запрос http://127.0.0.1:5000/twit только с методом "GET".
- Для обновления твита необходимо выбрать метод "UPDATE" и передать запрос по тому же адресу http://127.0.0.1:5000/twit, предварительно изменив тело запроса 
  например {'body': 'Bye World', 'author': 'Mariy'} по умолчанию редактируется первый твит.
- Для удаления твита применяется метод "DELETE" по адресу http://127.0.0.1:5000/twit, по умолчанию удаляется последний твит.
