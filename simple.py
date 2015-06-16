# Copyright (C) 2014 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import socket
import time

from ryu.base import app_manager

from ryu.lib import hub
from ryu.lib.hub import StreamServer


class Demo(app_manager.RyuApp):
    def __init__(self):
        super(Demo, self).__init__()
        self.name = 'demo'
        # self.server_host = os.environ.get('RYU_BMP_SERVER_HOST', '0.0.0.0')
        # self.server_port = int(os.environ.get('RYU_BMP_SERVER_PORT', 11019))
        self.server_host = '0.0.0.0'
        self.server_port = 2200

    def start(self):
        super(Demo, self).start()
        self.logger.debug("listening on %s:%s", self.server_host,
                          self.server_port)

        return hub.spawn(StreamServer((self.server_host, self.server_port),
                                      self.loop).serve_forever)

    def loop(self, sock, addr):
        self.logger.debug("simple client connected, ip=%s, port=%s", addr[0],
                          addr[1])
        is_active = True

        while is_active:
            ret = sock.recv(4096)
            if len(ret) == 0:
                is_active = False
                break
            t = time.strftime("%Y %b %d %H:%M:%S", time.localtime())
            self.logger.debug("%s | %s | %s\n", t, addr[0], ret)

        self.logger.debug("simple client disconnected, ip=%s, port=%s", addr[0],
                          addr[1])

        sock.close()
