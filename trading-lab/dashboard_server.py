#!/usr/bin/env python3
"""
Trading Lab Dashboard Server with Password Protection
Access: http://localhost:8000
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import base64
import os

# Set password here
DASHBOARD_PASSWORD = "123Spz@#shopify"  # Change this to your preferred password
DASHBOARD_USER = "admin"

class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the request path
        parsed_path = urlparse(self.path)
        
        # Allow dashboard.html only with auth
        if 'dashboard.html' in self.path:
            # Check for Authorization header
            auth_header = self.headers.get('Authorization', '')
            
            if not auth_header:
                # No auth header, prompt for login
                self.send_response(401)
                self.send_header('WWW-Authenticate', 'Basic realm="Trading Lab Dashboard"')
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"""
                    <html>
                    <head><title>Login Required</title></head>
                    <body style="font-family: Arial; text-align: center; padding: 50px;">
                        <h1>Trading Lab Dashboard</h1>
                        <p>Username and password required</p>
                        <p style="color: #666; font-size: 0.9em;">Username: admin</p>
                    </body>
                    </html>
                """)
                return
            
            # Parse auth header
            try:
                auth_type, auth_string = auth_header.split(' ', 1)
                if auth_type.lower() != 'basic':
                    self.send_response(401)
                    self.end_headers()
                    return
                
                # Decode credentials
                decoded = base64.b64decode(auth_string).decode('utf-8')
                username, password = decoded.split(':', 1)
                
                # Check credentials
                if username != DASHBOARD_USER or password != DASHBOARD_PASSWORD:
                    self.send_response(401)
                    self.send_header('WWW-Authenticate', 'Basic realm="Trading Lab Dashboard"')
                    self.end_headers()
                    return
                
                # Auth successful, serve the file
                self.path = '/dashboard.html'
                
            except Exception as e:
                self.send_response(401)
                self.end_headers()
                return
        
        # Serve other files normally
        super().do_GET()
    
    def end_headers(self):
        # Add cache control
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

def run_server(port=8000):
    """Start the dashboard server"""
    os.chdir('/root/.openclaw/workspace/trading-lab')
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, DashboardHandler)
    
    print(f"""
    ╔════════════════════════════════════════════════════════════╗
    ║       Trading Lab Dashboard - Started                      ║
    ╠════════════════════════════════════════════════════════════╣
    ║                                                            ║
    ║  📊 Dashboard: http://localhost:{port}/dashboard.html      ║
    ║  👤 Username:  admin                                       ║
    ║  🔑 Password:  {DASHBOARD_PASSWORD}                    ║
    ║                                                            ║
    ║  Auto-refresh: Every 30 seconds                           ║
    ║  Local only: No external access                           ║
    ║                                                            ║
    ║  Press Ctrl+C to stop                                     ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✅ Dashboard stopped.")
        httpd.server_close()

if __name__ == '__main__':
    run_server(port=8000)
