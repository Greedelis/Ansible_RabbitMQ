# Simple Ansible RabbitMQ playbook for Debian
Simple Ansbile playbook to setup RabbitMQ on Debian system

This playbook installs Erlang, RabbitMQ, setups admin page and setups firewall

roles/rabbitmq/vars/main.yml variable file is encrypted and password for RabbitMQ users is stored

Firewall rules are configured using templates and variables. Firewall rules can be described in host_vars for any host individualy.
By default, RabbitMQ 5672 port is only accessable form localhost, and admin page on port 15674 is accessable from anywhere

To run this playbook simply run:

```
ansible-playbook playbook/setup_rabbitmq.yml --ask-vault-pass
```

and enter ansible-vault pass to continue (if none of the files are encrypted using ansible-vault, --ask-vault-pass is not needed)



## Producer
In main.py is there is a script, that creates test exchange and queue, binds that test exchange to queue and sends couple sample messages

replace rabbitmq_host, rabbitmq_user, rabbitmq_pass, and rabbitmq_vhost values with actual values you use, for script to work.
THIS SCRIPT NEED pika pip package.

scipt can be simply ran using this command

```
python3 main.py
```


all .yml files passed ansible-lint check