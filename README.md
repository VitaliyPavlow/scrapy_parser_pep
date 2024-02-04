# Проект парсинга PEP при помощи фреймворка Srapy

### Описание:
Проект предназначен для парсинга документов PEP с официального сайта.

### Что на выходе?
Два csv файла в папке results. Один содержит номер, название и актуальный статус PEP-документа.
Второй представляет собой саммари по количеству документов в каждом статусе и итоговую сумму.

### Управление из коммандной строки
Для запуска скрипта из командной строки:
```
scrapy crawl pep
```

### Установка
Клонировать репозиторий и перейти в него в командной строке:

```git@github.com:VitaliyPavlow/scrapy_pareser_pep```

Cоздать и активировать виртуальное окружение:

Команды для Windows:

```py -m venv venv```

```source venv/Scripts/activate```

Команды для Linux и macOS:

```python3 -m venv venv```

```source venv/bin/activate``` 
 

Обновить пакетный менеджер pip:

```py -m pip install --upgrade pip``` - для Windows.

```python3 -m pip install --upgrade pip``` - для Linux и macOS.

Установить зависимости из файла requirements.txt:

```pip install -r requirements.txt```

*Запускать парсер необходимо из корневой папки проекта /scrapy_parser_pep.*