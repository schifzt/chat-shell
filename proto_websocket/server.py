#!python3
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.options import options
import os
import sys
import signal
import logging
import subprocess
from run_bash_command_in_python import run_command
from tab_completion import complete_command

cl = []
is_closing = False
timeout = 1
prohibited_commands = ["sudo", "rm"]


def signal_handler(signum, frame):
    global is_closing
    logging.info("Exiting...")
    is_closing = True


def try_exit():
    global is_closing
    if (is_closing):
        tornado.ioloop.IOLoop.instance().stop()
        logging.info("Exit success.")


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        if self not in cl:
            cl.append(self)

    def on_message(self, message):
        print("client --> server: \'%s\'" % message)

        if message[:3] == "___":    
            # message is an incomplete word
            out = b"___" + (b"\n" if message[3:] == "" else complete_command(message[3:]))
        elif any(cmd in message for cmd in prohibited_commands):
            # message is a prohibited command
            out = ("Command \'{}\' is prohibited.".format(message)).encode()
        else:
            # message is a complete command
            out = run_command(message, timeout)

        for client in cl:
            client.write_message(out)



    def on_close(self):
        if self in cl:
            cl.remove(self)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


BASE_DIR = os.path.dirname(__file__)
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", WebSocketHandler),
],
    template_path=os.path.join(BASE_DIR, "templates"),
    static_path=os.path.join(BASE_DIR, "static"),
    autoreload=True,
    debug=True,
)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    signal.signal(signal.SIGINT, signal_handler)
    application.listen(8000)
    tornado.ioloop.PeriodicCallback(try_exit, 1000).start()
    tornado.ioloop.IOLoop.instance().start()
