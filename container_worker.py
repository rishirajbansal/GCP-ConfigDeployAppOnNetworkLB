
import yaml


def GenerateManifest(context):

  env_list = []
  if 'dockerEnv' in context.properties:
    for key, value in context.properties['dockerEnv'].iteritems():
      env_list.append({'name': key, 'value': str(value)})

  manifest = {
      'apiVersion': 'v1',
      'kind': 'Pod',
      'metadata': {
          'name': str(context.env['name'])
          },
      'spec': {
          'containers': [{
              'name': str(context.env['name']),
              'image': context.properties['dockerImage'],
              'ports': [{
                  'hostPort': context.properties['port'],
                  'containerPort': context.properties['port']
                  }],
              }]
          }
      }

  if env_list:
    manifest['spec']['containers'][0]['env'] = env_list

  return yaml.dump(manifest, default_flow_style=False)