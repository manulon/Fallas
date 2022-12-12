from app import app
import os

# do some production specific things to the app
if os.environ.get('DEBUG', False):
    app.config['DEBUG'] = True
else:
    app.config['DEBUG'] = False

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6002))
    app.run(host='0.0.0.0', port=port)
