import sys
import shutil
from app import freezer, app

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        shutil.rmtree('./app/build')
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)
