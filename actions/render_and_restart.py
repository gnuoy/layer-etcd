#!/usr/local/sbin/charm-env python3

from charms.templating.jinja2 import render
from charmhelpers.core import host

from etcd_databag import EtcdDatabag

def render_config():
    bag = EtcdDatabag()

    conf_path = "{}/etcd.conf.yml".format(bag.etcd_conf_dir)
    render('etcd3.conf', conf_path, bag.__dict__, owner='root',
           group='root')
    host.service_restart(bag.etcd_daemon)

if __name__ == '__main__':
    render_config()
