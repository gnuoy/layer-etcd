#!/usr/local/sbin/charm-env python3

from charmhelpers.core.hookenv import is_leader
from charmhelpers.core.hookenv import leader_set
from charms.templating.jinja2 import render
from charmhelpers.core import host

from etcd_databag import EtcdDatabag
from etcd_lib import get_ingress_address
from etcdctl import get_connection_string

def render_config():
    bag = EtcdDatabag()

    conf_path = "{}/etcd.conf.yml".format(bag.etcd_conf_dir)
    render('etcd3.conf', conf_path, bag.__dict__, owner='root',
           group='root')
    host.service_restart(bag.etcd_daemon)
    address = get_ingress_address('cluster')
    if is_leader():
        leader_set({'leader_address':
                   get_connection_string(
                       [address],
                       bag.port,
                       protocol='http')})


if __name__ == '__main__':
    render_config()
