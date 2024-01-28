import argparse
import multiprocessing as mp
from plot3d.td_app import TDApp
from plot3d.td_client import TDClient

def run():
    # Argument parsing
    parser = argparse.ArgumentParser(description='Plot3D')
    parser.add_argument('--port', type=int, default=9000, help='Port to use for the Plot3D app')
    args = parser.parse_args()

    # Start the VisPy application process
    app = TDApp(port=args.port)
    app_proc = mp.Process(target=app.run)
    app_proc.start()

    # Wait until for keyboard interrupt
    try:
        app_proc.join()
    except KeyboardInterrupt:
        # Send a close signal to the app
        app_proc.terminate()
        app_proc.join()

if __name__ == '__main__':
    # Run
    run()
