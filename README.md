# Вычислитель различий в конфигурационных файлах в форматах json и yml

## Статусы

### Статусы workflow actions

[![Actions Status](https://github.com/experiment0/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/experiment0/python-project-50/actions)
[![hexlet-check](https://github.com/experiment0/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/experiment0/python-project-50/actions/workflows/hexlet-check.yml)
[![Python CI](https://github.com/experiment0/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/experiment0/python-project-50/actions/workflows/pyci.yml)

### Статусы [SonarQube](https://sonarcloud.io/)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-50&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-50)

## О проекте

Данный проект создан в процессе прохождения курса [Python-разработчик](https://ru.hexlet.io/programs/python).\
В нем реализован скрипт для вычисления различий между двумя файлами в форматах `json` или `yml`.

## Инструкция по запуску

1. Проверить, установлена ли утилита `uv`:

   ```bash
   uv --version
   ```

   Если не установлена, то нужно установить [по инструкции](https://docs.astral.sh/uv/getting-started/installation/#installation-methods).

2. Установка пакета из данного репо:

   ```sh
   uv tool install --force git+https://github.com/experiment0/python-project-50.git
   ```

   Флаг `--force` нужен на случай, если данный пакет уже был установлен ранее.

3. Утилита запускается командой `gendiff` и принимает следующие праметры.
   | Параметры | Пример вызова | Результат |
   | ---       | ---           | ---       |
   | `-h` или `--help` | `gendiff -h` или<br />`gendiff --help` | Выведет справку. |
   | Позиционные аргументы:<br /> `filepath1` - путь к исходной версии файла;<br />`filepath1` - путь к версии файла после изменений. <br />Принимает файлы в форматах: `json`, `yaml`, `yml`. | `gendiff ./file1.json file2.json` | Выведет различия в формате `stylish`. <br /> Формат вывода `stylish` используется по умолчанию. |
   Именованный аргумент<br /> с доступными форматами вывода.<br /> `-f` или `--format`<br /> Может принимать значения:<br />`stylish`, `stylish_colored`, `json`, `plain`. | `gendiff -f plain ./file1.yml file2.yml` | Выведет различия в формате `plain`.<br /> Вид форматов вывода<br /> можно посмотреть в демо ниже. |

4. Демонстрация работы скрипта:

   [![asciicast](https://asciinema.org/a/tstZArOclkMDlGRq7BEyhSqg1.svg)](https://asciinema.org/a/tstZArOclkMDlGRq7BEyhSqg1)
