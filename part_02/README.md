# GitHub

[Git book](https://git-scm.com/book/ru/v2)

Перенос нового проекта в репозиторий на GitHub
```
git init
git add part_01/
git add ...
git add ...
...
git commit -m "add part_01"
git remote add origin https://github.com/YOUR_REP/introduction.git
git push -u origin master
```

Склонировать существующий проект к себе
```
git clone https://github.com/folknik/introduction.git
```

Создать новую ветку от текущей ветки и сразу в нее перейти
```
git checkout -b develop
```

Просто перейти в другую ветку
```
git checkout develop
```

Показать ссылку на удаленный репозиторий
```
git remote -v
```

Посмотреть все коммиты в удаленный репозиторий
```
git log
```

Сменить указатель в текущей ветке на другой коммит
```
git checkout <commit_hash>
```

Конфиг, email & name
```
git config --global user.name "NEW NAME"
git config --global user.mail "NEW MAIL"
```

