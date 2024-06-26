import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class OnMyWatch:
    # Set the directory on watch
    watchDirectory = '.'

    def __init__(self) -> None:
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("File changed - Running testing.py")
            subprocess.run(["python", "testing.py"])


if __name__ == "__main__":
    watch = OnMyWatch()
    watch.run()
