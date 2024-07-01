from atlassian import Jira
import csv
import time
import sys

# CLI анимация прогресса
def animate():
    chars = "|/-\\"
    for char in chars:
        sys.stdout.write(f'\r{char} Processing...')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')

# подключение к Jira
JIRA_INSTANCE_URL = "https://project.samokat.ru/"
JIRA_TOKEN = "" # ваш токен авторизации
jira = Jira(url=JIRA_INSTANCE_URL, token=JIRA_TOKEN)

# фильтры
components = ["promo", "promo-federal"] # компонент для выгрузки
categories = ["Процедуры", "Седина", "Мозги"]
severities = ["XS", "S", "M", "L", "XL"]

# логика
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    header_row_1 = ["Week"] + [f"{category} {severity}" for category in categories for severity in severities for _ in ["created", "resolved", "delta"]]
    header_row_2 = [""] + ["created", "resolved", "delta"] * len(categories * severities)
    writer.writerow(header_row_1)
    writer.writerow(header_row_2)
    for week_number in range(-32, 0):
        row_data = [f'Week {week_number + 33}']
        for category in categories:
            for severity in severities:
                base_jql = f'project in ("CommDes") AND component IN ({components}) AND "Категория" = "{category}" AND Severity = "{severity}"'
                jql_query = f"{base_jql} AND resolved >= startOfWeek({week_number}w) and resolved <= endOfWeek({week_number}w)"
                resolved_issues_result = jira.jql(jql_query)
                resolved_issues = resolved_issues_result.get('total', 0)
                jql_query = f"{base_jql} AND created >= startOfWeek({week_number}w) and created <= endOfWeek({week_number}w)"
                created_issues_result = jira.jql(jql_query)
                created_issues = created_issues_result.get('total', 0)
                delta = resolved_issues - created_issues
                row_data.extend([created_issues, resolved_issues, delta])
        writer.writerow(row_data)
    animate()
print("CSV file created successfully.")