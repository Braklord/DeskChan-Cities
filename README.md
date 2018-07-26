![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
![DeskChan](https://img.shields.io/badge/DeskChan-Plugin-blue.svg)
![Version](https://img.shields.io/badge/Version-0.7-blue.svg)
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
![TeamCity CodeBetter](https://img.shields.io/teamcity/codebetter/bt428.svg)



## Игра в "Города"
Плагин на Python, созданный для проекта [DeskChan](https://github.com/DeskChan/DeskChan)

### Правила игры [(Википедия)](https://ru.wikipedia.org/wiki/Города_(игра))
> Города́ — игра для нескольких (двух или более) человек, в которой каждый 
> участник в свою очередь называет реально существующий город любой страны,
> название которого начинается на ту букву, которой оканчивается название 
> предыдущего участника.

Небольшое изменение: В этот раз ты будешь играть против своего персонального ассистента.

### Планируется сделать:
- [x] Алгоритм выбора города и сравнение с базой данных
- [x] В зависимисти от игровой ситуации изменять эмоцию скина ассистента
- [x] Достать массив настроек характера ассистента ДЧ и последующая экстракция величины "Опыт"
- [ ] Включить в игру возможность выигрыша против ассистента ДЧ, в зависимости от величины "Опыт"
- [ ] Изменить алгоритм поиска города на нужную букву - сейчас поиск проходит в 
порядке появления в списке, что делает противника предсказуемым.

### Зависимости/библиотеки:

For Windows user: You will need to install [Python 3](https://www.python.org/downloads/release/python-370/).
While the installation process you have to "*add Python 3.x to PATH*". After the reboot type 'python' in your command prompt.
If you don't get an error, your installation was successful.
Notice you can also use the pip for automatic updates of the (also missing) libraries.

To update pip himself, type in your command prompt:
```
python -m pip install --upgrade pip
```