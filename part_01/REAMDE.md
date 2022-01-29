# Virtual environment

Создание нового окружения и его активация

```
cd part_01/
python3 -m venv new_env
source new_env/bin/activate
```

Деактивация ранее активированного виртуального окружения
```
deactivate
```

Настройка виртуального окружения в PyCharm - [link](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter)

Установка дополнительных пакетов в новое окружение
```
pip install pyyaml
pip install numpy==1.22.0
```

Вывести список всех пакетов
```
pip list
```

Вывести список пакетов в файл requirements.txt
```
pip freeze > requirements.txt
```

Установка списка пакетов из готового файла requirements.txt
```
pip install -r requirements.txt
```