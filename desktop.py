import threading
import time
import sys
import os
import webbrowser
from urllib.request import urlopen, URLError

from app import app, create_dummy_data

try:
    import webview
    WEBVIEW_AVAILABLE = True
except Exception:
    WEBVIEW_AVAILABLE = False


def run_server(host='127.0.0.1', port=5000):
    # Run the Flask development server in a background thread
    app.run(host=host, port=port, debug=False, use_reloader=False)


def wait_for_server(url, timeout=10):
    start = time.time()
    while time.time() - start < timeout:
        try:
            resp = urlopen(url)
            if resp:
                return True
        except URLError:
            time.sleep(0.2)
    return False


def main():
    # Initialize DB if needed
    create_dummy_data()

    host = '127.0.0.1'
    port = 5000
    url = f'http://{host}:{port}/'

    server_thread = threading.Thread(target=run_server, kwargs={'host': host, 'port': port}, daemon=True)
    server_thread.start()

    print('Starting server...')
    ok = wait_for_server(url, timeout=10)
    if not ok:
        print('Error: server did not start in time.')
        sys.exit(1)

    print(f'Server running at {url}')

    # Choose GUI strategy
    use_gui = WEBVIEW_AVAILABLE and (sys.platform == 'win32' or sys.platform == 'darwin' or os.environ.get('DISPLAY'))

    if use_gui:
        try:
            webview.create_window('UniTrack', url, width=1100, height=800)
            webview.start()
        except Exception as e:
            print('pywebview failed, falling back to browser:', e)
            webbrowser.open(url)
    else:
        print('Opening default browser...')
        webbrowser.open(url)

    try:
        # Keep the main thread alive while the server (daemon thread) and GUI run
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Shutting down...')


if __name__ == '__main__':
    main()
