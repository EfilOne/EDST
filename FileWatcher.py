# File watcher

import sys
import time 
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class JournalHandler(PatternMatchingEventHandler):
	pattern = ["*.log"]

	def process(self, event):
		"""
		event.event_type
			'modified' | 'created' | 'moved' | 'deleted'
		event.is_directory
			True | False
		event.src_path
			~\Saved Games\Frontier Developments\Elite Dangerous
		"""
		# File will be processed here
		############################# <--
		# File will be processed here

		print(event.src_path, event.event_type)

	def on_modified(self,event):
		self.process(event)

	def on_created(self, event):
		self.process(event)

# Observer schedule task
if __name__ == '__main__':
	args = sys.argv[1:]
	observer = Observer()
	observer.schedule(JournalHandler(), path=args[0] if args else '.')
	observer.start()

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()

	observer.join()