#!python3
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.options import options
import os
import sys
import signal
import logging
from run_bash_command_in_python import run_command

cl = []
is_closing = False


def signal_handler(signum, frame):
    global is_closing
    logging.info("Exiting...")
    is_closing = True


def try_exit():
    global is_closing
    if (is_closing):
        tornado.ioloop.IOLoop.instance().stop()
        logging.info("Exit success")


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        if self not in cl:
            cl.append(self)

    def on_message(self, message):
        print("client --> server: %s" % message)
        if not "sudo" in message:
            out = run_command(message)

            if not out == "":
                for client in cl:
                    client.write_message(out)

    def on_close(self):
        if self in cl:
            cl.remove(self)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        '''Respond to GET request from client.
        '''
        self.render(
            "index.html", message="Response to GET request from client.")


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
    # application.listen(8000)
    # tornado.ioloop.IOLoop.current().start()

    tornado.options.parse_command_line()
    signal.signal(signal.SIGINT, signal_handler)
    application.listen(8000)
    tornado.ioloop.PeriodicCallback(try_exit, 1000).start()
    tornado.ioloop.IOLoop.instance().start()
