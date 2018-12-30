from gi.repository import Gtk


class MouseButtons:
    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3


class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):

        self.darea = Gtk.DrawingArea()
        self.darea.connect("draw", self.on_draw)
        # self.darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.add(self.darea)

        self.coords = []

        self.darea.connect("button-press-event", self.on_button_press)

        self.set_title("Lines")
        self.resize(300, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_draw(self, wid, cr):
        cr.move_to(20, 30)
        cr.show_text("S")
        cr.move_to(10, 20)
        cr.show_text("S")
        # cr.set_source_rgb(0, 0, 0)
        # cr.set_line_width(0.5)
        # cr.move_to(0, 1)
        # cr.line_to(100, 100)
        # cr.stroke()
        # for i in self.coords:
        #     for j in self.coords:
        #         cr.move_to(i[0], i[1])
        #         cr.line_to(j[0], j[1])
        #         cr.stroke()
        #
        # del self.coords[:]

    def on_button_press(self, w, e):
        print(e)
        # if e.type == Gdk.EventType.BUTTON_PRESS \
        #         and e.button == MouseButtons.LEFT_BUTTON:
        #     self.coords.append([e.x, e.y])
        #
        # if e.type == Gdk.EventType.BUTTON_PRESS \
        #         and e.button == MouseButtons.RIGHT_BUTTON:
        #     self.darea.queue_draw()


def main():
    app = Example()
    Gtk.main()


if __name__ == "__main__":
    main()