# Ansible Collection - my_own_namespace.yandex_cloud_elk

Yandex Cloud ELK Ansible Collection
Эта коллекция предоставляет Ansible инструменты для управления ELK (Elasticsearch, Logstash, Kibana) в Yandex Cloud. Включая в себя модули для деплоя, настройки и мониторинга.

Содержимое
my_own_module: Этот модуль позволяет создавать и редактировать файлы на управляемой машине. Он предоставляет базовые функции для работы с текстовыми файлами, такими как изменение содержимого или задание прав на файл.

Роль my_role: Эта роль автоматизирует процесс создания файлов на управляемых машинах с использованием модуля my_own_module. Она также обеспечивает настройки по умолчанию и может быть легко интегрирована в более крупные проекты.

Использование
Установка коллекции
Для установки этой коллекции, используйте следующую команду:

```
ansible-galaxy collection install my_own_namespace.yandex_cloud_elk
```

Использование модуля
Пример задачи с использованием модуля my_own_module:

```
---
- hosts: localhost
  tasks:
    - name: Create a file using my_own_module
      my_own_namespace.yandex_cloud_elk.my_own_module:
        path: "/tmp/example.txt"
        content: "Hello, Yandex Cloud ELK!"

```

Использование роли
Для использования роли my_role в вашем playbook:

```
---
- hosts: localhost
  collections:
    - my_own_namespace.yandex_cloud_elk
  roles:
    - my_role

```

Убедитесь, что вы указали нужные параметры в group_vars или передали их напрямую в playbook.

