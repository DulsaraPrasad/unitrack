from app import app
import os

OUTPUT_DIR = 'build'

# List of paths to export as static HTML. Only non-authenticated pages are useful
# because GitHub Pages can't run server-side code (sessions, DB, uploads).
PATHS = [
    '/',
    '/login',
    '/forgot-password',
]


def path_to_filepath(path: str) -> str:
    # Normalize path to file path inside OUTPUT_DIR
    if path == '/' or path == '':
        return os.path.join(OUTPUT_DIR, 'index.html')
    p = path.lstrip('/')
    if p.endswith('/'):
        p = p[:-1]
    # If no extension, add .html
    if os.path.splitext(p)[1] == '':
        p = p + '.html'
    return os.path.join(OUTPUT_DIR, p)


def save_response(path: str, response_data: bytes):
    filepath = path_to_filepath(path)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'wb') as f:
        f.write(response_data)
    print(f'Wrote {filepath}')


def main():
    # Ensure output dir exists and is empty
    if os.path.exists(OUTPUT_DIR):
        # Remove only files we will overwrite; keep simple by recreating
        pass
    else:
        os.makedirs(OUTPUT_DIR)

    client = app.test_client()

    for path in PATHS:
        print(f'Fetching {path} ...')
        resp = client.get(path, follow_redirects=True)
        if resp.status_code == 200:
            save_response(path, resp.data)
        else:
            print(f'Warning: {path} returned status {resp.status_code}')
    
    # Create .nojekyll to ensure GitHub Pages serves the site correctly
    nojekyll_path = os.path.join(OUTPUT_DIR, '.nojekyll')
    with open(nojekyll_path, 'w') as f:
        f.write('')
    print(f'Wrote {nojekyll_path}')


if __name__ == '__main__':
    main()
