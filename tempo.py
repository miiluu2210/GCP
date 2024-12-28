import http.client
import ssl

# Enable legacy renegotiation
ssl_context = ssl.create_default_context()
ssl_context.options |= ssl.OP_LEGACY_SERVER_CONNECT

conn = http.client.HTTPSConnection("https://bidv.com.vn/ServicesBIDV/InterestDetailServlet", context=ssl_context)

try:
    conn.request("GET", "https://bidv.com.vn/ServicesBIDV/InterestDetailServlet")
    response = conn.getresponse()
    print(f"Status: {response.status}")
    print("Response:")
    print(response.read().decode('utf-8', errors='replace'))
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()
