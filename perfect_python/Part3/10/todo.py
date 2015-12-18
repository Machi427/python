#!/usr/local/bin/python3.3
# -*- coding:utf-8 -*-
import sys
import shelve
import argparse
from datetime import datetime

def create_task(name, due_date, required_time):
    return dict(name=name, due_date=due_date, required_time=required_time, finished=False)


def format_task(task):
    state = "完了" if task['finished'] else "未完了"
    format = "{state} {task[name]}: {task[due_date]:%Y-%m-%d}まで 予定所要時間{task[required_time]}分"
    return format.format(task=task, state=state)


def finish_task(task):
    task['finished'] = True


def next_task_name(db):
    id = db.get('next_id', 0)
    db['next_id'] = id + 1
    return "task:{0}".format(id)


def add_task(db, task):
    key = next_task_name(db)
    db[key] = task


def all_task(db):
    for key in db:
        if key.startswith('task:'):
            yield key, db[key]


def unfinished_tasks(db):
    return ((key, task)
            for key, task in all_task(db) 
            if not task['finished'])


def cmd_add(args):
    name = input('task name:')
    due_date = datetime.strptime(input('due date [Y-m-d]:'), '%Y-%m-%d')
    required_time = int(input('required_time:'))

    task = create_task(name, due_date, required_time)
    add_task(args.db, task)


def cmd_list(args):
    if args.all:
        tasks = all_task(args.db)
    else:
        tasks = unfinished_tasks(args.db)

    for key, task in tasks:
        print("{0} {1}".format(key, format_task(task)))


def cmd_finish(args):
    task = args.db[args.task]
    finish_task(task)
    args.db[args.task] = task


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('shelve')
    
    subparsers = parser.add_subparsers()
    add_parser = subparsers.add_parser('add')
    add_parser.set_defaults(func=cmd_add)
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('-a', '--all', action="store_true")
    list_parser.set_defaults(func=cmd_list)
    finish_parser = subparsers.add_parser('finish')
    finish_parser.add_argument('task')
    finish_parser.set_defaults(func=cmd_finish)

    args = parser.parse_args()
    
    db = shelve.open(args.shelve, 'c')
    try:
        args.db = db
        if hasattr(args, 'func'):
            args.func(args)
        else:
            parser.print_help()
    finally:
        db.close()


if __name__ == '__main__':
    main()
