
def GenerateConfig(context):

  backend = context.env['deployment'] + '-backend'
  frontend = context.env['deployment'] + '-view'
  firewall = context.env['deployment'] + '-application-fw'
  application_port = 8080
  mysql_port = 8080
  resources = [{
      'name': backend,
      'type': 'container_vm.py',
      'properties': {
          'zone': context.properties['zone'],
          'dockerImage': 'test.demo/mysql',
          'containerImage': 'family/cos-stable',
          'port': mysql_port
      }
  }, {
      'name': view,
      'type': 'view.py',
      'properties': {
          'zone': context.properties['zone'],
          'dockerImage': 'test.demo/viewservice',
          'port': application_port,
          'dockerEnv': {
              'SEVEN_SERVICE_MYSQL_PORT': mysql_port,
              'SEVEN_SERVICE_PROXY_HOST': '$(ref.' + backend + '.networkInterfaces[0].networkIP)'
          },
          'size': 2,
          'maxSize': 20
      }
  }, {
      'name': firewall,
      'type': 'compute.v1.firewall',
      'properties': {
          'allowed': [{
              'IPProtocol': 'TCP',
              'ports': [application_port]
          }],
          'sourceRanges': ['0.0.0.0/0']
      }
  }]
  return {'resources': resources}