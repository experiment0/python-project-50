# Загружает зависимости проекта
install:
	uv sync

# Прогоняет все тесты
test:
	uv run pytest

# Проверяет покрытие кода тестами и формирует отчет в файле coverage.xml
# Далее этот файл использует SonarCloud для анализа
test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

# Проверяет код в папке gendiff на соответствие правилам линтера из ruff.toml
lint:
	uv run ruff check gendiff

# Исправляет замечания линтера, не связанные с логикой (порядок импортов, пробелы, и т.д.)
fix:
	uv run ruff check --fix gendiff

# Прогоняет сначала тесты, потом проверку линтером
check: test lint

# Формирует сборку пакета в папку dist
build:
	uv build

# Инсталлирует пакет, чтобы была возможность вызывать скрипт gendiff командой из консоли
package-install:
	uv tool install dist/hexlet_code-0.1.0-py3-none-any.whl

# Переустанавливает пакет, если он был установлен ранее
package-reinstall:
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl

# Команды, которые могут совпадать с именами директорий и не должны быть с ними перепутаны
.PHONY: install test lint selfcheck check build
