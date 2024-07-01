Скрипт для экспорта показателей пропускной способности из джиры по набору фильтров (компонент, категория и трудоемкость задачи) для команды коммуникационного дизайна Мегамаркета (проект CMMDS).

Результат — таблица `output.csv`, где для каждой комбинации категории и трудоемкости запроса рендерится 3 столбца: открытые задачи, закрытые задачи, дельта (незакрытые задачи).
Период выгрузки — 32 недели, строка = неделя.

Перед использованием:
1. вставить свой токен авторизации в 17 строке (нужно создать его в настройках профиля джиры)
2. заменить список компонентов, данные которых хотим получить (например, для команды промо это будут "promo" и "promo-federal")
