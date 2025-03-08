
Культура и инструменты open source разработки
=============================================

Оглавление
----------


* Раздел 1. Введение, подходы к программированию

  * `Терминология </educational_materials/terms/content.md>`_
  * `Командная строка как универсальный способ взаимодействия с любым компьютером </educational_materials/bash/content.md>`_

    * `Задачи </educational_materials/bash/exercises.md>`_
    * `Вопросы </educational_materials/bash/quiz.md>`_

  * `Система контроля версий git. Основные понятия. Работа с локальным репозиторием. Локальное использование </educational_materials/git_base/content.md>`_
  * `Основы командной работы </educational_materials/team_work_on_a_project/content.md>`_

    * `Задачи </educational_materials/team_work_on_a_project/exercises.md>`_
    * `Вопросы </educational_materials/team_work_on_a_project/quiz.md>`_

  * `Знакомство с платформами размещения исходного кода программ на примере GitFlic. </educational_materials/team_work_on_a_gitflic/content.md>`_

    * `Задачи </educational_materials/team_work_on_a_gitflic/exercises.md>`_
    * `Вопросы </educational_materials/team_work_on_a_gitflic/quiz.md>`_

  * `Среды разработки. Основные возможности </educational_materials/ide/content.md>`_
  * `Оформление кода. Виды стилей. Автоматические средства для форматирование </educational_materials/styles/content.md>`_

    * `Задачи </educational_materials/styles/exercises.md>`_
    * `Вопросы </educational_materials/styles/quiz.md>`_

  * `Зачем нужно документирование. Учимся читать и использовать в своем проекте чужой код с Github </educational_materials/github/content.md>`_

* Раздел 2. Работа над проектом

  * `Стадии жизни проекта </educational_materials/stages/content.md>`_
  * `Работа над MVP. Этапы разработки и проверка гипотез </educational_materials/mvp/content.md>`_
  * `UML диаграммы </educational_materials/uml/content.md>`_

    * `Задачи </educational_materials/uml/exercises.md>`_
    * `Вопросы </educational_materials/uml/quiz.md>`_

  * `Код -> Библиотека </educational_materials/code_to_lib/content.md>`_

    * `Задачи </educational_materials/code_to_lib/exercises.md>`_
    * `Вопросы </educational_materials/code_to_lib/quiz.md>`_

  * `Основы Open Source </educational_materials/open_source/content.md>`_
  * `Обзор открытых лицензий и типов проектов, для которых они подходят </educational_materials/open_license/content.md>`_
  * `Создаем свой первый статичный сайт на GitHub Pages </educational_materials/github_pages/content.md>`_

    * `Задачи </educational_materials/github_pages/exercises.md>`_
    * `Вопросы </educational_materials/github_pages/quiz.md>`_

* Раздел 3. Инструменты

  * `Знакомство с рабочим окружением. Системное окружение. Создание виртуального окружения venv для проекта </educational_materials/path_venv/content.md>`_

    * `Задачи </educational_materials/path_venv/exercises.md>`_
    * `Вопросы </educational_materials/path_venv/quiz.md>`_

  * `Стандарты составления документации к коду и приложению </educational_materials/docs/content.md>`_

    * `Задачи </educational_materials/docs/exercises.md>`_
    * `Вопросы </educational_materials/docs/quiz.md>`_

  * `Автотесты и культура разработки кода test-driven-development </educational_materials/testing/content.md>`_

    * `Задачи </educational_materials/testing/exercises.md>`_
    * `Вопросы </educational_materials/testing/quiz.md>`_

  * `Логирование работы приложения </educational_materials/logging/content.md>`_

    * `Задачи </educational_materials/logging/exercises.md>`_
    * `Вопросы </educational_materials/logging/quiz.md>`_

  * `Менеджеры пакетов Python. Сборка проекта </educational_materials/packaging/content.md>`_

    * `Задачи </educational_materials/packaging/exercises.md>`_
    * `Вопросы </educational_materials/packaging/quiz.md>`_

  * `Управление вызовом приложений: автоматизация процессов посредством планировщика задач crontab и systemctl </educational_materials/managers/content.md>`_

    * `Задачи </educational_materials/managers/exercises.md>`_
    * `Вопросы </educational_materials/managers/quiz.md>`_

  * `Контейнеризация на примере Docker. </educational_materials/docker_base/content.md>`_

    * `Задачи </educational_materials/docker_base/exercises.md>`_
    * `Вопросы </educational_materials/docker_base/quiz.md>`_

* Дополнительные материалы

  * `Концепция сети в Docker </educational_materials/docker_network/content.md>`_
  * `Реестр Docker </educational_materials/docker_hub/content.md>`_

Сборка
------

Создайте виртуальное окружение (опционально):

.. code-block:: bash

   conda create -n sphinx_md python=3.10
   conda activate sphinx_md

Установите sphinx и поддержку markdown:

.. code-block:: bash

   pip install sphinx
   pip install --upgrade myst-parser

Соберите html (находясь в корневой директории проекта):

.. code-block:: bash

   make html

В корневой директории появится папка build, где будет находиться собранная документация.

Для сборки pdf установите latexmk и поддержку кириллицы:

.. code-block:: bash

   sudo apt install latexmk
   sudo apt install texlive-lang-cyrillic
   make latexpdf
