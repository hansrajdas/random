def get_host_and_port(url):
  server = url.split('/')[2]
  if len(server.split(':')) > 1:
    return server.split(':')
  return server, 80 if url.split('/')[0][:-1] == 'http' else 443


a, b = get_host_and_port('http://localhost:8080/abc/def/health')
print a, b

a, b = get_host_and_port('https://localhost:9090/abc/def/health')
print a, b

a, b = get_host_and_port('http://localhost/abc/def/health')
print a, b

a, b = get_host_and_port('https://localhost/abc/def/health')
print a, b

a, b = get_host_and_port('http://10.207.1.2:90/abc/def/health')
print a, b

a, b = get_host_and_port('http://10.207.1.2/abc/def/health')
print a, b
