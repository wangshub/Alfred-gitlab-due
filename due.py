# encoding: utf-8
import sys
import argparse
from workflow import Workflow
from datetime import datetime
from datetime import timedelta


def get_date(date_fmt='%Y-%m-%d', add_days=0):
    another_date = (datetime.now() + timedelta(days=add_days))
    week = another_date.strftime('%A')
    return another_date.strftime(date_fmt), week


def main(wf):
    parser = argparse.ArgumentParser()
    parser.add_argument('--days', dest='days', nargs='?', default=None)
    args = parser.parse_args(wf.args)

    add_days = 7

    try:
        add_days = int(args.days) if args.days else add_days
    except:
        wf.add_item(title='Wrong days fmt, need a number')
        wf.send_feedback()
        return

    another_date, week = get_date(add_days=add_days)
    gitlab_cmd = '/due {}'.format(another_date)
    wf.add_item(title='Due in {}'.format(another_date),
                subtitle=week,
                arg=gitlab_cmd,
                valid=True)
    wf.send_feedback()
    return


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
